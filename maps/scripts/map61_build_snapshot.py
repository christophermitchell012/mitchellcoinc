#!/usr/bin/env python3
"""Build Map 61's country-level FAO SDG 6.4.1 snapshot."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path


ACTIVITIES = {
    "_T": "total",
    "ISIC4_A01_A0210_A0322": "agriculture",
    "ISIC4_BTFXE": "industry",
    "ISIC4_GTT": "services",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def round_coords(value):
    if isinstance(value, list):
        if value and isinstance(value[0], (int, float)):
            return [round(float(x), 3) for x in value]
        return [round_coords(x) for x in value]
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("fao_csv", type=Path)
    parser.add_argument("country_geojson", type=Path)
    args = parser.parse_args()

    values = {name: defaultdict(list) for name in ACTIVITIES.values()}
    source_rows = 0
    with args.fao_csv.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            source_rows += 1
            activity = ACTIVITIES.get(row.get("ACTIVITY"))
            if row.get("SERIES") != "ER_H2O_WUEYST" or row.get("REF_AREA_TYPE") != "3" or not activity:
                continue
            iso3 = row.get("REF_AREA_ISO3", "").strip()
            try:
                year, value = int(row["TIME_PERIOD"]), float(row["OBS_VALUE"])
            except (KeyError, TypeError, ValueError):
                continue
            if len(iso3) != 3 or not math.isfinite(value):
                continue
            values[activity][iso3].append([
                year, round(value, 3), row.get("NATURE", ""), row.get("OBS_STATUS", "")
            ])

    all_iso3 = {iso3 for series in values.values() for iso3 in series}
    source = json.loads(args.country_geojson.read_text(encoding="utf-8"))
    features, matched = [], set()
    for feature in source["features"]:
        props = feature.get("properties", {})
        candidates = [props.get(k) for k in ("ISO_A3", "ISO_A3_EH", "ADM0_A3", "SOV_A3", "GU_A3")]
        iso3 = next((code for code in candidates if code in all_iso3), None)
        if not iso3 or iso3 in matched:
            continue
        matched.add(iso3)
        features.append({
            "type": "Feature",
            "properties": {"iso3": iso3, "name": props.get("NAME_LONG") or props.get("ADMIN") or iso3},
            "geometry": {"type": feature["geometry"]["type"], "coordinates": round_coords(feature["geometry"]["coordinates"])},
        })

    features.sort(key=lambda f: f["properties"]["iso3"])
    for activity in values.values():
        for series in activity.values():
            series.sort(key=lambda item: item[0])
    years = sorted({item[0] for activity in values.values() for series in activity.values() for item in series})
    payload = {
        "schema": "map61-fao-sdg-6-4-1-v1",
        "built_on": "2026-10-29",
        "source_file_last_modified": "2026-07-23T12:30:46Z",
        "indicator": "SDG 6.4.1",
        "unit": "constant 2015 USD per cubic metre",
        "source_rows": source_rows,
        "country_observations": sum(len(series) for activity in values.values() for series in activity.values()),
        "countries_with_values": len(all_iso3),
        "mapped_countries": len(matched),
        "unmapped_iso3": sorted(all_iso3 - matched),
        "years": years,
        "activities": ["total", "agriculture", "industry", "services"],
        "values": {name: {code: activity[code] for code in sorted(activity)} for name, activity in values.items()},
        "countries": {"type": "FeatureCollection", "features": features},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    args.output.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    print(json.dumps({
        "output": str(args.output), "output_bytes": args.output.stat().st_size,
        "output_sha256": sha256(args.output), "fao_csv_sha256": sha256(args.fao_csv),
        "country_geojson_sha256": sha256(args.country_geojson), "source_rows": source_rows,
        "country_observations": payload["country_observations"], "countries_with_values": len(all_iso3),
        "mapped_countries": len(matched), "unmapped_iso3": payload["unmapped_iso3"],
        "year_range": [min(years), max(years)],
        "activity_observations": {name: sum(len(v) for v in activity.values()) for name, activity in values.items()},
    }, indent=2))


if __name__ == "__main__":
    main()
