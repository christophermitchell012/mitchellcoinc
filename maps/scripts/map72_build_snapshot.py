#!/usr/bin/env python3
"""Build and verify Map 72's deterministic NHTSA FARS crash snapshot."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import zipfile
from pathlib import Path

SCHEMA = "map72-fars-fatal-crashes-v1"
EXPECTED_YEAR = 2024
INPUT_MEMBER = "FARS2024NationalCSV/accident.csv"
DICT_FIELDS = (
    "STATENAME", "COUNTYNAME", "CITYNAME", "HARM_EVNAME",
    "RUR_URBNAME", "LGT_CONDNAME", "WEATHERNAME",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_bytes(document: dict) -> bytes:
    return (json.dumps(document, ensure_ascii=False, separators=(",", ":")) + "\n").encode()


def verify_snapshot(path: Path) -> None:
    compressed = path.read_bytes()
    raw = gzip.decompress(compressed)
    document = json.loads(raw)
    if raw != canonical_bytes(document) or compressed != gzip.compress(raw, compresslevel=9, mtime=0):
        raise SystemExit("snapshot is not canonical deterministic gzip")
    if document.get("schema") != SCHEMA or document.get("source_year") != EXPECTED_YEAR:
        raise SystemExit("unexpected schema or source year")
    columns = document.get("columns")
    if columns != ["lat", "lon", "case", "state", "county", "city", "month", "day", "hour", "fatalities", "pedestrians", "persons", "harmful_event", "rural_urban", "light", "weather"]:
        raise SystemExit("unexpected column contract")
    rows = document.get("rows", [])
    dictionaries = document.get("dictionaries", {})
    if len(rows) != document.get("valid_coordinate_crashes") or len(rows) < 30000:
        raise SystemExit("unexpected crash count")
    seen = set()
    fatalities = 0
    for row in rows:
        if len(row) != len(columns):
            raise SystemExit("row width mismatch")
        lat, lon, case = row[:3]
        if not (math.isfinite(lat) and math.isfinite(lon) and 17 <= lat <= 72 and -180 <= lon <= -60):
            raise SystemExit(f"invalid coordinate: {case}")
        if case in seen:
            raise SystemExit(f"duplicate case: {case}")
        seen.add(case)
        fatalities += row[9]
        for field, position in zip(DICT_FIELDS, (3, 4, 5, 12, 13, 14, 15)):
            if not 0 <= row[position] < len(dictionaries[field]):
                raise SystemExit(f"invalid dictionary index: {case} {field}")
    if fatalities != document.get("fatalities_at_valid_locations"):
        raise SystemExit("fatality total mismatch")
    print(json.dumps({
        "verified": str(path), "bytes": len(compressed), "sha256": sha256(path),
        "crashes": len(rows), "fatalities": fatalities,
        "excluded_coordinate_rows": document.get("excluded_coordinate_rows"),
    }, indent=2))


def integer(row: dict[str, str], key: str, default: int = -1) -> int:
    try:
        return int(row[key])
    except (KeyError, TypeError, ValueError):
        return default


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("output", type=Path)
    parser.add_argument("source_zip", type=Path, nargs="?")
    args = parser.parse_args()
    if args.verify_only:
        verify_snapshot(args.output)
        return
    if args.source_zip is None:
        parser.error("source_zip is required when building")

    with zipfile.ZipFile(args.source_zip) as archive:
        source = archive.read(INPUT_MEMBER)
    rows = list(csv.DictReader(io.StringIO(source.decode("utf-8-sig"))))
    required = {"STATE", "STATENAME", "ST_CASE", "COUNTYNAME", "CITYNAME", "MONTH", "DAY", "HOUR", "LATITUDE", "LONGITUD", "FATALS", "PEDS", "PERSONS", *DICT_FIELDS}
    if not rows or not required.issubset(rows[0]):
        raise SystemExit("source columns differ from the Map 72 contract")
    if {integer(row, "YEAR") for row in rows} != {EXPECTED_YEAR}:
        raise SystemExit("source year differs from the Map 72 contract")

    valid: list[dict[str, str]] = []
    for row in rows:
        try:
            lat, lon = float(row["LATITUDE"]), float(row["LONGITUD"])
        except (TypeError, ValueError):
            continue
        if math.isfinite(lat) and math.isfinite(lon) and 17 <= lat <= 72 and -180 <= lon <= -60:
            valid.append(row)
    valid.sort(key=lambda row: integer(row, "ST_CASE"))
    dictionaries = {field: sorted({row[field].strip() or "Unavailable" for row in valid}) for field in DICT_FIELDS}
    indexes = {field: {value: i for i, value in enumerate(values)} for field, values in dictionaries.items()}
    compact = []
    for row in valid:
        compact.append([
            round(float(row["LATITUDE"]), 5), round(float(row["LONGITUD"]), 5), integer(row, "ST_CASE"),
            indexes["STATENAME"][row["STATENAME"].strip() or "Unavailable"],
            indexes["COUNTYNAME"][row["COUNTYNAME"].strip() or "Unavailable"],
            indexes["CITYNAME"][row["CITYNAME"].strip() or "Unavailable"],
            integer(row, "MONTH"), integer(row, "DAY"), integer(row, "HOUR"), integer(row, "FATALS", 0),
            integer(row, "PEDS", 0), integer(row, "PERSONS", 0),
            indexes["HARM_EVNAME"][row["HARM_EVNAME"].strip() or "Unavailable"],
            indexes["RUR_URBNAME"][row["RUR_URBNAME"].strip() or "Unavailable"],
            indexes["LGT_CONDNAME"][row["LGT_CONDNAME"].strip() or "Unavailable"],
            indexes["WEATHERNAME"][row["WEATHERNAME"].strip() or "Unavailable"],
        ])
    payload = {
        "schema": SCHEMA,
        "built_on": "2026-11-08",
        "source_year": EXPECTED_YEAR,
        "source_downloaded": "2026-11-08",
        "source_url": "https://static.nhtsa.gov/nhtsa/downloads/FARS/2024/National/FARS2024NationalCSV.zip",
        "source_zip_sha256": sha256(args.source_zip),
        "source_rows": len(rows),
        "valid_coordinate_crashes": len(compact),
        "excluded_coordinate_rows": len(rows) - len(compact),
        "fatalities_at_valid_locations": sum(row[9] for row in compact),
        "coverage": "50 states and the District of Columbia",
        "columns": ["lat", "lon", "case", "state", "county", "city", "month", "day", "hour", "fatalities", "pedestrians", "persons", "harmful_event", "rural_urban", "light", "weather"],
        "dictionaries": dictionaries,
        "rows": compact,
    }
    raw = canonical_bytes(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    verify_snapshot(args.output)


if __name__ == "__main__":
    main()
