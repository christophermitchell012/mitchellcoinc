#!/usr/bin/env python3
"""Build Map 39's compact EPA SEMS NPL-site snapshot.

The source service is anonymous and keyless, but the national result is stored
same-origin so the published map does not fan out to a slow cross-origin API.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "map39-superfund-npl-sites.json"
BASE = "https://data.epa.gov/efservice/sems.envirofacts_site"
STATUS_CODES = ("F", "P", "D")


def fetch_status(code):
    url = f"{BASE}/npl_status_code/equals/{code}/1:2500/json"
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "MitchellCo Map 39 snapshot builder; https://mitchellcoinc.com/maps/",
        },
    )
    with urlopen(request, timeout=180) as response:
        if response.status != 200:
            raise RuntimeError(f"EPA returned HTTP {response.status}: {url}")
        return url, json.load(response)


def clean(row):
    lat = row.get("primary_latitude_decimal_val")
    lon = row.get("primary_longitude_decimal_val")
    if lat in (None, "") or lon in (None, ""):
        return None
    lat, lon = float(lat), float(lon)
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        return None
    return {
        "id": row.get("epa_id") or row.get("site_id"),
        "name": row.get("name"),
        "status_code": row.get("npl_status_code"),
        "status": row.get("npl_status_name"),
        "state": row.get("fk_ref_state_code"),
        "city": row.get("city_name"),
        "county": row.get("county_name"),
        "lat": lat,
        "lon": lon,
        "federal": row.get("federal_facility_ind") == "Y",
    }


def main():
    source_urls, records, raw_counts = [], [], {}
    for code in STATUS_CODES:
        url, rows = fetch_status(code)
        source_urls.append(url)
        raw_counts[code] = len(rows)
        records.extend(site for row in rows if (site := clean(row)))
    records.sort(key=lambda site: (site["status_code"], site["state"] or "", site["name"] or "", site["id"] or ""))
    payload = {
        "schema_version": 1,
        "retrieved_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source": "U.S. EPA Envirofacts SEMS envirofacts_site",
        "source_urls": source_urls,
        "status_codes": {"F": "Final NPL", "P": "Proposed NPL", "D": "Deleted from NPL"},
        "raw_counts": raw_counts,
        "records_with_coordinates": len(records),
        "records": records,
    }
    OUT.write_text(json.dumps(payload, separators=(",", ":")) + "\n")
    print(f"Wrote {OUT}: {len(records)} mapped records from {sum(raw_counts.values())} source rows")


if __name__ == "__main__":
    main()
