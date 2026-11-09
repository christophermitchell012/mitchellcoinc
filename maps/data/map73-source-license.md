# Map 73 source and use notes

## Scope

Map 73 is a dated county-level view of housing-cost burden derived from the U.S. Census Bureau's 2020–2024 American Community Survey (ACS) 5-year estimates. It reports the estimated share of renter households, owners with a mortgage, and owners without a mortgage whose reported housing costs are 30 percent or more of household income. The denominator for each measure excludes units for which the source table cannot compute the cost-to-income ratio.

The map is not a live housing-market feed, a rent listing service, a measure of homelessness or eviction, a parcel-level estimate, a forecast, a causal analysis, a county ranking, eligibility guidance, or financial advice. County averages hide differences within counties. ACS values are estimates subject to sampling and nonsampling error; the map does not display margins of error.

## Sources

- Publisher: U.S. Census Bureau
- Survey: 2024 ACS 5-Year Estimates, covering 2020–2024
- Tables: B25070, Gross Rent as a Percentage of Household Income in the Past 12 Months; B25091, Mortgage Status by Selected Monthly Owner Costs as a Percentage of Household Income in the Past 12 Months
- Summary-file directory: <https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/>
- ACS release page: <https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html>
- Boundaries: 2024 Census cartographic boundary file, counties, 1:20,000,000
- Boundary page: <https://www.census.gov/geographies/mapping-files/2024/geo/carto-boundary-file.html>
- Download date: 2026-11-09
- B25070 SHA-256: `862ccc17d913305d11e6f802ce4518d76b30585ea0b05b251cd8cf21f8661386`
- B25091 SHA-256: `152e35f7a5143f3e0a27b58b1ec9c142346d975904964b0cab8990c0ddef5f14`
- County boundary ZIP SHA-256: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`

The Census Bureau permits use of its API and public data for display and analysis, asks users to cite it as the original source, and states that conclusions from analysis are the performing party's responsibility. The Census Bureau name is not used to imply endorsement. No respondent-level data is used or exposed.

## Processing

`maps/scripts/map73_build_snapshot.py` reads the official pipe-delimited summary-file tables, retains county geography records, and joins them to the official generalized county boundary file by five-digit GEOID. For renters, it divides the sum of B25070 categories at 30 percent or more by the table total less the not-computed count. For mortgaged and mortgage-free owners, it applies the same calculation to the corresponding B25091 categories. Percentages are rounded to one decimal place.

The script uses only the Python standard library, parses the Polygon shapefile and DBF directly, preserves Polygon and MultiPolygon geometry, rounds boundary coordinates to five decimal places, sorts counties by GEOID, serializes canonical compact JSON, and writes deterministic gzip with `mtime=0`.

- Snapshot: `maps/data/map73-housing-cost-burden-2024.json.gz`
- Snapshot SHA-256: `72ebe83f1576a1bcc43a636c8e963abe8e2e844e78e0650ef12c08235d551546`
- Snapshot size: 439,656 bytes
- Coverage: 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico
- No authentication, API key, Esri service, runtime Census request, or respondent-level data is used.

## Interpretation limits

The 30-percent threshold is a descriptive cost-to-income convention, not a determination that every household above it faces the same hardship or that every household below it can comfortably afford housing. A value can be volatile where the estimated denominator is small. Table counts and their derived shares can change in later ACS releases or revisions. The generalized boundaries are for national display and are not legal boundaries, parcel lines, service areas, or precise local geography.

## Required citations

- U.S. Census Bureau, 2020–2024 American Community Survey 5-Year Estimates, tables B25070 and B25091.
- U.S. Census Bureau, 2024 Cartographic Boundary Files, counties, 1:20,000,000.
- OpenStreetMap contributors for the base map.
