# Map 81 source, calculation, and reuse notes

## Scope

Map 81 compares county-level estimates of when housing structures were built from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B25034. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B25034: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25034.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B25034.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-17. SHA-256 checksums:

- B25034 table: `806d6cb18e8e6c0855e065eca99164b07334cc32f521899aa45a4415ef7d380e`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `96f2c861c9dbcc654f2a1649c0a510ad5ac8a955a28c15224a45a1b6ba8a778a`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

The denominator is B25034 estimate 001, total housing units. The source's mutually exclusive year-built categories are estimates 002–011:

- Built since 2010: estimates 002 and 003
- Built 2000–2009: estimate 004
- Built 1990–1999: estimate 005
- Built 1980–1989: estimate 006
- Built 1970–1979: estimate 007
- Built 1960–1969: estimate 008
- Built before 1960: estimates 009–011
- Built before 1940: estimate 011

The build verifies that estimates 002–011 sum to estimate 001 for every retained county. Counts are retained and percentages are displayed to one decimal place.

`maps/scripts/map81_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are survey estimates, not building inspections, condition or safety ratings, renovation histories, code-compliance findings, lead or asbestos assessments, energy-efficiency measures, or individual property records. The source reports when structures were originally built; it does not establish the age of later additions, roofs, mechanical systems, wiring, plumbing, or other components. County averages hide property and neighborhood differences. Margins of error are not displayed. Generalized cartographic shapes are not legal or parcel boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
