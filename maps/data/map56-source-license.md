# Map 56 source and use notes

## Source contract

Map 56 combines a dated, same-origin display snapshot derived from the **2025 Federal Highway Administration National Bridge Inventory (NBI)** with an optional live NOAA/National Weather Service alert layer. FHWA's bulk file was last modified June 16, 2025 and the 2025 download page was updated June 20, 2025. It was downloaded anonymously on October 24, 2026.

The build script reads FHWA's supplied latitude, longitude, state code, and BRIDGE_CONDITION fields. It excludes 600 missing or obviously malformed coordinate values and 22 additional coordinates outside a padded Census county extent for the record's state or a broad robust state check. It draws 623,571 retained records in three transparent 8,192-pixel Web Mercator overview rasters and writes a compact state summary. The points are orientation marks, not bridge footprints or engineering geometry.

## Provenance and integrity

- FHWA 2025 NBI download page: https://www.fhwa.dot.gov/bridge/nbi/ascii2025.cfm
- Direct FHWA delimited all-state highway-bridge ZIP: https://www.fhwa.dot.gov/bridge/nbi/2025hwybronefiledel.zip
- BTS ROSA-P NBI archive: https://rosap.ntl.bts.gov/view/dot/54703
- NOAA/NWS active alerts API: https://api.weather.gov/alerts/active
- Input ZIP SHA-256: bee3b363a1f51095d0f9fb731f01a83bc30fb35243e1176955057c016e5f656e
- Good-condition raster SHA-256: 2aa184c91cb70b82e064d83160e39182aa492de5df47fb7dc779cc4cdab2eb52
- Fair-condition raster SHA-256: 2e2daeaf9ec941c780d6103baee63f062172551ca596e7c6e2b06f02d70f2cbc
- Poor-condition raster SHA-256: 6bcdae2bb5ab5917ec504afe77f035d88ccd4199a68d40b6b087d9fa10b4b2be
- State-summary SHA-256: 6f632ccb34ea78d9ab2106c5a6a700da8e76e35758b9e3bfbcd5de58201045a8
- Rebuild script: maps/scripts/map56_build_snapshot.py

## Rights and attribution

The U.S. Department of Transportation NBI Data Management Plan identifies the NBI as public-domain data reusable without restriction; citation is appreciated. The Data.gov catalog record identifies the published dataset as CC0 1.0 Universal. Census geographic reference data and NOAA/NWS alert information are U.S. government data. Map 56 retains agency names, links, dates, transformation notes, integrity hashes, and limits. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain OpenStreetMap attribution.

## Runtime behavior

The three condition rasters and state summary are same-origin static files. Active NWS alerts are not requested until the visitor presses **Load active NWS alerts**. The anonymous request keeps selected land-weather events that include official polygon or multipolygon geometry and makes no affected-zone fan-out. Alerts without polygon geometry are counted but not drawn.

## Limits

FHWA's condition category is an inventory summary, not an engineering assessment by MitchellCo. A “poor” label does not mean a bridge is unsafe; a “good” label does not replace inspection or official operating information. The display is not suitable for routing, navigation, route clearance, permitting, freight planning, load decisions, inspection scheduling, maintenance, emergency response, or asset-level analysis. FHWA specifically cautions that NBI data must not be used for route-clearance decisions. A weather polygon over a bridge point shows geographic coincidence only. It does not establish damage, closure, restriction, condition change, exposure severity, accessibility, or safety. Alerts change after page load and may omit geometry. Consult transportation agencies, emergency managers, NOAA/NWS, and local authorities for operational decisions.
