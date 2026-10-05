# Map 37 source and license notes

## Map

**Fire Weather Alerts: Wildfire Readiness Context**  
Public URL: <https://mitchellcoinc.com/maps/37-fire-weather-alerts-wildfire-readiness-context.html>

Initial publication: 2026-10-05

## Runtime sources

The map requests the NOAA National Weather Service Alerts API directly from the visitor's browser:

`https://api.weather.gov/alerts/active?event=Red%20Flag%20Warning,Fire%20Weather%20Watch`

For alerts without inline polygon geometry, the page can request the official NWS forecast-zone URLs listed in each alert's `affectedZones` property. Zone geometry is loaded only after the visitor selects an alert or presses **Draw all affected areas**. Requests are anonymous and keyless, use at most four concurrent workers, are cached for the browser session, and stop after 80 previously uncached zone URLs per action.

- NWS API documentation: <https://www.weather.gov/documentation/services-web-api>
- NWS alerts service: <https://api.weather.gov/alerts>
- NWS API terms: <https://www.weather.gov/documentation/services-web-api#/default>

The NWS API is a U.S. federal government service. NWS alert text and geometries are treated as public-domain federal information. NOAA and NWS do not endorse MitchellCo or this presentation.

## Basemap and renderer

- OpenStreetMap tiles and data: © OpenStreetMap contributors, Open Database License. <https://www.openstreetmap.org/copyright>
- Leaflet 1.9.4: BSD-2-Clause. <https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE>

## Scope and limitations

- The map includes only active NWS Red Flag Warnings and Fire Weather Watches returned at request time.
- The page does not bundle or imply a continuously updated alert snapshot. A failed browser request produces an explicit unavailable state.
- Official alert polygons are shown when supplied. Otherwise, official NWS affected-zone geometry can be drawn as a dashed fallback. Forecast zones can be much broader than the exact area experiencing critical fire-weather conditions.
- Alert descriptions may discuss wind, relative humidity, dry fuels and potential rapid fire spread. The map does not show active fires, predict ignitions, estimate spread, issue evacuation guidance or inventory burn restrictions.
- No proprietary risk score, loss estimate or readiness recommendation is calculated. Visitors should read the complete official alert and follow local fire restrictions and authorities.
