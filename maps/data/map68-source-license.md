# Map 68 — Global Life Expectancy

## What is mapped

Map 68 compares the latest available national estimates for three World Development Indicators: life expectancy at birth for the total population (`SP.DYN.LE00.IN`), females (`SP.DYN.LE00.FE.IN`), and males (`SP.DYN.LE00.MA.IN`). The dated snapshot was built on 2026-11-04 from source observations extending through 2024. All three measures contain values for 217 countries or areas; Natural Earth geometry maps 214 of them. Gibraltar, Kosovo, and the Channel Islands remain in the value table but are not drawn rather than being geocoded or guessed.

Life expectancy at birth indicates how many years a newborn would live if the mortality patterns prevailing at birth remained constant throughout the child's life. It is a period population estimate, not a prediction for an individual.

## Sources and licence

- The World Bank World Development Indicators pages identify the United Nations Population Division's World Population Prospects, national statistical offices, and Eurostat as sources.
- World Bank labels all three indicator pages **Creative Commons Attribution 4.0 (CC BY 4.0)**.
- Country boundaries are from **Natural Earth 1:50m Admin 0 Countries**, public domain.
- Basemap tiles are OpenStreetMap contributors and are attributed on the map.

Source pages:

- https://data.worldbank.org/indicator/SP.DYN.LE00.IN
- https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN
- https://data.worldbank.org/indicator/SP.DYN.LE00.MA.IN
- https://databank.worldbank.org/metadataglossary/world-development-indicators/series/SP.DYN.LE00.IN
- https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson

## Snapshot construction and integrity

The browser loads only `map68-life-expectancy-latest.json.gz` from the same origin. No API key, authentication, Esri service, browser geolocation, or runtime health-data API is used. `maps/scripts/map68_build_snapshot.py` excludes World Bank aggregates, keeps the most recent finite observation from 0 through 120 years for each country code and measure, rounds boundary coordinates to three decimals, and writes reproducible gzip output (`mtime=0`).

Inputs used for the 2026-11-04 build:

- World Bank country metadata SHA-256: `c9acf3932785191a649cbc04c3056af4cf64a236e5c3b49d49be25ddb0440bce`
- Natural Earth 1:50m country GeoJSON SHA-256: `3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb`
- Total indicator API response SHA-256: `bdfcc8fb1e797327e96d86f51d693509bd116ca795219140bc65ece64a0996fa`
- Female indicator API response SHA-256: `04c7f4d32e9714f732df803addb7b663c63086dc4cce32b7dd8bf6bf1d3ab2af`
- Male indicator API response SHA-256: `a0f70df9f092d0630533f7ee068ca7d0b9f32412949024c42cdc38c66233e661`
- Published gzip SHA-256: `abba83fe79768cb1902c296a435956239ea7e1b1b12a5ef637ecf31f9e4abe72`

The World Bank API reported a source update date of 2026-10-08 for all three series. Each popup retains the actual year of the selected country's latest observation.

## Interpretation limits

Life expectancy summarizes a population under a hypothetical continuation of current mortality rates. It does not predict any person's lifespan and is not healthy life expectancy. National averages hide differences by region, income, ethnicity, health access, and other conditions. The World Bank notes that some UN annual series are interpolated from five-year period estimates and therefore may not reflect sudden real events precisely. Values from different statistical systems can also differ in completeness and method. The map is not live surveillance, a health-system ranking, causal analysis, or medical advice.
