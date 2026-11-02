# Map 66 — Global Childhood Vaccination Coverage

## What is mapped

Map 66 compares the latest available national estimates for three World Development Indicators: DPT three-dose coverage (`SH.IMM.IDPT`), measles first-dose coverage (`SH.IMM.MEAS`), and hepatitis B three-dose coverage (`SH.IMM.HEPB`). The dated snapshot was built on 2026-11-02 from source observations extending through 2024. It contains values for 193 countries or areas; 193 have a Natural Earth geometry. Hepatitis B has 189 latest values.

These are percentage coverage estimates for the age groups defined by each source series. They are not live immunization records, vaccine-effectiveness measures, local appointment availability, individual protection assessments, or medical advice.

## Sources and licence

- WHO and UNICEF produce the coverage estimates using administrative reports, household surveys, potential-bias review, and local expert input.
- World Bank World Development Indicators redistributes the series through its public API and labels each series **Creative Commons Attribution 4.0 (CC BY 4.0)**.
- Country boundaries are from **Natural Earth 1:50m Admin 0 Countries**, public domain.
- Basemap tiles are OpenStreetMap contributors, used under the OpenStreetMap tile policy and attributed on the map.

Source pages:

- https://data.worldbank.org/indicator/SH.IMM.IDPT
- https://data.worldbank.org/indicator/SH.IMM.MEAS
- https://data.worldbank.org/indicator/SH.IMM.HEPB
- https://databank.worldbank.org/metadataglossary/world-development-indicators/series/SH.IMM.IDPT
- https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson

## Snapshot construction and integrity

The browser loads only `map66-childhood-vaccination-latest.json.gz` from the same origin. No API key, authentication, Esri service, browser geolocation, or runtime health-data API is used. `maps/scripts/map66_build_snapshot.py` keeps the most recent finite 0–100 observation for each non-aggregate World Bank country code, rounds boundary coordinates to three decimals, and writes reproducible gzip output (`mtime=0`).

Inputs used for the 2026-11-02 build:

- World Bank country metadata SHA-256: `c9acf3932785191a649cbc04c3056af4cf64a236e5c3b49d49be25ddb0440bce`
- Natural Earth 1:50m country GeoJSON SHA-256: `3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb`
- DPT API response SHA-256: `2bf510ceaadb7bbbac96423efa95682e69ad15962c69f849703114b5730a98d3`
- Measles API response SHA-256: `da19e78d4302b53b8e518dbb22016c3e909f6e6c61d21579e23a07ddc170eede`
- Hepatitis B API response SHA-256: `ac8d059f666c23bffe600b0c704ef53bc0ef429c8eb7cc6be398184a1477f5b0`
- Published gzip SHA-256: `10cdc110585f6d1067a6e17e375020ce8cbc5d057c7827292449212bc34351af`

## Interpretation limits

National values can hide large subnational differences. WHO/UNICEF estimates reconcile multiple evidence streams, but the number of children in the target cohort can be uncertain and administrative and survey sources can disagree. Each popup shows the actual latest source year for the selected series. “No mapped value” means this snapshot has no usable value for that country and series; it does not mean zero vaccination.
