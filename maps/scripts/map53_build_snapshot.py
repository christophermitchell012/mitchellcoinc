#!/usr/bin/env python3
"""Build Map 53's bounded beach-location snapshot from EPA's GeoPackage."""

import argparse
import gzip
import hashlib
import json
import sqlite3
from pathlib import Path

SOURCE_URL = "https://dmap-data-commons-ow.s3.amazonaws.com/data/beach/geospatial/beach_20240228_gpkg.zip"
ARCHIVE_SHA256 = "c0f0475706bf5895f81080604a1a3f2b588a7abd54b245d45b05d02910a16bc1"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("gpkg", type=Path, help="extracted beach_20240229.gpkg")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    digest = hashlib.sha256(args.gpkg.read_bytes()).hexdigest()
    if digest != "8fe250cd76c6f389113502c297a3a40da76d19033a292ff89ae9d76e1d557f91":
        raise SystemExit(f"unexpected GeoPackage SHA-256: {digest}")
    db = sqlite3.connect(args.gpkg)
    rows = db.execute("""
        SELECT beach_id, beach_name, beach_county, beach_state,
               historical_id_flag, beach_len_in_mi, latest_beach_year,
               beach_access, owner_access, start_latitude_measure,
               start_longitude_measure
          FROM beach_attr
         ORDER BY beach_state, beach_county, beach_name, beach_id
    """).fetchall()
    beaches = []
    skipped = 0
    for beach_id, name, county, state, historical, miles, year, access, owner, lat, lon in rows:
        if lat is None or lon is None or not (-90 <= lat <= 90 and -180 <= lon <= 180):
            skipped += 1
            continue
        beaches.append({
            "id": beach_id,
            "name": name,
            "county": county,
            "state": state,
            "historical": historical == "Y",
            "miles": round(miles, 4) if miles is not None else None,
            "latest_year": int(year) if year is not None else None,
            "access": access,
            "owner_access": owner,
            "lat": round(lat, 6),
            "lon": round(lon, 6),
        })
    payload = {
        "source": "U.S. EPA WATERS BEACH Program geospatial download",
        "source_url": SOURCE_URL,
        "download_page": "https://www.epa.gov/waterdata/waters-geospatial-data-downloads",
        "download_page_extract_label": "April 28, 2024",
        "archive_member": "beach_20240229.gpkg",
        "archive_sha256": ARCHIVE_SHA256,
        "built_utc": "2026-10-21T15:01:52Z",
        "beach_count": len(beaches),
        "skipped_invalid_coordinates": skipped,
        "beaches": beaches,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    args.output.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    print(f"wrote {len(beaches):,} beaches; skipped {skipped}")


if __name__ == "__main__":
    main()
