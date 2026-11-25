# Map 89 source, calculation, and reuse notes

## Scope

Map 89 compares county-level median household income estimates and their published margins of error from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B19013. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B19013: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b19013.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B19013.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census income guidance: `https://www.census.gov/topics/income-poverty/income/guidance.html`
- ACS margin-of-error guidance: `https://www.census.gov/programs-surveys/acs/guidance/training-presentations/acs-moe.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were retrieved or checksum-verified on 2026-11-25. SHA-256 checksums:

- B19013 table: `b25a176b0e6c339b6f3a2a0d3d8446bf06f5f080b4395993ec9a8313efb1c229`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `304b5d72b144edcddf9d76bdb3d3928d2240d2a1c3071770666a313df32bfae9`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

Field B19013_001E is median household income in the past 12 months, expressed in 2024 inflation-adjusted dollars. B19013_001M is the published 90% margin of error. The optional uncertainty view calculates relative margin of error as `margin of error / estimate × 100`, rounded to one decimal place. No interpolation, inflation update, cost-of-living adjustment, ranking, or eligibility threshold is applied.

`maps/scripts/map89_build_snapshot.py` performs the join, validates estimates and geometry, verifies the relative-margin calculation, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are 2020–2024 survey estimates, not individual or current income, wages, wealth, disposable income, purchasing power, cost of living, economic mobility, tax records, benefit eligibility, or financial advice. A county median is the midpoint of the estimated household distribution and does not describe every household. County medians hide demographic, neighborhood, and household differences. Comparisons should consider the margin of error. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
