# Map 74 source and use notes

## Scope

Map 74 is a dated county-level view of the primary home-heating fuel reported for occupied housing units in the U.S. Census Bureau's 2020–2024 American Community Survey (ACS) 5-year estimates. It lets visitors compare the estimated share of occupied units using utility gas, bottled or tank gas, electricity, fuel oil or kerosene, coal or coke, wood, solar energy, another fuel, or no fuel.

The map is not a live utility feed, energy-consumption measure, fuel-price comparison, emissions inventory, heating-system inspection, parcel-level estimate, forecast, causal analysis, household recommendation, eligibility determination, or proof that a fuel is available at an address. County averages hide differences within counties. ACS values are estimates subject to sampling and nonsampling error; margins of error are not displayed.

## Sources

- Publisher: U.S. Census Bureau
- Survey: 2024 ACS 5-Year Estimates, covering 2020–2024
- Table: B25040, House Heating Fuel
- Summary-file directory: <https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/>
- ACS release page: <https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release.html>
- Boundaries: 2024 Census cartographic boundary file, counties, 1:20,000,000
- Boundary page: <https://www.census.gov/geographies/mapping-files/2024/geo/carto-boundary-file.html>
- Download date: 2026-11-10
- B25040 SHA-256: `470470c2520a27748bd358527abd0088c5a252d541cd73a6112b6f914d4442d2`
- County boundary ZIP SHA-256: `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`

The Census Bureau's public data are produced by the U.S. government and may be used with attribution. The Census Bureau name is not used to imply endorsement. No respondent-level data is used or exposed.

## Processing

`maps/scripts/map74_build_snapshot.py` reads the official pipe-delimited B25040 summary-file table, retains county geography records, and joins them to the official generalized county boundary file by five-digit GEOID. For every fuel category, it divides the corresponding occupied-housing-unit estimate by B25040's total occupied housing units. Percentages are rounded to one decimal place; source counts are retained. No missing value is inferred.

The script uses only the Python standard library, parses the Polygon shapefile and DBF directly, preserves Polygon and MultiPolygon geometry, rounds boundary coordinates to five decimal places, sorts counties by GEOID, serializes canonical compact JSON, and writes deterministic gzip with `mtime=0`.

- Snapshot: `maps/data/map74-home-heating-fuel-2024.json.gz`
- Snapshot SHA-256: `543c247481057bae0eddc8e7333e8509c4eda50446b3003e8d1d00ee5f827e8c`
- Snapshot size: 543,211 bytes
- Coverage: 3,222 counties or county equivalents in the 50 states, District of Columbia, and Puerto Rico
- No authentication, API key, Esri service, runtime Census request, or respondent-level data is used.

## Interpretation limits

The source asks for the fuel used most to heat the housing unit; it does not report every backup fuel, equipment type, delivered energy, cost, efficiency, reliability, indoor temperature, outage exposure, or emissions. “Solar energy” is a source response category and is not a count of rooftop solar installations. “No fuel used” does not establish that a unit is uninhabitable or lacks all energy service. Small estimates can have large relative margins of error. Generalized boundaries are for national display and are not legal boundaries, parcel lines, utility territories, service areas, or precise local geography.

## Required citations

- U.S. Census Bureau, 2020–2024 American Community Survey 5-Year Estimates, table B25040.
- U.S. Census Bureau, 2024 Cartographic Boundary Files, counties, 1:20,000,000.
- OpenStreetMap contributors for the base map.
