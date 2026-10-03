# Map 35 source and license notes

## Map

**Beach & Surf Hazard Alerts: Shoreline Safety Context**  
Public URL: <https://mitchellcoinc.com/maps/35-beach-surf-hazard-alerts-shoreline-safety-context.html>

Initial publication: 2026-10-03

## Runtime sources

The map requests the NOAA National Weather Service Alerts API directly from the visitor's browser:

`https://api.weather.gov/alerts/active?event=Rip%20Current%20Statement,Beach%20Hazards%20Statement,High%20Surf%20Advisory,High%20Surf%20Warning`

For alerts without inline polygon geometry, the page can request the official NWS forecast-zone URLs listed in each alert's `affectedZones` property. Zone geometry is loaded only after the visitor selects an alert or presses **Draw all affected areas**. Requests are anonymous and keyless, use at most four concurrent workers, are cached for the browser session, and stop after 80 previously uncached zone URLs per action.

- NWS API documentation: <https://www.weather.gov/documentation/services-web-api>
- NWS alerts service: <https://api.weather.gov/alerts>
- NWS API terms: <https://www.weather.gov/documentation/services-web-api#/default>

The NWS API is a U.S. federal government service. NWS alert text and geometries are treated as public-domain federal information. NOAA and NWS do not endorse MitchellCo or this presentation.

## Basemap and renderer

- OpenStreetMap tiles and data: © OpenStreetMap contributors, Open Database License. <https://www.openstreetmap.org/copyright>
- Leaflet 1.9.4: BSD-2-Clause. <https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE>

## Scope and limitations

- The map includes only active NWS Rip Current Statements, Beach Hazards Statements, High Surf Advisories, and High Surf Warnings returned at request time.
- The page does not bundle or imply a continuously updated alert snapshot. A failed browser request produces an explicit unavailable state.
- Official alert polygons are shown when supplied. Otherwise, official NWS affected-zone geometry can be drawn as a dashed fallback. Forecast zones can be much broader than the exact hazardous shoreline.
- The map does not report lifeguard staffing, beach closures, rescue activity, measured surf at every beach, or conditions between observation points.
- No proprietary risk score, casualty estimate, or personal-safety guarantee is calculated. Visitors should read the complete official alert and follow local authorities and beach-safety personnel.
