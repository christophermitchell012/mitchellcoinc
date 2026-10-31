# Map 64 source and use notes

## Source contract

Map 64 presents the World Bank's SDG 7.1.1 electricity-access estimates for the total, urban and rural populations. Each metric is the percentage of the corresponding population with access to electricity. The three World Development Indicators are `EG.ELC.ACCS.ZS`, `EG.ELC.ACCS.UR.ZS` and `EG.ELC.ACCS.RU.ZS`.

The same-origin snapshot was retrieved anonymously from the World Bank API on October 31, 2026. The API reported an October 8, 2026 update and supplied observations through 2024. The build retains each country's latest finite value from 0 through 100 and excludes World Bank regional and income aggregates. Every popup displays the actual year for the selected metric. Generalized Natural Earth polygons are reference geometry only. No value, year, boundary or missing country is inferred.

## Provenance and integrity

- World Bank national series: https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS
- World Bank urban series: https://data.worldbank.org/indicator/EG.ELC.ACCS.UR.ZS
- World Bank rural series: https://data.worldbank.org/indicator/EG.ELC.ACCS.RU.ZS
- World Bank data licensing: https://datacatalog.worldbank.org/public-licenses
- Natural Earth country geometry: https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson
- National API JSON SHA-256: `677da72ab359c44e5fa2c4697a5eee678374e206efc26a2a6a78b060f482d30e`
- Urban API JSON SHA-256: `1bf138bacfe8b1cdb99fa2652f695ceb35f38596561565279087f13ddee42b87`
- Rural API JSON SHA-256: `6cb676e1c738ba2cbce10789b959c195a2d5e816f69c3488c24455d4af031019`
- World Bank country-metadata JSON SHA-256: `c9acf3932785191a649cbc04c3056af4cf64a236e5c3b49d49be25ddb0440bce`
- Natural Earth GeoJSON SHA-256: `3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb`
- Normalized compressed snapshot SHA-256: `6041b4722515a6ce0533f2b047af904e7813f655d085c3b8d31e7d18c1a41736`
- Rebuild script: `maps/scripts/map64_build_snapshot.py`

## Rights and attribution

The World Bank pages identify the source as the SDG 7.1.1 Electrification Dataset and label the series CC BY 4.0. The World Bank's open-data licensing page describes attribution and change-notice requirements. Natural Earth vector data is public domain. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain OpenStreetMap attribution.

Suggested attribution: World Bank. 2026. SDG 7.1.1 Electrification Dataset, World Development Indicators. Accessed 31 October 2026. Licence: CC BY 4.0.

## Runtime behavior

The browser downloads one same-origin deterministically compressed JSON snapshot. It makes no authenticated or live data request. Metric and country-search controls only filter the stored observations and reference geometry.

## Limits

Access means the source's modeled or reported share of people with electricity access; it does not establish household connection quality, affordability, reliability, service hours, voltage quality, fuel mix, generation capacity, grid boundaries, utility provider, account eligibility or an individual address's service. National percentages hide local gaps and differences within urban and rural classifications. Latest values may be estimates and revision-prone. The metrics' latest years can differ by country. Boundaries are generalized reference geometry and do not imply endorsement or settled jurisdiction.
