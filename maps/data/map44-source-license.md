# Map 44 source and license notes

## Map

**Specific Conductance Explorer: Recent USGS Measurements**  
Public URL: <https://mitchellcoinc.com/maps/44-specific-conductance-recent-usgs-measurements.html>

Initial publication: 2026-10-12

## Runtime source

Map 44 requests the U.S. Geological Survey modern Water Data OGC API `latest-continuous` collection after an explicit user action. Requests use parameter code `00095`, defined by USGS as specific conductance of unfiltered water in microsiemens per centimeter at 25 degrees Celsius, restrict results to stream sites (`site_type_code=ST`), and include the current map bounding box plus a rolling 48-hour observation window.

The browser sends one anonymous, keyless request per permitted load and caps responses at 500 features. A 60-second client cooldown prevents rapid repeat requests. Missing, nonnumeric, negative, nonpoint, and older records are excluded. No proxy, proprietary GIS service, credential, or saved measurement snapshot is used.

- USGS parameter 00095: <https://api.waterdata.usgs.gov/ogcapi/v1/collections/parameter-codes/items/00095?f=html>
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
- Specific conductance measures water’s ability to carry electrical current after temperature normalization. It does not identify which dissolved ions or substances caused a value.
- Values can change with flow, runoff, groundwater inputs, local geology, sensor condition, and other local factors.
- The four display colors are descriptive bins, not salinity, drinking-water, ecological, agricultural, corrosivity, contamination, impairment, or regulatory thresholds.
- The 500-feature ceiling can truncate a broad view. The page tells users to zoom in when the response reaches the cap.
- The map does not infer constituent concentration, cause, trend, salinity class, contamination, ecosystem health, drinking-water safety, agricultural suitability, impairment, or regulatory compliance.
- If the runtime request fails, the page reports the feed as unavailable and does not substitute stale data.
