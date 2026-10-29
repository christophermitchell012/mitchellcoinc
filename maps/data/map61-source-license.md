# Map 61 source and use notes

## Source contract

Map 61 presents FAO SDG indicator 6.4.1, **Change in water-use efficiency over time**. FAO defines national water-use efficiency as the sum of major-sector efficiencies weighted by each sector's share of total water withdrawal. The measure is gross value added per unit of water used, expressed in constant 2015 U.S. dollars per cubic metre. The same-origin snapshot was retrieved anonymously from FAO's public SDMX endpoint on October 29, 2026. The linked unfiltered workbook reported a `Last-Modified` value of July 23, 2026.

The build retains 15,805 finite country-level observations for 184 ISO3 areas from 2000–2023: 3,700 overall, 3,758 agriculture, 4,075 industry and 4,272 services observations. Generalized Natural Earth 1:50m country polygons draw all 184 represented ISO3 areas. No value, boundary, activity, or missing year is inferred.

## Provenance and integrity

- FAO indicator page: https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/641-change-in-water-use-efficiency-over-time/
- FAO Data Explorer: https://dataexplorer.fao.org/vis?df%5Bag%5D=FAO&df%5Bds%5D=ds-release&df%5Bid%5D=DF_SDG_6_4_1&df%5Bvs%5D=1.0&lc=en
- Anonymous SDMX CSV endpoint: https://nsi-release-ro-statsuite.fao.org/rest/data/FAO,DF_SDG_6_4_1,1.0/
- FAO statistical database terms: https://www.fao.org/contact-us/terms/db-terms-of-use/en
- Natural Earth country geometry: https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson
- FAO CSV SHA-256: `807c9bc328a3a31bdca0fbf2b85f3a9223890e9dc7df57755711eaad8b7dc882`
- Natural Earth GeoJSON SHA-256: `3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb`
- Normalized compressed snapshot SHA-256: `7c75e649fac8d753abfd22f623809b0d785aba82543554d8102db81b25a361d5`
- Rebuild script: `maps/scripts/map61_build_snapshot.py`

## Rights and attribution

FAO's statistical database terms license datasets under Creative Commons Attribution 4.0 unless a dataset states otherwise and require attribution. This release credits FAO, identifies the indicator and access date, and links to the source and terms. Natural Earth vector data is public domain. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain OpenStreetMap attribution.

Suggested attribution: FAO. 2026. FAO Data Explorer: Indicator 6.4.1 – Change in water-use efficiency over time. Accessed 29 October 2026. Licence: CC BY 4.0.

## Runtime behavior

The browser downloads one same-origin deterministically compressed JSON snapshot. It makes no authenticated or live FAO request. Year, activity and country-search controls only filter stored observations and reference geometry.

## Limits

This is a country-level annual economic-productivity indicator, not a direct measure of conservation, water availability, scarcity, sustainability, physical irrigation efficiency, service quality, household access, drinking-water safety, affordability, infrastructure performance, forecast, operating recommendation or safety determination. FAO notes that higher water-use efficiency can result from economic growth without reduced withdrawals. Sector estimates use different underlying economic and water-withdrawal inputs; values should not be treated as interchangeable production metrics. Country averages can hide subnational and seasonal differences. Nature and observation-status codes are retained as supplied. Boundaries are generalized reference geometry and do not imply endorsement or settled jurisdiction.
