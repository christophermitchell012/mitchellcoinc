# Map 80 source, calculation, and reuse notes

## Scope

Map 80 compares county-level housing vacancy rates and vacancy-status categories from the U.S. Census Bureau's 2020–2024 American Community Survey five-year tables B25002 and B25004. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B25002: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25002.dat`
- ACS table B25004: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25004.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B25002.json` and `https://api.census.gov/data/2024/acs/acs5/groups/B25004.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-16. SHA-256 checksums:

- B25002 table: `eb98debfe8e8533e9a8e647a8c5dca5dbe11401c4de4e4449b4a2ba7dc75620f`
- B25004 table: `cbc82f087ece808cf269ce8e9eb1c3227c28d82206726339a9a34dda8398ec49`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- B25002 definitions: `7203086ab854865dab956d9efa0f5b9e83d3a91db99eb311b2772c1c299b97e1`
- B25004 definitions: `bc6e63dab202188cda6e465b85a24b20beebf38cef6daec23cfddc05512d866a`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

The overall vacancy-rate denominator is B25002 estimate 001, total housing units; its numerator is estimate 003, vacant housing units. Vacancy-type shares use B25004 estimate 001, total vacant housing units, as their denominator:

- For rent: estimate 002
- Rented, not occupied: estimate 003
- For sale only: estimate 004
- Sold, not occupied: estimate 005
- For seasonal, recreational, or occasional use: estimate 006
- For migrant workers: estimate 007
- Other vacant: estimate 008

The build verifies that occupied plus vacant units reconcile to B25002 estimate 001, B25004 estimate 001 equals the B25002 vacant count, and the seven vacancy-status categories sum to the vacant total for every retained county. Percentages are displayed to one decimal place.

`maps/scripts/map80_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are survey estimates, not live rental or sale listings, evidence a unit is available or habitable, price or affordability measures, building inspections, code-status or abandonment findings, or individual property records. Vacancy reasons reflect Census survey categories and may include seasonal and occasional-use units. County averages hide property and neighborhood differences. Margins of error are not displayed. Generalized cartographic shapes are not legal or parcel boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
