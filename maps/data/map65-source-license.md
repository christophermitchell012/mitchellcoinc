# Map 65 source and use notes

## Source contract

Map 65 presents under-five mortality estimates from the United Nations Inter-agency Group for Child Mortality Estimation (UN IGME), distributed through the World Bank World Development Indicators API. The three indicators are the overall (`SH.DYN.MORT`), female (`SH.DYN.MORT.FE`) and male (`SH.DYN.MORT.MA`) probabilities per 1,000 live births that a newborn would die before age five if subject to the age-specific mortality rates of the indicated year.

The same-origin snapshot was retrieved anonymously on November 1, 2026. The API reported an October 8, 2026 update and supplied estimates through 2024. The build retains each country's latest finite nonnegative observation and excludes World Bank regional and income aggregates. Every popup displays the actual year for the selected measure. Generalized Natural Earth polygons are reference geometry only. No value, year, boundary or missing country is inferred.

## Provenance and integrity

- World Bank overall series and source attribution: https://data.worldbank.org/indicator/SH.DYN.MORT
- World Bank female series: https://data.worldbank.org/indicator/SH.DYN.MORT.FE
- World Bank male series: https://data.worldbank.org/indicator/SH.DYN.MORT.MA
- World Bank metadata, definition, methods and licence: https://databank.worldbank.org/metadataglossary/world-development-indicators/series/SH.DYN.MORT
- UN IGME: https://childmortality.org/
- Natural Earth country geometry: https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson
- Overall API JSON SHA-256: `af5560ae5b5a66fb0228a149f1d1ea90f121701b22c94d2ff42adc78ca0e7097`
- Female API JSON SHA-256: `1c8dd93ac44ad3dfa7e626b454d358f1937d00bc7f449744753cb8df0ab225f9`
- Male API JSON SHA-256: `78c046778108790edf3748bea648df6682e82c2da49babeb98c4dd2a8d33de1f`
- World Bank country-metadata JSON SHA-256: `c9acf3932785191a649cbc04c3056af4cf64a236e5c3b49d49be25ddb0440bce`
- Natural Earth GeoJSON SHA-256: `3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb`
- Normalized compressed snapshot SHA-256: `9e2391e6b709b55bdf8674fc3859017575cdfb38f182a9320e5b26c73e041030`
- Rebuild script: `maps/scripts/map65_build_snapshot.py`

## Rights and attribution

The World Bank indicator pages and metadata identify UN IGME—UNICEF, WHO, World Bank and the UN Population Division—as the source and label these series Creative Commons Attribution 4.0. Natural Earth vector data is public domain. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain OpenStreetMap attribution.

Suggested attribution: United Nations Inter-agency Group for Child Mortality Estimation, via World Bank World Development Indicators. 2026. Under-five mortality rate. Accessed 1 November 2026. Licence: CC BY 4.0.

## Runtime behavior

The browser downloads one same-origin deterministically compressed JSON snapshot. It makes no authenticated or live data request. Measure and country-search controls only filter the stored observations and reference geometry.

## Limits

These are national modeled estimates, not counts of deaths, live surveillance, local clinical data, individual risk predictions, causal explanations, health-care quality ratings or medical advice. Survey data can have recall and sampling error; indirect estimates and extrapolations can be uncertain where source data are sparse or old. Values are probabilities expressed per 1,000 live births, not percentages. National averages hide subnational and socioeconomic disparities. The female and male series should not be interpreted as proof of discrimination or a causal mechanism. Boundaries are generalized reference geometry and do not imply endorsement or settled jurisdiction.
