# Map 54 source and use notes

## Source contract

Map 54 is a dated, same-origin display of NOAA Coral Reef Watch's daily global 5 km Marine Heatwave Watch category product, version 1.0.1. The stored pixel image is for **October 18, 2026** and was downloaded from NOAA on October 22, 2026. The archive filename supplies the product date. The map does not call the snapshot live or current.

The source grid is 7,200 by 3,600 pixels at 0.05-degree resolution. NOAA defines the product values as land (-127), climatology sea ice (-1), no marine heatwave (0), and Marine Heatwave Categories 1 through 5. The page uses NOAA's exact eight-color pixel palette to identify a clicked grid cell. It does not interpolate, forecast, convert categories to temperature, or calculate a separate score.

## Provenance and integrity

- Product page: https://coralreefwatch.noaa.gov/product/marine_heatwave/index.php
- Methodology: https://coralreefwatch.noaa.gov/product/5km/methodology.php
- Dated pixel image: https://www.star.nesdis.noaa.gov/pub/socd/mecb/crw/data/marine_heatwave/v1.0.1/category/image_plain/daily/png/2026/noaa-crw_mhw_v1.0.1_category_20261018.png
- Local snapshot: `maps/data/map54-noaa-marine-heatwave-20261018.png`
- Image dimensions: 7,200 × 3,600 RGBA pixels
- Source and local snapshot SHA-256: `ecec04768aad7e8658f508eeaa8047d0d6b11a2c114bbe70a3cb84900f7eca68`

## Rights and attribution

NOAA Coral Reef Watch is a U.S. government program. The map retains NOAA attribution, product name, version, date, methodology link, and direct archive link. NOAA's site disclaimer and recommended citation guidance remain applicable. Leaflet is BSD-2-Clause software. The map uses an equirectangular coordinate reference system so the source's regular longitude-latitude grid is not forced into a Web Mercator basemap.

## Limits

Marine heatwaves are prolonged periods of anomalously high sea-surface temperature; this product categorizes them relative to NOAA's location- and day-specific climatology. It is not an air-temperature map, a forecast, a coral-bleaching alert, a fishery or navigation advisory, a local sensor reading, or a safety determination. Category does not equal degrees Celsius. NOAA notes that the static climatology sea-ice mask is conservative and is not daily sea-ice status. Pixel identification is limited by the source grid and browser coordinate rounding. Consult NOAA and local authorities for operational decisions.
