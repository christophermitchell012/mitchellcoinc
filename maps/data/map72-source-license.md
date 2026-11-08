# Map 72 source and use notes

## Scope

Map 72 is a dated crash-level view of the 2024 National Highway Traffic Safety Administration Fatality Analysis Reporting System (FARS). FARS is a nationwide census of motor-vehicle traffic crashes on public trafficways in the 50 states, the District of Columbia and Puerto Rico that result in a death within 30 days. The national file used here covers the 50 states and D.C.

This map is not a live crash feed, a count of all crashes or injuries, a road-danger rating, an exposure-adjusted risk model, a causal analysis, a forecast, legal advice, or a substitute for official records. Markers show coded crash locations, not future risk. Overlapping markers and general map scale can hide individual crashes.

## Source

- Publisher: National Highway Traffic Safety Administration, National Center for Statistics and Analysis
- Dataset: Fatality Analysis Reporting System, 2024 National CSV package
- Source page: <https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars>
- Download directory: <https://www.nhtsa.gov/file-downloads?p=nhtsa%2Fdownloads%2FFARS%2F2024%2FNational%2F>
- Downloaded file: <https://static.nhtsa.gov/nhtsa/downloads/FARS/2024/National/FARS2024NationalCSV.zip>
- Download date: 2026-11-08
- ZIP SHA-256: `5112727a8c0dc91ffee27ca05bddb073934f2d192ce4fae997da767dccdbe04f`
- Source member: `FARS2024NationalCSV/accident.csv`
- Source rows: 36,297 crashes

NHTSA states that FARS contains no personal identifying information such as names, addresses or Social Security numbers. NHTSA's terms describe information presented on its website as public information that may be distributed or copied. Attribution to NHTSA and the source year is retained. NHTSA disclaims warranties concerning accuracy, completeness and adequacy.

## Processing and exclusions

`maps/scripts/map72_build_snapshot.py` reads only the crash-level `accident.csv` member, verifies the 2024 year and required columns, and retains rows whose coordinates fall within a broad U.S. extent. It rounds coordinates to five decimal places, dictionary-encodes repeated source labels, sorts by FARS case number, serializes canonical compact JSON and writes deterministic gzip with `mtime=0`.

The snapshot contains 36,127 mapped crash rows and 39,073 fatalities. It excludes 170 rows whose coordinates are reported using NHTSA's unknown or unavailable sentinel values. No missing coordinates, coded circumstances or counts are inferred. The map keeps the source case number, state, county, city, month, day, hour, fatalities, pedestrian fatalities, persons involved, first harmful event, rural/urban code label, lighting and weather label.

- Snapshot: `maps/data/map72-fatal-crashes-2024.json.gz`
- Snapshot SHA-256: `3b2b843105d58bf967c8b0439ce4e14d75a62208fe18f75daccc4408ce863d06`
- Snapshot size: 700,068 bytes
- No authentication, API key, Esri service, runtime NHTSA request, or personal data is used.

## Interpretation limits

FARS is compiled from state records and can include coding, timing and location uncertainty. Fatalities are crash outcomes, not exposure-adjusted rates; high counts can reflect population, travel volume and road use as well as road conditions. A mapped point does not identify fault, legal liability or a single correct intervention. The newest annual files can be revised. The snapshot will not change unless it is deliberately rebuilt and republished.

## Required citations

- National Highway Traffic Safety Administration, Fatality Analysis Reporting System (FARS), 2024 National CSV package.
- OpenStreetMap contributors for the base map.

The snapshot and this explanatory text do not grant rights in third-party names or marks.
