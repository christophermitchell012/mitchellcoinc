# Map 84 source, calculation, and reuse notes

## Scope

Map 84 compares county-level labor-force participation, employment-to-population, and unemployment estimates from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B23025. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B23025: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b23025.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B23025.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-20. SHA-256 checksums:

- B23025 table: `264a5bd9367c5f58d9773fa4966fa94fe1e02f9c7106bc2ab39168d6de7c3e4a`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `0d8397bf28777cfe02323d8c20856178f36efe34eb0a1f8e9fe440ece20a4bd0`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

The source fields are population age 16 and older (001), in the labor force (002), civilian labor force (003), employed (004), unemployed (005), armed forces (006), and not in the labor force (007).

The map reports:

- Labor-force participation rate: 002 / 001
- Employment-to-population ratio: 004 / 001
- Unemployment rate: 005 / 003

The build verifies that labor-force plus not-in-labor-force counts equal the population age 16 and older, civilian labor force plus armed forces equals the labor force, and employed plus unemployed equals the civilian labor force. Counts and denominators are retained and percentages are displayed to one decimal place.

`maps/scripts/map84_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are 2020–2024 survey estimates, not current monthly labor statistics, job openings, wages, job quality, underemployment, discouraged-worker counts, benefit eligibility, or individual employment records. ACS definitions and reference periods differ from the monthly Current Population Survey and Local Area Unemployment Statistics. County averages hide demographic, household, and neighborhood differences; small denominators can produce unstable percentages. Margins of error are not displayed. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
