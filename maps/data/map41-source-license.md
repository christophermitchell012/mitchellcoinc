# Map 41 source and license notes

## Map

**Stream Temperature Explorer: Latest USGS Measurements**  
Public URL: <https://mitchellcoinc.com/maps/41-stream-temperature-latest-usgs-measurements.html>

Initial publication: 2026-10-09

## Runtime source

Map 41 requests the U.S. Geological Survey modern Water Data OGC API `latest-continuous` collection after an explicit user action. Requests use parameter code `00010`, defined by USGS as water temperature in degrees Celsius, restrict results to stream sites (`site_type_code=ST`), and include the current map bounding box plus a rolling 48-hour observation window.

The browser sends one anonymous, keyless request per permitted load and caps responses at 500 features. A 60-second client cooldown prevents rapid repeat requests. No proxy, proprietary GIS service, credential, or saved measurement snapshot is used.

- USGS Water Data OGC API documentation: <https://api.waterdata.usgs.gov/docs/ogcapi>
- USGS instantaneous-values documentation and parameter-code guidance: <https://waterservices.usgs.gov/docs/instantaneous-values/instantaneous-values-details/>
- USGS water-data metadata guidance: <https://waterdata.usgs.gov/blog/wdfn-metadata>
- USGS copyrights and credits: <https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits>

USGS-authored data and information are generally public domain in the United States. Source credit is retained, no USGS logo is used as MitchellCo identity, and no endorsement is implied.

## Basemap and renderer

- OpenStreetMap tiles and data: © OpenStreetMap contributors, Open Database License. <https://www.openstreetmap.org/copyright>
- Leaflet 1.9.4: BSD-2-Clause. <https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE>

## Scope and limitations

- Values are the latest continuous observations returned for the requested area and 48-hour window. They may be provisional and subject to revision.
- A point represents a monitoring location, not the temperature of every part of a river, lake, watershed, or downstream reach.
- Stations differ in sensor placement, depth, sampling interval, local flow, shade, season, and watershed context. Values should not be compared as if every site were measuring identical conditions.
- The four display colors are descriptive temperature bins, not ecological, regulatory, swimming-safety, drinking-water, fish-stress, or health thresholds.
- The 500-feature ceiling can truncate a broad view. The page tells users to zoom in when the response reaches the cap.
- The map does not infer trend, cause, dissolved oxygen, pathogen levels, algal blooms, fish mortality, habitat suitability, recreational safety, drinking-water safety, or regulatory compliance.
- If the runtime request fails, the page reports the feed as unavailable and does not substitute stale data.
