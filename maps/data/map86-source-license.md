# Map 86 source, calculation, and reuse notes

## Scope

Map 86 compares county-level disability-prevalence estimates overall and for people under age 18, ages 18–34, ages 35–64, and age 65 or older from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B18101. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B18101: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b18101.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B18101.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- ACS disability data guidance: `https://www.census.gov/topics/health/disability/guidance/data-collection-acs.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-22. SHA-256 checksums:

- B18101 table: `efd8f4945ac4c4986b9a7b9478b7b831e83cc1430e0ead22b2d1f47eae8d4ec4`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `e79961e48723c1552ba12a40401c102c9cc17ede041522a0ab97776848a1490c`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

Table B18101 divides the civilian noninstitutionalized population by sex, age, and disability status. The build combines the male and female rows and reports people with one or more disabilities divided by the matching age-group population:

- Under age 18: population fields 003, 006, 022 and 025; with-disability fields 004, 007, 023 and 026.
- Ages 18–34: population fields 009 and 028; with-disability fields 010 and 029.
- Ages 35–64: population fields 012 and 031; with-disability fields 013 and 032.
- Age 65 and older: population fields 015, 018, 034 and 037; with-disability fields 016, 019, 035 and 038.
- Overall: the sum of all displayed age-group with-disability counts divided by field 001.

The build verifies every age population equals its with-disability plus no-disability rows, that the age groups partition the full population universe, and that overall with- plus without-disability counts equal that universe. Counts and denominators are retained and percentages are displayed to one decimal place.

`maps/scripts/map86_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are 2020–2024 survey estimates, not diagnoses, medical records, benefit eligibility, service availability, accommodation needs, disability severity, or an individual person's disability status. ACS disability concepts are based on reported difficulty with selected functions and differ by age. County averages hide demographic, household, and neighborhood differences; small age-group denominators can produce unstable percentages. Margins of error are not displayed. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
