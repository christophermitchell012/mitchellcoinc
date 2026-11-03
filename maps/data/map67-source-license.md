# Map 67 — Global Maternal Mortality

## What is mapped

Map 67 compares the latest available national estimates for three World Development Indicators: maternal mortality ratio (`SH.STA.MMRT`), lifetime risk of maternal death as a percentage (`SH.MMR.RISK.ZS`), and estimated maternal deaths (`SH.MMR.DTHS`). The dated snapshot was built on 2026-11-03 from source observations extending through 2023. All three measures contain values and Natural Earth geometry for 194 countries or areas.

The mortality ratio represents modeled maternal deaths per 100,000 live births. Lifetime risk estimates the probability that a 15-year-old woman will eventually die from a maternal cause, accounting for both maternal mortality and fertility. The death count is an estimated annual total and is strongly affected by population and birth volume.

## Sources and licence

- The Maternal Mortality Estimation Inter-Agency Group includes the World Health Organization, UNICEF, UNFPA and World Bank.
- World Bank World Development Indicators redistributes the three series through its public API and labels them **Creative Commons Attribution 4.0 (CC BY 4.0)**.
- Country boundaries are from **Natural Earth 1:50m Admin 0 Countries**, public domain.
- Basemap tiles are OpenStreetMap contributors and are attributed on the map.

Source pages:

- https://data.worldbank.org/indicator/SH.STA.MMRT
- https://data.worldbank.org/indicator/SH.MMR.RISK.ZS
- https://data.worldbank.org/indicator/SH.MMR.DTHS
- https://databank.worldbank.org/metadataglossary/world-development-indicators/series/SH.STA.MMRT
- https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson

## Snapshot construction and integrity

The browser loads only `map67-maternal-mortality-latest.json.gz` from the same origin. No API key, authentication, Esri service, browser geolocation, or runtime health-data API is used. `maps/scripts/map67_build_snapshot.py` keeps the most recent finite nonnegative observation for each non-aggregate World Bank country code, rounds boundary coordinates to three decimals, and writes reproducible gzip output (`mtime=0`).

Inputs used for the 2026-11-03 build:

- World Bank country metadata SHA-256: `c9acf3932785191a649cbc04c3056af4cf64a236e5c3b49d49be25ddb0440bce`
- Natural Earth 1:50m country GeoJSON SHA-256: `3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb`
- Mortality-ratio API response SHA-256: `199a44f1c394842ee7ffc8f64179f35eefcea63ae19f7f6a3d85306cf01119aa`
- Lifetime-risk API response SHA-256: `490bf799fd93dbeabd53d9dced5f8d914b827eafa20e2967d3a94ed042e308ae`
- Maternal-deaths API response SHA-256: `c6f9a98257cb8d57625ec009a07bf869de53107c77dffce004b95d0761a3e057`
- Published gzip SHA-256: `b0f111c5f2132f3770be7939c4b72990d4ff3b51209d9a1f0f2f735653bc0186`

## Interpretation limits

Maternal deaths are difficult to identify and are sometimes misclassified, including where vital-registration systems are strong. For countries without complete registration, the inter-agency group uses regression models based on available mortality data and socioeconomic information. The World Bank metadata warns that modeled ratios are of uncertain reliability, cannot be assumed to be exact, and should not be compared with estimates produced under earlier methodology. National estimates hide subnational inequities. The map is not live surveillance, an individual risk prediction, a health-system ranking, a causal analysis, or medical advice.
