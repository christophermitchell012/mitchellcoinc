#!/usr/bin/env python3
"""Build and verify Map 73's deterministic ACS county housing snapshot."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import re
import struct
import zipfile
from pathlib import Path

SCHEMA = "map73-acs-housing-cost-burden-v1"
COUNTY_ID = re.compile(r"^0500000US(\d{5})$")
STATE_NAMES = {
    "01": ("Alabama", "AL"), "02": ("Alaska", "AK"), "04": ("Arizona", "AZ"),
    "05": ("Arkansas", "AR"), "06": ("California", "CA"), "08": ("Colorado", "CO"),
    "09": ("Connecticut", "CT"), "10": ("Delaware", "DE"), "11": ("District of Columbia", "DC"),
    "12": ("Florida", "FL"), "13": ("Georgia", "GA"), "15": ("Hawaii", "HI"),
    "16": ("Idaho", "ID"), "17": ("Illinois", "IL"), "18": ("Indiana", "IN"),
    "19": ("Iowa", "IA"), "20": ("Kansas", "KS"), "21": ("Kentucky", "KY"),
    "22": ("Louisiana", "LA"), "23": ("Maine", "ME"), "24": ("Maryland", "MD"),
    "25": ("Massachusetts", "MA"), "26": ("Michigan", "MI"), "27": ("Minnesota", "MN"),
    "28": ("Mississippi", "MS"), "29": ("Missouri", "MO"), "30": ("Montana", "MT"),
    "31": ("Nebraska", "NE"), "32": ("Nevada", "NV"), "33": ("New Hampshire", "NH"),
    "34": ("New Jersey", "NJ"), "35": ("New Mexico", "NM"), "36": ("New York", "NY"),
    "37": ("North Carolina", "NC"), "38": ("North Dakota", "ND"), "39": ("Ohio", "OH"),
    "40": ("Oklahoma", "OK"), "41": ("Oregon", "OR"), "42": ("Pennsylvania", "PA"),
    "44": ("Rhode Island", "RI"), "45": ("South Carolina", "SC"), "46": ("South Dakota", "SD"),
    "47": ("Tennessee", "TN"), "48": ("Texas", "TX"), "49": ("Utah", "UT"),
    "50": ("Vermont", "VT"), "51": ("Virginia", "VA"), "53": ("Washington", "WA"),
    "54": ("West Virginia", "WV"), "55": ("Wisconsin", "WI"), "56": ("Wyoming", "WY"),
    "72": ("Puerto Rico", "PR"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_bytes(document: dict) -> bytes:
    return (json.dumps(document, ensure_ascii=False, separators=(",", ":")) + "\n").encode()


def number(row: dict[str, str], field: str) -> int | None:
    try:
        value = int(row[field])
    except (KeyError, TypeError, ValueError):
        return None
    return value if value >= 0 else None


def share(numerator: list[int | None], denominator: int | None, not_computed: int | None) -> tuple[float | None, int]:
    usable = None if denominator is None else denominator - (not_computed or 0)
    if usable is None or usable <= 0 or any(value is None for value in numerator):
        return None, max(0, usable or 0)
    total = sum(value for value in numerator if value is not None)
    return round(total * 100 / usable, 1), usable


def read_table(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="|"):
            match = COUNTY_ID.match(row.get("GEO_ID", ""))
            if match:
                rows[match.group(1)] = row
    return rows


def read_dbf(raw: bytes) -> list[dict[str, str]]:
    header_length, record_length = struct.unpack_from("<HH", raw, 8)
    fields = []
    offset = 32
    while offset + 32 <= header_length and raw[offset] != 0x0D:
        desc = raw[offset:offset + 32]
        name = desc[:11].split(b"\0", 1)[0].decode("ascii")
        fields.append((name, desc[16]))
        offset += 32
    records = []
    position = header_length
    while position + record_length <= len(raw):
        record = raw[position:position + record_length]
        position += record_length
        if record[:1] == b"*":
            continue
        cursor = 1
        item = {}
        for name, length in fields:
            item[name] = record[cursor:cursor + length].decode("latin-1").strip()
            cursor += length
        records.append(item)
    return records


def signed_area(ring: list[list[float]]) -> float:
    return sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(ring, ring[1:])) / 2


def contains(ring: list[list[float]], point: list[float]) -> bool:
    x, y = point
    inside = False
    for a, b in zip(ring, ring[1:]):
        if (a[1] > y) != (b[1] > y):
            crossing = (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0]
            if x < crossing:
                inside = not inside
    return inside


def group_rings(rings: list[list[list[float]]]) -> list[list[list[list[float]]]]:
    outers = [ring for ring in rings if signed_area(ring) < 0]
    holes = [ring for ring in rings if signed_area(ring) >= 0]
    if not outers and rings:
        largest = max(rings, key=lambda ring: abs(signed_area(ring)))
        outers, holes = [largest], [ring for ring in rings if ring is not largest]
    polygons = [[outer] for outer in outers]
    for hole in holes:
        choices = [(abs(signed_area(poly[0])), poly) for poly in polygons if contains(poly[0], hole[0])]
        if choices:
            min(choices, key=lambda item: item[0])[1].append(hole)
        else:
            polygons.append([hole])
    return polygons


def read_shapes(raw: bytes) -> list[dict | None]:
    if len(raw) < 100 or struct.unpack_from(">i", raw, 0)[0] != 9994:
        raise SystemExit("invalid shapefile header")
    shapes = []
    offset = 100
    while offset + 8 <= len(raw):
        _, words = struct.unpack_from(">ii", raw, offset)
        offset += 8
        content = raw[offset:offset + words * 2]
        offset += words * 2
        shape_type = struct.unpack_from("<i", content, 0)[0]
        if shape_type == 0:
            shapes.append(None)
            continue
        if shape_type != 5:
            raise SystemExit(f"unexpected shapefile geometry type: {shape_type}")
        part_count, point_count = struct.unpack_from("<ii", content, 36)
        starts = list(struct.unpack_from(f"<{part_count}i", content, 44)) + [point_count]
        point_offset = 44 + part_count * 4
        points = [
            [round(x, 5), round(y, 5)]
            for x, y in struct.iter_unpack("<dd", content[point_offset:point_offset + point_count * 16])
        ]
        rings = []
        for start, end in zip(starts, starts[1:]):
            ring = points[start:end]
            if len(ring) >= 4:
                if ring[0] != ring[-1]:
                    ring.append(ring[0])
                rings.append(ring)
        polygons = group_rings(rings)
        shapes.append({"type": "Polygon", "coordinates": polygons[0]} if len(polygons) == 1 else {"type": "MultiPolygon", "coordinates": polygons})
    return shapes


def read_boundaries(path: Path) -> dict[str, tuple[str, dict]]:
    with zipfile.ZipFile(path) as archive:
        shp_name = next(name for name in archive.namelist() if name.endswith(".shp"))
        dbf_name = next(name for name in archive.namelist() if name.endswith(".dbf"))
        shapes = read_shapes(archive.read(shp_name))
        records = read_dbf(archive.read(dbf_name))
    if len(shapes) != len(records):
        raise SystemExit("shapefile and DBF record counts differ")
    return {record["GEOID"]: (record["NAMELSAD"], shape) for record, shape in zip(records, shapes) if shape}


def verify_snapshot(path: Path) -> None:
    compressed = path.read_bytes()
    raw = gzip.decompress(compressed)
    document = json.loads(raw)
    if raw != canonical_bytes(document) or compressed != gzip.compress(raw, compresslevel=9, mtime=0):
        raise SystemExit("snapshot is not canonical deterministic gzip")
    if document.get("schema") != SCHEMA or document.get("source_year") != 2024:
        raise SystemExit("unexpected schema or source year")
    features = document.get("counties", {}).get("features", [])
    if len(features) != document.get("county_count") or len(features) < 3200:
        raise SystemExit("unexpected county count")
    seen = set()
    for feature in features:
        props = feature.get("properties", {})
        geoid = props.get("id")
        if not isinstance(geoid, str) or len(geoid) != 5 or geoid in seen:
            raise SystemExit(f"invalid or duplicate county GEOID: {geoid}")
        seen.add(geoid)
        if feature.get("geometry", {}).get("type") not in {"Polygon", "MultiPolygon"}:
            raise SystemExit(f"invalid geometry: {geoid}")
        for key in ("renter", "mortgaged", "free_clear"):
            value = props.get(key)
            if value is not None and not (0 <= value <= 100 and math.isfinite(value)):
                raise SystemExit(f"invalid percentage: {geoid} {key}")
    print(json.dumps({"verified": str(path), "bytes": len(compressed), "sha256": sha256(path), "counties": len(features)}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("output", type=Path)
    parser.add_argument("rent_table", type=Path, nargs="?")
    parser.add_argument("owner_table", type=Path, nargs="?")
    parser.add_argument("county_boundaries", type=Path, nargs="?")
    args = parser.parse_args()
    if args.verify_only:
        verify_snapshot(args.output)
        return
    if None in (args.rent_table, args.owner_table, args.county_boundaries):
        parser.error("rent_table, owner_table and county_boundaries are required when building")

    rent = read_table(args.rent_table)
    owner = read_table(args.owner_table)
    boundaries = read_boundaries(args.county_boundaries)
    features = []
    for geoid in sorted(set(rent) & set(owner) & set(boundaries)):
        rent_row, owner_row = rent[geoid], owner[geoid]
        renter, renter_units = share(
            [number(rent_row, f"B25070_E{i:03d}") for i in range(7, 11)],
            number(rent_row, "B25070_E001"), number(rent_row, "B25070_E011"),
        )
        mortgaged, mortgaged_units = share(
            [number(owner_row, f"B25091_E{i:03d}") for i in range(8, 12)],
            number(owner_row, "B25091_E002"), number(owner_row, "B25091_E012"),
        )
        free_clear, free_clear_units = share(
            [number(owner_row, f"B25091_E{i:03d}") for i in range(19, 23)],
            number(owner_row, "B25091_E013"), number(owner_row, "B25091_E023"),
        )
        state_name, state_abbr = STATE_NAMES[geoid[:2]]
        name, geometry = boundaries[geoid]
        features.append({
            "type": "Feature",
            "properties": {
                "id": geoid, "name": name, "state": state_name, "abbr": state_abbr,
                "renter": renter, "renter_units": renter_units,
                "mortgaged": mortgaged, "mortgaged_units": mortgaged_units,
                "free_clear": free_clear, "free_clear_units": free_clear_units,
            },
            "geometry": geometry,
        })
    if len(features) < 3200:
        raise SystemExit(f"too few joined county records: {len(features)}")
    payload = {
        "schema": SCHEMA,
        "built_on": "2026-11-09",
        "source_year": 2024,
        "estimate_period": "2020-2024",
        "source_downloaded": "2026-11-09",
        "coverage": "50 states, District of Columbia, and Puerto Rico",
        "county_count": len(features),
        "metrics": {
            "renter": {"label": "Renters paying 30%+ of income", "unit": "%", "table": "B25070"},
            "mortgaged": {"label": "Mortgaged owners paying 30%+", "unit": "%", "table": "B25091"},
            "free_clear": {"label": "Mortgage-free owners paying 30%+", "unit": "%", "table": "B25091"},
        },
        "source_sha256": {
            "b25070": sha256(args.rent_table), "b25091": sha256(args.owner_table),
            "county_boundaries": sha256(args.county_boundaries),
        },
        "counties": {"type": "FeatureCollection", "features": features},
    }
    raw = canonical_bytes(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    verify_snapshot(args.output)


if __name__ == "__main__":
    main()
