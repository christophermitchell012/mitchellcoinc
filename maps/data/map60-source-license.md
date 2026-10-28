# Map 60 source and use notes

## Source contract

Map 60 presents FAO SDG indicator 6.4.2, **Level of water stress: freshwater withdrawal as a proportion of available freshwater resources**. FAO defines the indicator as total freshwater withdrawal by major economic sectors divided by renewable freshwater resources after accounting for environmental water requirements. The same-origin snapshot was retrieved anonymously from FAO's public SDMX endpoint on October 28, 2026. The FAO Data Explorer reported 20,016 unfiltered observations and an October 19, 2026 update.

The build retains 16,487 finite country-level observations for 182 ISO3 areas from 2000–2023. Natural Earth 1:50m country polygons map 180 areas; French Guiana and Réunion remain in the source counts but are not drawn because the reference geometry does not expose distinct matching country features. No value, boundary, or missing year is inferred.

## Provenance and integrity

- FAO indicator page: https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/642-water-stress/
- FAO Data Explorer: https://dataexplorer.fao.org/vis?df%5Bag%5D=FAO&df%5Bds%5D=ds-release&df%5Bid%5D=DF_SDG_6_4_2&df%5Bvs%5D=1.0&lc=en
- Anonymous SDMX CSV endpoint: https://nsi-release-ro-statsuite.fao.org/rest/data/FAO,DF_SDG_6_4_2,1.0/
- FAO statistical database terms: https://www.fao.org/contact-us/terms/db-terms-of-use/en
- Natural Earth country geometry: https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson
- FAO CSV SHA-256: `e1dc5728eb90e838a21bcb20b30d06eecf3cf16fb6799646751a230942718e2b`
- Natural Earth GeoJSON SHA-256: `3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb`
- Normalized compressed snapshot SHA-256: `24424d1cfb4fb9c7ab0fbe1cf73ac118e877c697533fff9af60e61bcd4c4a3ce`
- Rebuild script: `maps/scripts/map60_build_snapshot.py`

## Rights and attribution

FAO's statistical database terms license datasets under Creative Commons Attribution 4.0 unless a dataset states otherwise and require attribution. This release credits FAO, identifies the indicator, update and access dates, and links to the source and terms. Natural Earth vector data is public domain. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain OpenStreetMap attribution.

Suggested attribution: FAO. 2026. FAO Data Explorer: Indicator 6.4.2 – Level of water stress. Accessed 28 October 2026. Licence: CC BY 4.0.

## Runtime behavior

The browser downloads one same-origin deterministically compressed JSON snapshot. It makes no authenticated or live FAO request. Year and country-search controls only filter the stored observations and reference geometry.

## Limits

This is a country-level annual ratio, not a live supply gauge, local basin model, drought monitor, household water-access measure, drinking-water assessment, infrastructure status, forecast, allocation recommendation, or safety determination. Country averages can hide large subnational and seasonal differences. Values above 100 percent can occur under the indicator definition and are not capped. Nature and observation-status codes are retained as supplied. Boundaries are generalized reference geometry and do not imply endorsement or settled jurisdiction.

