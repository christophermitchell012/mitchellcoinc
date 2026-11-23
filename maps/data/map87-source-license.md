# Map 87 source, calculation, and reuse notes

## Scope

Map 87 compares county-level educational-attainment estimates for adults age 25 and older from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B15003. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B15003: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b15003.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B15003.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census educational-attainment guidance: `https://www.census.gov/topics/education/educational-attainment.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-23. SHA-256 checksums:

- B15003 table: `d0c8609e958022459215c8a31d7452ef7528ee8dd70fbb6f9a99de0f491f42d7`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `314b11a7841dfcd003364789ded2db734e9d47679f7a200964e9caefd4c625c6`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

Table B15003 partitions the population age 25 and older into detailed attainment categories. The build combines those source rows into four mutually exclusive display groups:

- No high school diploma: fields 002–016.
- High school diploma or equivalent: fields 017–018.
- Some college or associate degree: fields 019–021.
- Bachelor's degree or higher: fields 022–025.

Each group is divided by field 001, the population age 25 and older. The build verifies that the four groups partition the full table universe. Counts and denominators are retained and percentages are displayed to one decimal place.

`maps/scripts/map87_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are 2020–2024 survey estimates, not school-performance data, education quality, literacy, current enrollment, workforce skill, credential validity, an individual education record, or an eligibility determination. Educational attainment describes completed education reported for adults age 25 and older and does not explain causes. County averages hide demographic, neighborhood, and household differences. Margins of error are not displayed. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
