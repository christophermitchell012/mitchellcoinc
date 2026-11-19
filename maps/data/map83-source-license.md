# Map 83 source, calculation, and reuse notes

## Scope

Map 83 compares county-level estimates of occupied housing units lacking complete kitchen facilities from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B25053. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B25053: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25053.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B25053.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-19. SHA-256 checksums:

- B25053 table: `07bf53826e067db1e472849719f7f8dd7a49838374f8c8e0d847e6c12b7d416c`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `f062ee20550ad19378f91f617abf953a39c3b648f1023dd975e12fb4033f2c74`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

The source fields are total occupied housing units (001), owner occupied (002), owner occupied with complete kitchen facilities (003), owner occupied lacking complete kitchen facilities (004), renter occupied (005), renter occupied with complete kitchen facilities (006), and renter occupied lacking complete kitchen facilities (007).

The map reports:

- All occupied units lacking complete kitchen facilities: (004 + 007) / 001
- Owner-occupied units lacking complete kitchen facilities: 004 / 002
- Renter-occupied units lacking complete kitchen facilities: 007 / 005

The build verifies that owner plus renter totals equal the overall total and that complete plus lacking counts equal each tenure total. Counts and denominators are retained and percentages are displayed to one decimal place.

`maps/scripts/map83_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are survey estimates, not property inspections or measures of food access, nutrition, appliance condition, affordability, needed repairs, habitability, code compliance, or individual eligibility. “Lacking complete kitchen facilities” is a Census category. County averages hide property, household, and neighborhood differences; small denominators can produce unstable percentages. Margins of error are not displayed. Generalized cartographic shapes are not legal or parcel boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
