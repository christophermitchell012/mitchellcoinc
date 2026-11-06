# Map 70 source and use notes

## Scope

Map 70 is a dated country-level comparison of electricity-generation shares and territorial fossil-and-industrial CO₂ emissions per person. It is not a live grid monitor, household-energy estimate, consumption-based carbon footprint, project siting tool, forecast, target tracker, causal model, policy scorecard, or proof of electricity access or reliability.

## Electricity mix

- Chart: [Share of electricity generation from fossil fuels, renewables and nuclear](https://ourworldindata.org/grapher/electricity-fossil-renewables-nuclear-line)
- Downloaded: 2026-11-05
- Source metadata last updated: 2026-06-30
- Source range: 1900–2025; the map retains each ISO3 country's latest complete three-share row.
- Attribution: Ember (2026); Energy Institute — Statistical Review of World Energy (2026); Pinto et al. (2023); UK Department for Energy Security and Net Zero (2023), with major processing by Our World in Data.
- Definitions: fossil fuels are coal, oil and gas. Renewables include solar, wind, hydropower, bioenergy, geothermal, wave and tidal generation. The measure is share of electricity generation, not total primary energy.
- Licence: Ember states that its electricity data are CC BY 4.0. Our World in Data labels the processed chart CC BY and requires attribution to OWID and underlying providers.
- Source CSV SHA-256: `5710f15c4d2acace782cbb6b5c8b40567182aa5dd9407137aded4a697ffceccf`

## CO₂ emissions per person

- Chart: [CO₂ emissions per capita](https://ourworldindata.org/grapher/co-emissions-per-capita)
- Downloaded: 2026-11-05
- Source metadata last updated: 2025-11-13
- Source range: 1750–2024; the map retains each ISO3 country's latest finite nonnegative row.
- Attribution: Global Carbon Budget (2025) and population based on various sources (2024), with major processing by Our World in Data.
- Definition: territorial CO₂ from fossil-fuel combustion and industrial processes, divided by population. Land-use change, emissions embedded in imported goods, and country attribution for international aviation and shipping are excluded.
- Licence: the Global Carbon Budget material and Our World in Data processing are published under CC BY 4.0, with attribution required.
- Source CSV SHA-256: `11a3a3531e4d814f96c5b6ce1ce4888be554cab5a48fe1394ba72f1b590e976e`

## Boundaries and build

The snapshot reuses the Natural Earth country geometries already stored in the Map 68 dated snapshot. Boundaries are generalized orientation geometry and do not imply a position on disputed borders or sovereignty. The Map 68 boundary snapshot SHA-256 was `abba83fe79768cb1902c296a435956239ea7e1b1b12a5ef637ecf31f9e4abe72`.

`maps/scripts/map70_build_snapshot.py` validates ISO3 codes, finite values, percentage ranges and a 99–101% electricity-share total. It keeps the latest valid row independently for electricity mix and emissions, rounds display values, sorts keys, rounds no additional geometry, serializes compact JSON, and writes deterministic gzip with `mtime=0`.

The resulting same-origin snapshot contains electricity-mix values for 207 ISO3 areas and emissions values for 213. Natural Earth geometry maps 199 electricity areas and 204 emissions areas. Missing geometry and missing values are not inferred.

- Snapshot: `maps/data/map70-energy-mix-emissions-latest.json.gz`
- Snapshot SHA-256: `c83322d5d546914c386955f7899b24a4da71a3bcf5eb3d76ea711e9a83fa8ac6`
- Snapshot size: 534,057 bytes
- No authentication, API key, Esri service, runtime third-party data request, or user data is used.

## Required citations

- Ember (2026) and other sources, with major processing by Our World in Data. “Share of electricity generation from fossil fuels, renewables and nuclear.”
- Global Carbon Budget (2025); Population based on various sources (2024), with major processing by Our World in Data. “CO₂ emissions per capita.”
- Natural Earth, public-domain boundary data.

The snapshot and this explanatory text do not grant rights in third-party names or marks.
