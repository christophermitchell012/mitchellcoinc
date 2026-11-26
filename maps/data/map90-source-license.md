# Map 90 source, calculation, and reuse notes

## Scope

Map 90 compares county-level median gross rent estimates and their published margins of error from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B25064. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B25064: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25064.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B25064.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census gross-rent definition: `https://www.census.gov/quickfacts/fact/note/US/HSG860223`
- ACS margin-of-error guidance: `https://www.census.gov/programs-surveys/acs/guidance/training-presentations/acs-moe.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were retrieved or checksum-verified on 2026-11-26. SHA-256 checksums:

- B25064 table: `b36e6dc1fcef36b8b307d31b37517b64c80d8b9c70d48c9b1894242860f42eb0`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `6e7536d071748c25add9844650d785a5dc59d8047f2923f4fd2889731fc8b670`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

Field B25064_001E is median gross rent, expressed in 2024 inflation-adjusted dollars. B25064_001M is the published 90% margin of error. Census defines gross rent as contract rent plus the estimated average monthly cost of electricity, gas, water and sewer, and other fuels paid by the renter. The optional uncertainty view calculates relative margin of error as `margin of error / estimate × 100`, rounded to one decimal place. No interpolation, inflation update, rent-burden calculation, ranking, or eligibility threshold is applied.

`maps/scripts/map90_build_snapshot.py` performs the join, validates estimates and geometry, verifies the relative-margin calculation, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are 2020–2024 survey estimates, not current asking rent, a unit listing, affordability, lease terms, housing quality, utility rates, availability, an individual household record, or eligibility. Gross rent excludes owner-occupied housing and does not isolate contract rent from included utility costs. A county median is the midpoint of the estimated renter distribution and does not describe every renter or unit. County medians hide unit, household, and neighborhood differences. Comparisons should consider the margin of error. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or proprietary GIS-service request and requires no authentication.
