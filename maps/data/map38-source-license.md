# Map 38 source and license notes

## Map

**Gale & Storm Marine Alerts: Coastal Operations Context**  
Public URL: <https://mitchellcoinc.com/maps/38-gale-storm-marine-alerts-coastal-operations-context.html>

Initial publication: 2026-10-06

## Runtime sources

The map requests the NOAA National Weather Service Alerts API directly from the visitor's browser:

`https://api.weather.gov/alerts/active?event=Gale%20Warning,Gale%20Watch,Storm%20Warning,Storm%20Watch,Hurricane%20Force%20Wind%20Warning,Hurricane%20Force%20Wind%20Watch,Hazardous%20Seas%20Warning,Hazardous%20Seas%20Watch,Special%20Marine%20Warning`

For alerts without inline polygon geometry, the page can request the official NWS marine-zone or forecast-zone URLs listed in each alert's `affectedZones` property. Zone geometry is loaded only after the visitor selects an alert or presses **Draw all affected areas**. Requests are anonymous and keyless, use at most four concurrent workers, are cached for the browser session, and stop after 80 previously uncached zone URLs per action.

- NWS API documentation: <https://www.weather.gov/documentation/services-web-api>
- NWS alerts service: <https://api.weather.gov/alerts>
- NWS API terms: <https://www.weather.gov/documentation/services-web-api#/default>

The NWS API is a U.S. federal government service. NWS alert text and geometries are treated as public-domain federal information. NOAA and NWS do not endorse MitchellCo or this presentation.

## Basemap and renderer

- OpenStreetMap tiles and data: © OpenStreetMap contributors, Open Database License. <https://www.openstreetmap.org/copyright>
- Leaflet 1.9.4: BSD-2-Clause. <https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE>

## Scope and limitations

- The map includes only active NWS Gale Warnings/Watches, Storm Warnings/Watches, Hurricane Force Wind Warnings/Watches, Hazardous Seas Warnings/Watches and Special Marine Warnings returned at request time.
- The page does not bundle or imply a continuously updated alert snapshot. A failed browser request produces an explicit unavailable state.
- Official alert polygons are shown when supplied. Otherwise, official NWS affected-zone geometry can be drawn as a dashed fallback. Marine zones can be much broader than the exact hazardous area.
- Alert descriptions may discuss hazardous winds, waves, thunderstorms or seas. The map does not route vessels, report port closures, infer wave heights where absent, or replace Coast Guard or local navigation guidance.
- No proprietary risk score, loss estimate or operating recommendation is calculated. Mariners should read the complete official alert and follow Coast Guard, port and local authorities.
