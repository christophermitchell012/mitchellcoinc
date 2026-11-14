# Map 78 source, calculation, and reuse notes

## Scope

Map 78 compares county-level estimates of vehicles available to households from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B08201. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B08201: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b08201.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B08201.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-14. SHA-256 checksums:

- B08201 table: `2f64e698223ba83f97b67dde4a34961a02f230e0359ffc69b9657b89a3df6b4d`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `24ce57c5e3cdc294dc0c3f4fb54cb857173906d67827b35a87ddc082ab8da957`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

The denominator is B08201 estimate 001, total households. The map divides each selected source estimate by that county total and displays one decimal place:

- 002: no vehicle available
- 003: one vehicle available
- 004: two vehicles available
- 005: three vehicles available
- 006: four or more vehicles available

The build verifies that estimates 002 through 006 are nonnegative and sum exactly to the total for every retained county. These five mutually exclusive categories cover all households in the table universe.

`maps/scripts/map78_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are survey estimates, not vehicle registrations or a measure of ownership, condition, affordability, trip access, transit quality, mobility need, or individual household records. “Available” follows the Census questionnaire concept and does not establish who owns or regularly uses a vehicle. County averages hide neighborhood and household differences. Margins of error are not displayed. Generalized cartographic shapes are not legal or parcel boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
