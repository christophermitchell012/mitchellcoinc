#!/usr/bin/env python3
"""Build Map 56's dated NBI condition rasters and compact state summary."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

from PIL import Image, ImageDraw

SIZE = 8192
STATE_NAMES = {
    "01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO",
    "09": "CT", "10": "DE", "11": "DC", "12": "FL", "13": "GA", "15": "HI",
    "16": "ID", "17": "IL", "18": "IN", "19": "IA", "20": "KS", "21": "KY",
    "22": "LA", "23": "ME", "24": "MD", "25": "MA", "26": "MI", "27": "MN",
    "28": "MS", "29": "MO", "30": "MT", "31": "NE", "32": "NV", "33": "NH",
    "34": "NJ", "35": "NM", "36": "NY", "37": "NC", "38": "ND", "39": "OH",
    "40": "OK", "41": "OR", "42": "PA", "44": "RI", "45": "SC", "46": "SD",
    "47": "TN", "48": "TX", "49": "UT", "50": "VT", "51": "VA", "53": "WA",
    "54": "WV", "55": "WI", "56": "WY", "60": "AS", "66": "GU", "69": "MP",
    "72": "PR", "78": "VI",
}
COLORS = {
    "G": (71, 214, 150, 210),
    "F": (255, 191, 105, 215),
    "P": (239, 92, 105, 230),
}


def dms(value: str, latitude: bool) -> float | None:
    raw = (value or "").strip()
    digits = 8 if latitude else 9
    if len(raw) != digits or not raw.isdigit():
        return None
    deg_len = 2 if latitude else 3
    deg = int(raw[:deg_len])
    minute = int(raw[deg_len:deg_len + 2])
    second = int(raw[deg_len + 2:deg_len + 4]) + int(raw[-2:]) / 100
    result = deg + minute / 60 + second / 3600
    return result if latitude else -result


def pixel(lon: float, lat: float) -> tuple[int, int]:
    lat = max(-85.05112878, min(85.05112878, lat))
    x = (lon + 180) / 360
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2
    return round(x * (SIZE - 1)), round(y * (SIZE - 1))


def coordinate_pairs(value):
    if isinstance(value, list) and len(value) >= 2 and all(isinstance(v, (int, float)) for v in value[:2]):
        yield float(value[0]), float(value[1])
    elif isinstance(value, list):
        for item in value:
            yield from coordinate_pairs(item)


def state_validation_bounds(data_dir: Path) -> dict[str, list[float]]:
    result: dict[str, list[float]] = {}
    for path in data_dir.glob("county-geometry-2025-cb20m-v1-*.geojson"):
        payload = json.loads(path.read_text())
        for feature in payload.get("features", []):
            state = feature.get("properties", {}).get("state")
            if not state:
                continue
            for lon, lat in coordinate_pairs(feature.get("geometry", {}).get("coordinates", [])):
                if state not in result:
                    result[state] = [lon, lat, lon, lat]
                else:
                    box = result[state]
                    box[0] = min(box[0], lon); box[1] = min(box[1], lat)
                    box[2] = max(box[2], lon); box[3] = max(box[3], lat)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("zipfile", type=Path, help="FHWA 2025 delimited all-state ZIP")
    parser.add_argument("output_dir", type=Path, help="Destination maps/data directory")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    images = {key: Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0)) for key in COLORS}
    draws = {key: ImageDraw.Draw(image) for key, image in images.items()}
    state_counts: dict[str, Counter] = defaultdict(Counter)
    bounds: dict[str, list[float]] = {}
    totals = Counter()
    valid = 0
    invalid_coordinates = 0
    unknown_condition = 0
    coordinate_outliers = 0
    records: list[tuple[str, str, float, float]] = []
    validation_bounds = state_validation_bounds(args.output_dir)

    with zipfile.ZipFile(args.zipfile) as archive:
        member = next(name for name in archive.namelist() if name.lower().endswith(".txt"))
        with archive.open(member) as binary:
            rows = csv.DictReader((line.decode("latin-1") for line in binary), quotechar="'")
            for row in rows:
                condition = (row.get("BRIDGE_CONDITION") or "").strip()
                if condition not in COLORS:
                    unknown_condition += 1
                    continue
                lat = dms(row.get("LAT_016", ""), True)
                lon = dms(row.get("LONG_017", ""), False)
                if lat is None or lon is None or not (-90 <= lat <= 90 and -180 <= lon <= 180):
                    invalid_coordinates += 1
                    continue
                state = STATE_NAMES.get((row.get("STATE_CODE_001") or "").zfill(2), (row.get("STATE_CODE_001") or "").strip())
                if abs(lat) < 10 or abs(lon) < 50:
                    invalid_coordinates += 1
                    continue
                records.append((state, condition, lat, lon))

    grouped: dict[str, list[tuple[str, str, float, float]]] = defaultdict(list)
    for record in records:
        grouped[record[0]].append(record)
    centers = {state: (statistics.median(r[2] for r in group), statistics.median(r[3] for r in group))
               for state, group in grouped.items()}

    for state, condition, lat, lon in records:
        center_lat, center_lon = centers[state]
        source_box = validation_bounds.get(state)
        outside_reference = source_box and not (
            source_box[0] - 0.75 <= lon <= source_box[2] + 0.75
            and source_box[1] - 0.75 <= lat <= source_box[3] + 0.75
        )
        lat_limit, lon_limit = ((16, 32) if state == "AK" else (8, 16))
        outside_robust = abs(lat - center_lat) > lat_limit or abs(lon - center_lon) > lon_limit
        if outside_reference or outside_robust:
            coordinate_outliers += 1
            continue
        x, y = pixel(lon, lat)
        color = COLORS[condition]
        draws[condition].ellipse((x - 1, y - 1, x + 1, y + 1), fill=color)
        totals[condition] += 1
        state_counts[state][condition] += 1
        valid += 1
        if state not in bounds:
            bounds[state] = [lon, lat, lon, lat]
        else:
            box = bounds[state]
            box[0] = min(box[0], lon); box[1] = min(box[1], lat)
            box[2] = max(box[2], lon); box[3] = max(box[3], lat)

    files = {}
    for condition, label in (("G", "good"), ("F", "fair"), ("P", "poor")):
        path = args.output_dir / f"map56-fhwa-nbi-{label}-2025.png"
        images[condition].save(path, optimize=True)
        files[label] = {"path": str(path), "bytes": path.stat().st_size}

    payload = {
        "source": "FHWA National Bridge Inventory",
        "source_vintage": "2025",
        "source_file_last_modified": "2025-06-16",
        "render": "Three transparent 8192 px Web Mercator overview rasters; each valid bridge record is drawn as a three-pixel-diameter point.",
        "valid_coordinate_records": valid,
        "excluded_invalid_coordinates": invalid_coordinates,
        "excluded_coordinate_outliers": coordinate_outliers,
        "excluded_unknown_condition": unknown_condition,
        "condition_counts": {"good": totals["G"], "fair": totals["F"], "poor": totals["P"]},
        "states": [
            {
                "state": state,
                "bounds": [round(value, 5) for value in bounds[state]],
                "conditions": {
                    "good": state_counts[state]["G"],
                    "fair": state_counts[state]["F"],
                    "poor": state_counts[state]["P"],
                },
            }
            for state in sorted(state_counts)
        ],
    }
    summary = args.output_dir / "map56-fhwa-nbi-state-summary-2025.json"
    summary.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False) + "\n")
    print(json.dumps({"summary": str(summary), "summary_bytes": summary.stat().st_size, "rasters": files, **payload}, indent=2))


if __name__ == "__main__":
    main()
