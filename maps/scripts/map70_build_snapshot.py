#!/usr/bin/env python3
"""Build Map 70's dated country electricity-mix and CO2 snapshot."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def finite(value: str) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def verify_snapshot(path: Path) -> None:
    compressed = path.read_bytes()
    raw = gzip.decompress(compressed)
    document = json.loads(raw)
    canonical = (json.dumps(document, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    if raw != canonical or compressed != gzip.compress(canonical, compresslevel=9, mtime=0):
        raise SystemExit("snapshot is not canonical deterministic gzip")
    if document.get("schema") != "map70-energy-mix-emissions-v1":
        raise SystemExit("unexpected snapshot schema")
    mapped = {feature["properties"]["iso3"] for feature in document["countries"]["features"]}
    energy = co2 = mapped_energy = mapped_co2 = 0
    for code, values in document["values"].items():
        if len(code) != 3:
            raise SystemExit(f"invalid ISO3 code: {code}")
        if "energy" in values:
            energy += 1
            year, nuclear, fossil, renewable = values["energy"]
            if not isinstance(year, int) or not all(math.isfinite(value) and 0 <= value <= 100 for value in (nuclear, fossil, renewable)) or not 99 <= nuclear + fossil + renewable <= 101:
                raise SystemExit(f"invalid energy row: {code}")
            mapped_energy += code in mapped
        if "co2" in values:
            co2 += 1
            year, value = values["co2"]
            if not isinstance(year, int) or not math.isfinite(value) or value < 0:
                raise SystemExit(f"invalid CO2 row: {code}")
            mapped_co2 += code in mapped
    expected = (document["countries_with_energy"], document["countries_with_co2"], document["mapped_energy"], document["mapped_co2"])
    actual = (energy, co2, mapped_energy, mapped_co2)
    if actual != expected:
        raise SystemExit(f"snapshot count mismatch: {actual} != {expected}")
    print(json.dumps({"verified": str(path), "bytes": len(compressed), "sha256": sha256(path), "counts": actual}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("output", type=Path)
    parser.add_argument("energy_csv", type=Path, nargs="?")
    parser.add_argument("co2_csv", type=Path, nargs="?")
    parser.add_argument("boundary_snapshot", type=Path, nargs="?")
    args = parser.parse_args()

    if args.verify_only:
        verify_snapshot(args.output)
        return
    if None in (args.energy_csv, args.co2_csv, args.boundary_snapshot):
        parser.error("energy_csv, co2_csv and boundary_snapshot are required when building")

    energy: dict[str, list[float | int]] = {}
    with args.energy_csv.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            code = row.get("Code", "")
            if len(code) != 3:
                continue
            nuclear = finite(row.get("Nuclear", ""))
            fossil = finite(row.get("Fossil fuels", ""))
            renewable = finite(row.get("Renewables", ""))
            try:
                year = int(row["Year"])
            except (KeyError, TypeError, ValueError):
                continue
            if None in (nuclear, fossil, renewable):
                continue
            assert nuclear is not None and fossil is not None and renewable is not None
            if not all(0 <= value <= 100 for value in (nuclear, fossil, renewable)):
                continue
            if not 99.0 <= nuclear + fossil + renewable <= 101.0:
                continue
            if code not in energy or year > energy[code][0]:
                energy[code] = [year, round(nuclear, 2), round(fossil, 2), round(renewable, 2)]

    co2: dict[str, list[float | int]] = {}
    with args.co2_csv.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            code = row.get("Code", "")
            value = finite(row.get("CO₂ emissions per capita", ""))
            try:
                year = int(row["Year"])
            except (KeyError, TypeError, ValueError):
                continue
            if len(code) != 3 or value is None or value < 0:
                continue
            if code not in co2 or year > co2[code][0]:
                co2[code] = [year, round(value, 3)]

    with gzip.open(args.boundary_snapshot, "rt", encoding="utf-8") as handle:
        boundary_doc = json.load(handle)
    countries = boundary_doc["countries"]
    mapped = {feature["properties"]["iso3"] for feature in countries["features"]}
    codes = sorted(set(energy) | set(co2))
    values = {
        code: {
            **({"energy": energy[code]} if code in energy else {}),
            **({"co2": co2[code]} if code in co2 else {}),
        }
        for code in codes
    }
    payload = {
        "schema": "map70-energy-mix-emissions-v1",
        "built_on": "2026-11-05",
        "sources": {
            "energy": {
                "title": "Share of electricity generation from fossil fuels, renewables and nuclear",
                "provider": "Ember (2026) and other sources, with major processing by Our World in Data",
                "last_updated": "2026-06-30",
                "latest_year": max(item[0] for item in energy.values()),
            },
            "co2": {
                "title": "Territorial fossil and industrial CO2 emissions per capita",
                "provider": "Global Carbon Budget (2025) and population sources, with major processing by Our World in Data",
                "last_updated": "2025-11-13",
                "latest_year": max(item[0] for item in co2.values()),
            },
            "boundaries": "Natural Earth boundaries previously stored for Map 68",
        },
        "metrics": {
            "renewable": {"label": "Renewables share of electricity", "unit": "%"},
            "fossil": {"label": "Fossil-fuel share of electricity", "unit": "%"},
            "nuclear": {"label": "Nuclear share of electricity", "unit": "%"},
            "co2": {"label": "Territorial CO₂ emissions per capita", "unit": "t/person"},
        },
        "countries_with_energy": len(energy),
        "countries_with_co2": len(co2),
        "mapped_energy": len(set(energy) & mapped),
        "mapped_co2": len(set(co2) & mapped),
        "unmapped_energy_iso3": sorted(set(energy) - mapped),
        "unmapped_co2_iso3": sorted(set(co2) - mapped),
        "values": values,
        "countries": countries,
    }
    raw = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    print(json.dumps({
        "output": str(args.output),
        "output_bytes": args.output.stat().st_size,
        "output_sha256": sha256(args.output),
        "energy_csv_sha256": sha256(args.energy_csv),
        "co2_csv_sha256": sha256(args.co2_csv),
        "boundary_snapshot_sha256": sha256(args.boundary_snapshot),
        "countries_with_energy": len(energy),
        "countries_with_co2": len(co2),
        "mapped_energy": payload["mapped_energy"],
        "mapped_co2": payload["mapped_co2"],
        "energy_latest_year": payload["sources"]["energy"]["latest_year"],
        "co2_latest_year": payload["sources"]["co2"]["latest_year"],
        "unmapped_energy_iso3": payload["unmapped_energy_iso3"],
        "unmapped_co2_iso3": payload["unmapped_co2_iso3"],
    }, indent=2))


if __name__ == "__main__":
    main()
