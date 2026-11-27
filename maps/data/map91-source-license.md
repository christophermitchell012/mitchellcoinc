# Map 91 source, calculation, and reuse notes

## Scope

Map 91 compares county-level median owner-occupied home value estimates and their published margins of error from the U.S. Census Bureau's 2020–2024 American Community Survey five-year table B25077. The dated same-origin snapshot contains 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico.

## Official source files

- ACS table B25077: `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25077.dat`
- 2024 county cartographic boundaries, 1:20,000,000: `https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_20m.zip`
- Table-variable definitions: `https://api.census.gov/data/2024/acs/acs5/groups/B25077.json`
- ACS data release: `https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html`
- Census housing guidance: `https://www.census.gov/topics/housing/housing-patterns/guidance.html`
- ACS margin-of-error guidance: `https://www.census.gov/programs-surveys/acs/guidance/training-presentations/acs-moe.html`
- Census data terms: `https://www.census.gov/data/developers/about/terms-of-service.html`

Files were retrieved or checksum-verified on 2026-11-27. SHA-256 checksums:

- B25077 table: `89eb2153764a2330b23959d8bbc29b3a8f3016f087b990f2a8ea0d5096d9a816`
- Boundary ZIP: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`
- Variable definitions: `892740d42c4a6c7120999f9302c18550508c964082f66eddc75865200f32fd0c`

U.S. Census Bureau data are public-domain U.S. government works. OpenStreetMap basemap tiles are credited on the map and remain subject to OpenStreetMap's copyright and Open Database License terms.

## Calculation

Field B25077_001E is median value in dollars for owner-occupied housing units. B25077_001M is the published 90% margin of error. Census value is the respondent's estimate of how much the property would sell for if it were for sale. The optional uncertainty view calculates relative margin of error as `margin of error / estimate × 100`, rounded to one decimal place. No appraisal, inflation adjustment, interpolation, ranking, equity estimate, affordability calculation, or eligibility threshold is applied.

`maps/scripts/map91_build_snapshot.py` performs the join, validates estimates and geometry, verifies the relative-margin calculation, rounds coordinates to five decimals, emits canonical JSON, and creates deterministic gzip bytes with `mtime=0`.

## Limits

These are 2020–2024 survey estimates, not appraisals, current asking or sale prices, tax assessments, equity, mortgage balances, affordability, housing condition, an individual property record, or financial advice. The universe is owner-occupied housing units, excluding renter-occupied and vacant units. A county median is the midpoint of the estimated distribution and does not describe every property. County medians hide property and neighborhood differences. Comparisons should consider the margin of error. Generalized cartographic shapes are not legal boundaries.

The snapshot makes no runtime government-data or proprietary GIS-service request and requires no authentication.
