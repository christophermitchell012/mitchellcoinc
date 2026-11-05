# Map 69 source and use notes

## Scope

Map 69 is a click-to-query explorer for two NASA POWER climatology parameters at a user-selected coordinate:

- `ALLSKY_SFC_SW_DWN`: all-sky surface shortwave downward irradiance, shown in kWh/m²/day for the Renewable Energy community;
- `WS50M`: modeled mean wind speed 50 metres above the surface, shown in m/s.

The browser requests one point only after the visitor clicks the map or chooses **Analyze coordinates**. No API key, account, token, proxy, ArcGIS service, Esri asset or same-origin copy of POWER values is used.

## Source contract

- Endpoint: `https://power.larc.nasa.gov/api/temporal/climatology/point`
- Parameters: `ALLSKY_SFC_SW_DWN,WS50M`
- Community: `RE`
- Format: JSON
- Source access verified: 2026-11-05
- Observed response: HTTP 200, `Access-Control-Allow-Origin: *`, API version `v2.10.1`
- Observed climatology range: January 2001 through December 2025
- Authentication: none
- Request pattern: one bounded point request per explicit selection, with a 15-second client timeout and stale-response guard

NASA POWER documents the climatology endpoint as analysis-ready solar and meteorological data for direct application use. Its methodology states that radiation data use a 1° source grid and meteorological data use a 0.5° × 0.625° source grid. Wind parameters are derived from MERRA-2 components and are intended to represent regional mean flow rather than building- or terrain-scale effects.

## Reuse and attribution

NASA content is generally not subject to copyright in the United States when used factually, subject to NASA's media and non-endorsement guidance and any specifically identified third-party rights. MitchellCo credits NASA POWER in the map, source panel, attribution control and this note. No NASA insignia, logotype, seal or employee image is used, and no NASA endorsement is implied.

OpenStreetMap provides the reference basemap. © OpenStreetMap contributors; data are available under the Open Database License. The standard tile service is used only for normal interactive viewing.

Leaflet 1.9.4 is distributed under the BSD-2-Clause license.

## Interpretation limits

The values are long-term grid-cell climatology estimates, not observations at the clicked point, current conditions, forecasts, engineering-grade wind-resource assessments, bankable solar-resource studies or energy-production forecasts. Nearby coordinates may resolve to the same source cell. The map does not evaluate local terrain, turbulence, obstructions, panel tilt, shading, equipment, capacity factor, losses, land control, transmission, interconnection, permitting, environmental review, construction feasibility or project economics.

## References

- https://power.larc.nasa.gov/docs/services/api/temporal/climatology/
- https://power.larc.nasa.gov/docs/services/api/temporal/
- https://power.larc.nasa.gov/docs/methodology/
- https://power.larc.nasa.gov/docs/methodology/data/sources_meteorology/
- https://power.larc.nasa.gov/docs/services/
- https://www.nasa.gov/nasa-brand-center/images-and-media/
- https://www.openstreetmap.org/copyright
- https://operations.osmfoundation.org/policies/tiles/
- https://leafletjs.com/
