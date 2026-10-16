# Map 48 source and license notes

## Map

**Dissolved Oxygen Saturation Explorer: Recent USGS Measurements**  
Public URL: <https://mitchellcoinc.com/maps/48-dissolved-oxygen-saturation-recent-usgs-measurements.html>

Initial publication: 2026-10-16

## Runtime source

Map 48 requests the U.S. Geological Survey modern Water Data OGC API `latest-continuous` collection after an explicit user action. Requests use parameter code `00301`, defined by USGS as dissolved oxygen in unfiltered water expressed as percent of saturation. Requests restrict results to stream sites (`site_type_code=ST`) and include the current map bounding box plus a rolling 48-hour observation window.

The browser sends one anonymous, keyless request per permitted load and caps responses at 500 features. A 60-second client cooldown prevents rapid repeat requests. Missing, nonnumeric, negative, nonpoint, and older records are excluded. The API reports the unit as `%`; the interface displays `% saturation` to preserve the official parameter meaning. No proxy, proprietary GIS service, credential, or saved measurement snapshot is used.

- USGS parameter 00301: <https://api.waterdata.usgs.gov/ogcapi/v1/collections/parameter-codes/items/00301?f=html>
- USGS Water Data OGC API documentation: <https://api.waterdata.usgs.gov/docs/ogcapi>
- USGS latest-continuous collection: <https://api.waterdata.usgs.gov/ogcapi/v1/collections/latest-continuous?f=html>
- USGS copyrights and credits: <https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits>

USGS-authored data and information are generally public domain in the United States. Source credit is retained, no USGS logo is used as MitchellCo identity, and no endorsement is implied.

## Basemap and renderer

- OpenStreetMap tiles and data: © OpenStreetMap contributors, Open Database License. <https://www.openstreetmap.org/copyright>
- Leaflet 1.9.4: BSD-2-Clause. <https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE>

## Scope and limitations

- Values are recent continuous measurements returned for the requested area and 48-hour window. They may be provisional and subject to revision.
- A point represents one monitoring location and time series, not every part of a river, lake, watershed, aquifer, or downstream reach.
- Multiple time series or sensors can exist at one site; the map preserves time-series identifiers rather than silently merging them.
- Percent saturation relates measured dissolved oxygen to equilibrium under local conditions. It can vary with water temperature, atmospheric pressure, salinity, mixing, photosynthesis, respiration, sensor condition, and site context, and it is not interchangeable with concentration in milligrams per liter.
- The four colors are descriptive display bands chosen for legibility. They are not oxygen-stress, ecosystem-health, impairment, treatment, safety, or regulatory thresholds.
- The 500-feature ceiling can truncate a broad view. The page tells users to zoom in when the response reaches the cap.
- The map does not infer causes, trends, oxygen stress, ecosystem health, treatment need, safety, impairment, or regulatory compliance.
- If the runtime request fails, the page reports the feed as unavailable and does not substitute stale data.
