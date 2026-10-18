# Map 50 source and license notes

## Map

**Precipitation Observation Explorer: Recent USGS Values**  
Public URL: <https://mitchellcoinc.com/maps/50-recent-usgs-precipitation-values.html>

Initial publication: 2026-10-18

## Runtime source

Map 50 requests the U.S. Geological Survey modern Water Data OGC API `latest-continuous` collection after an explicit user action. Requests use parameter code `00045`, defined by USGS as “Precipitation, total, inches.” Requests restrict results to stream sites (`site_type_code=ST`) and include the current map bounding box plus a rolling 48-hour observation window.

The browser sends one anonymous, keyless request per permitted load and caps responses at 500 features. A 60-second client cooldown prevents rapid repeat requests. Missing, nonnumeric, negative, nonpoint, and older records are excluded. No proxy, proprietary GIS service, credential, or saved measurement snapshot is used.

- USGS parameter 00045: <https://api.waterdata.usgs.gov/ogcapi/v1/collections/parameter-codes/items/00045?f=html>
- USGS Water Data OGC API documentation: <https://api.waterdata.usgs.gov/docs/ogcapi>
- USGS latest-continuous collection: <https://api.waterdata.usgs.gov/ogcapi/v1/collections/latest-continuous?f=html>
- USGS copyrights and credits: <https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits>

USGS-authored data and information are generally public domain in the United States. Source credit is retained, no USGS logo is used as MitchellCo identity, and no endorsement is implied.

## Basemap and renderer

- OpenStreetMap tiles and data: © OpenStreetMap contributors, Open Database License. <https://www.openstreetmap.org/copyright>
- Leaflet 1.9.4: BSD-2-Clause. <https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE>

## Scope and limitations

- Values are recent continuous-series records returned for the requested area and 48-hour window. They may be provisional and subject to revision.
- A point represents one monitoring location and time series, not every part of a storm, river, watershed, or surrounding area.
- Multiple time series or sensors can exist at one site; the map preserves time-series identifiers and supplied statistic identifiers rather than silently merging them.
- The USGS parameter definition names total precipitation in inches but supplies no universal statistical basis or accumulation time basis. Different series can use different methods or reporting intervals. A displayed value must not be treated as a comparable storm total, daily total, rainfall rate, or intensity without reviewing that series' metadata.
- The single marker color deliberately avoids suggesting cross-site magnitude or hazard classes. It is not a flood, weather, safety, infrastructure, agricultural, or regulatory threshold.
- The 500-feature ceiling can truncate a broad view. The page tells users to zoom in when the response reaches the cap.
- The map does not infer storm totals, daily totals, rates, intensities, forecasts, flood conditions, trends, causes, exposure, damage, safety, or compliance.
- If the runtime request fails, the page reports the feed as unavailable and does not substitute stale data.
