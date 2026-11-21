# Map 85 source, calculation, and reuse notes

## Scope

Map 85 compares county-level poverty-status estimates overall and for people under age 18, ages 18–64, and age 65 or older from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B17001. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B17001: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b17001.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B17001.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census poverty-measure guidance: `https://www.census.gov/topics/income-poverty/poverty/guidance/poverty-measures.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-21. SHA-256 checksums:

- B17001 table: `707adda8aaff136382f4fe0858617d09062da48b1a3d2ab2e9a1047def09b531`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `3554588a3334d9e4359d82508e7abb7f16b3bc52da9ff4b406d4e93375e146e5`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

Table B17001 divides the poverty-status universe by status, sex, and age. The overall rate is field 002 divided by field 001. For each displayed age group, the build sums the applicable male and female below-poverty fields, then divides that sum by the below-poverty plus at-or-above-poverty counts for the same ages:

- Under age 18: below-poverty fields 004–009 and 018–023; at-or-above fields 033–038 and 047–052.
- Ages 18–64: below-poverty fields 010–014 and 024–028; at-or-above fields 039–043 and 053–057.
- Age 65 and older: below-poverty fields 015–016 and 029–030; at-or-above fields 044–045 and 058–059.

The build verifies that below-poverty plus at-or-above counts equal the full poverty-status universe and that the three age denominators partition that universe. Counts and denominators are retained and percentages are displayed to one decimal place.

`maps/scripts/map85_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are 2020–2024 survey estimates, not current economic conditions, household income records, benefit eligibility, a cost-of-living measure, or a complete measure of material hardship. Census poverty thresholds vary by family size and composition but not geographically. County averages hide demographic, household, and neighborhood differences; small age-group denominators can produce unstable percentages. Margins of error are not displayed. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
