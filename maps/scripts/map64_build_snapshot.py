#!/usr/bin/env python3
"""Build Map 64's country-level electricity-access snapshot."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path


INDICATORS = {
    "EG.ELC.ACCS.ZS": "national",
    "EG.ELC.ACCS.UR.ZS": "urban",
    "EG.ELC.ACCS.RU.ZS": "rural",
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
    parser.add_argument("country_metadata", type=Path)
    parser.add_argument("country_geojson", type=Path)
    parser.add_argument("indicator_json", nargs=3, type=Path)
    args = parser.parse_args()

    country_doc = json.loads(args.country_metadata.read_text(encoding="utf-8"))
    allowed = {
        item["id"]
        for item in country_doc[1]
        if item.get("region", {}).get("value") != "Aggregates" and len(item.get("id", "")) == 3
    }
    values: dict[str, dict[str, list[float | int]]] = {}
    source_meta = {}
    for path in args.indicator_json:
        doc = json.loads(path.read_text(encoding="utf-8"))
        indicator_id = doc[1][0]["indicator"]["id"]
        metric = INDICATORS.get(indicator_id)
        if not metric:
            raise SystemExit(f"unexpected indicator {indicator_id}")
        source_meta[metric] = {
            "indicator": indicator_id,
            "last_updated": doc[0]["lastupdated"],
            "rows": doc[0]["total"],
        }
        for row in doc[1]:
            iso3 = row.get("countryiso3code", "")
            if iso3 not in allowed or row.get("value") is None:
                continue
            try:
                year, value = int(row["date"]), float(row["value"])
            except (TypeError, ValueError):
                continue
            if not math.isfinite(value) or not 0 <= value <= 100:
                continue
            current = values.setdefault(iso3, {}).get(metric)
            if current is None or year > current[0]:
                values[iso3][metric] = [year, round(value, 2)]

    source = json.loads(args.country_geojson.read_text(encoding="utf-8"))
    features, matched = [], set()
    for feature in source["features"]:
        props = feature.get("properties", {})
        candidates = [props.get(k) for k in ("ISO_A3", "ISO_A3_EH", "ADM0_A3", "SOV_A3", "GU_A3")]
        iso3 = next((code for code in candidates if code in values), None)
        if not iso3 or iso3 in matched:
            continue
        matched.add(iso3)
        features.append({
            "type": "Feature",
            "properties": {"iso3": iso3, "name": props.get("NAME_LONG") or props.get("ADMIN") or iso3},
            "geometry": {"type": feature["geometry"]["type"], "coordinates": round_coords(feature["geometry"]["coordinates"])},
        })
    features.sort(key=lambda f: f["properties"]["iso3"])
    payload = {
        "schema": "map64-electricity-access-v1",
        "built_on": "2026-10-31",
        "source": "World Bank SDG 7.1.1 Electrification Dataset",
        "source_meta": source_meta,
        "metrics": {
            "national": {"label": "All people", "unit": "% of population"},
            "urban": {"label": "Urban", "unit": "% of urban population"},
            "rural": {"label": "Rural", "unit": "% of rural population"},
        },
        "countries_with_values": len(values),
        "mapped_countries": len(matched),
        "unmapped_iso3": sorted(set(values) - matched),
        "values": {code: values[code] for code in sorted(values)},
        "countries": {"type": "FeatureCollection", "features": features},
    }
    raw = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    print(json.dumps({
        "output": str(args.output),
        "output_bytes": args.output.stat().st_size,
        "output_sha256": sha256(args.output),
        "country_metadata_sha256": sha256(args.country_metadata),
        "country_geojson_sha256": sha256(args.country_geojson),
        "indicator_sha256": {p.name: sha256(p) for p in args.indicator_json},
        "countries_with_values": len(values),
        "mapped_countries": len(matched),
        "unmapped_iso3": payload["unmapped_iso3"],
        "metric_counts": {m: sum(m in item for item in values.values()) for m in ("national", "urban", "rural")},
    }, indent=2))


if __name__ == "__main__":
    main()
