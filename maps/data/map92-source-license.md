# Map 92 source, calculation, and reuse notes

## Scope

Map 92 compares county-level Gini index estimates and their published margins of error from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B19083. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B19083: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b19083.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B19083.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census Gini-index guidance: `https://www.census.gov/topics/income-poverty/income-inequality/about/metrics/gini-index.html`
- ACS margin-of-error guidance: `https://www.census.gov/programs-surveys/acs/guidance/training-presentations/acs-moe.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

The B19083 table and variable definitions were retrieved on 2026-11-28. The boundary file checksum was verified for Map 91 on 2026-11-27, and Map 92 reuses that unchanged normalized geometry. SHA-256 checksums:

- B19083 table: `338f7a1191eaaf3913913e78c36aaa9d82f2b5c8faaf889be2e597b28869205e`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `fa7b3875438e93d3a18f8fe8f61c0a39c3056daf3664deb91a02c52926fb6c56`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

Field B19083_001E is the Gini index of household-income inequality. It ranges from 0, perfect equality, to 1, perfect inequality. B19083_001M is the published 90% margin of error. The optional uncertainty view calculates relative margin of error as `margin of error / estimate × 100`, rounded to one decimal place. No ranking, interpolation, imputation, wealth estimate, income conversion, threshold label, or eligibility calculation is applied.

`maps/scripts/map92_build_snapshot.py` joins B19083 to the same official 2024 generalized county geometry verified for Map 91, validates estimates and geometry, verifies the relative-margin calculation, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

The Gini index summarizes the distribution of household income. It does not measure wealth, poverty, median income, purchasing power, cost of living, mobility, quality of life, or the income of an individual household. A county index hides differences among people, neighborhoods, household types, and income sources. Values are survey estimates and comparisons should consider the margin of error. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or proprietary GIS-service request and requires no authentication.
