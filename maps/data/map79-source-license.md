# Map 79 source, calculation, and reuse notes

## Scope

Map 79 compares county-level occupied-housing crowding estimates from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B25014. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B25014: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25014.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B25014.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-15. SHA-256 checksums:

- B25014 table: `020e9e669d5a49ce9f59dfff724ef1b13c5b64adc8c0959833cd32b111dcdf49`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `087eb339ec85c8054d3640b0f56bec894bedff9ff12fd07d7c3213c68f37686b`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

The overall denominator is B25014 estimate 001, total occupied housing units. Owner- and renter-specific rates use estimates 002 and 008 respectively. The map aggregates the source categories and displays one decimal place:

- Crowded: estimates 005–007 and 011–013, more than 1 occupant per room
- Severely crowded: estimates 006–007 and 012–013, more than 1.5 occupants per room
- Owner-occupied crowding: estimates 005–007 divided by estimate 002
- Renter-occupied crowding: estimates 011–013 divided by estimate 008

The build verifies that the five owner categories reconcile to estimate 002, the five renter categories reconcile to estimate 008, the tenure totals reconcile to estimate 001, severe crowding does not exceed overall crowding, and owner plus renter crowding equals overall crowding for every retained county.

`maps/scripts/map79_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are survey estimates, not building-code determinations, inspections, vacancy measures, housing-condition ratings, affordability measures, or individual household records. The terms “crowded” and “severely crowded” are analytical labels for more than 1 and more than 1.5 occupants per room; they are not legal findings. County averages hide neighborhood and household differences. Margins of error are not displayed. Generalized cartographic shapes are not legal or parcel boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
