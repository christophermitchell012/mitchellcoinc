# Map 77 source, calculation, and reuse notes

## Scope

Map 77 compares county-level household internet-access and subscription estimates from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B28002. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B28002: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b28002.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B28002.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-13. SHA-256 checksums:

- B28002 table: `12446ff0691b8818f5908cdc398817361772c5b3078c506d0409adc9c841840b`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `c62551684ddb3241dc42dfcfc42c38c02aabdefdf4b2b17aad8ac8b2cdf3afb3`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

The denominator is B28002 estimate 001, total households. The map divides each selected source estimate by that county total and displays one decimal place:

- 002: households with an internet subscription
- 004: broadband of any type
- 006: cellular data plan with no other subscription type
- 008: cable, fiber optic, or DSL with no other subscription type
- 010: satellite service with no other subscription type
- 012: internet access without a subscription
- 013: no internet access

The build verifies that estimates 002, 012, and 013 sum exactly to the total for every retained county. Broadband technologies can overlap unless the Census label says “with no other type,” so technology columns are not added together.

`maps/scripts/map77_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are survey estimates, not current service availability, speed, latency, reliability, affordability, provider coverage, outage status, address-level eligibility, device ownership, digital skills, or individual household records. County averages hide neighborhood and household differences. Margins of error are not displayed. Generalized cartographic shapes are not legal, parcel, provider, or service boundaries.

The snapshot makes no runtime Census or Esri request and requires no authentication.
