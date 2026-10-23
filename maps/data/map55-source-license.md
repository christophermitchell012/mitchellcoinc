# Map 55 source and use notes

## Source contract

Map 55 combines a dated, same-origin display snapshot of the U.S. portion of the Bureau of Transportation Statistics/Federal Railroad Administration North American Rail Network (NARN) with an optional live NOAA/National Weather Service alert layer. The rail snapshot is from the **October 16, 2024** NARN file geodatabase in the non-Esri ROSA-P archive. It was downloaded on October 23, 2026.

The build script keeps U.S. line records, classifies them for display as passenger, Strategic Rail Corridor Network (STRACNET), or other rail, simplifies geometry by 500 meters in Web Mercator, and draws a transparent 8,192-pixel overview. A compact state summary preserves source record counts, source-reported mileage sums, and display bounds. These are orientation products, not precise engineering geometry.

## Provenance and integrity

- Data.gov catalog record: https://catalog.data.gov/dataset/north-american-rail-network-lines-7762c
- BTS/FRA ROSA-P archive: https://rosap.ntl.bts.gov/view/dot/53568
- Direct non-Esri archive ZIP: https://ntlrepository.blob.core.windows.net/lib/78000/78400/78432/North_American_Rail_Network_NTAD1995_Present.zip
- Local rail raster: `maps/data/map55-bts-narn-rail-lines-20241016.png`
- Local state summary: `maps/data/map55-bts-narn-state-summary-20241016.json`
- Rebuild script: `maps/scripts/map55_build_snapshot.py`
- NOAA/NWS active alerts API: https://api.weather.gov/alerts/active
- Rail raster SHA-256: `e4d794f13ca1088be6f1a31e14042400887f07f684e145c4ecc54ac454d59cee`
- State summary SHA-256: `cd8435936dda93429b3021c8bf5a8952883af6ee5c94eaa5590369234f264366`

## Rights and attribution

The Data.gov catalog identifies the NARN Rail Lines dataset as CC0 1.0 Universal. The ROSA-P DCAT metadata also links to the CC0 1.0 legal code. NOAA/NWS alert information is U.S. government data. Map 55 retains agency names, links, snapshot date, transformation notes, and limits. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain OpenStreetMap attribution.

## Runtime behavior

The rail raster and state summary are same-origin static files. Active NWS alerts are not requested until the visitor presses **Load active NWS alerts**. The anonymous request uses `api.weather.gov`, keeps selected land-weather events that include official polygon or multipolygon geometry, and makes no affected-zone fan-out. Alerts without polygon geometry are counted but not drawn.

## Limits

The rail layer is a generalized overview and is not suitable for routing, dispatch, navigation, ownership, right-of-way, grade-crossing, asset, maintenance, or engineering decisions. Display classes may overlap; source-reported mileage sums can include network and attribution complexities and are not independently measured by MitchellCo. An alert polygon over a rail line shows geographic coincidence only. It does not establish track conditions, disruption, closure, delay, speed restriction, damage, service availability, exposure severity, or safety. Alerts change after page load and may omit geometry. Consult rail operators, emergency managers, NOAA/NWS, and local authorities for operational decisions.
