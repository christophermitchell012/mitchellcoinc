# Map 88 source, calculation, and reuse notes

## Scope

Map 88 compares county-level estimates of language spoken at home and English proficiency for people age 5 and older from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table C16001. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table C16001: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-c16001.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/C16001.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census language-use guidance: `https://www.census.gov/topics/population/language-use.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were downloaded on 2026-11-24. SHA-256 checksums:

- C16001 table: `dae7f251470e964510ce46eedb520b5609835a8244190a530638e022ecd1a84e`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `082f0be108480f5b6a95cf0e645dda6f05dca42766535f6b9c1c2a39c90a15a4`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Source feasibility decision

The more detailed B16001 downloadable file was tested first but contains no county rows in the 2024 table-based summary release. An unauthenticated county-wide Census API request returned a `Missing Key` response. Map 88 therefore uses the official, county-compatible collapsed table C16001. This preserves zero-auth runtime and publication architecture while avoiding unsupported county coverage claims.

## Calculation

Table C16001 partitions the population age 5 and older by language spoken at home and, for every non-English category, whether the person speaks English “very well” or less than “very well.” Display measures are:

- Language other than English at home: category totals 003, 006, 009, 012, 015, 018, 021, 024, 027, 030, 033 and 036.
- Speak English less than “very well”: fields 005, 008, 011, 014, 017, 020, 023, 026, 029, 032, 035 and 038.
- Spanish at home: field 003.
- Other Indo-European languages: fields 006, 009, 012 and 015.
- Asian and Pacific Island languages: fields 018, 021, 024, 027 and 030.
- Other language groups: fields 033 and 036.

Each count is divided by field 001, the population age 5 and older. The build verifies that English-only plus all non-English categories partition the table universe, and that the four broad language groups partition the non-English total. Counts and denominators are retained; percentages are displayed to one decimal place.

`maps/scripts/map88_build_snapshot.py` performs the join, validates counts and geometry, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are 2020–2024 survey estimates, not immigration status, citizenship, literacy, disability, education, translation need, language preference, an individual ability assessment, or an eligibility determination. “Less than very well” is the Census survey response category; it does not measure every dimension of communication or proficiency. The broad groups combine many languages and do not enumerate all communities. County averages hide demographic, neighborhood, and household differences. Margins of error are not displayed. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or third-party GIS-service request and requires no authentication.
