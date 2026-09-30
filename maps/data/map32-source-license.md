# Map 32 source and reuse notes

## Source contract
- **Source:** NOAA National Weather Service API, active Severe Thunderstorm Warnings.
- **Endpoint:** `https://api.weather.gov/alerts/active?event=Severe%20Thunderstorm%20Warning`
- **Fields used:** alert event, area description, effective/expiry times, sender office, headline, geometry, instruction, and the structured `parameters.maxHailSize` value when present.
- **Runtime:** the visitor's browser makes one anonymous, keyless request. No alert data are stored, proxied, or republished as a snapshot.

## Semantics
- The map includes only active Severe Thunderstorm Warnings that expose a positive structured maximum hail-size value. It does not infer hail size from prose.
- Warning polygons are official alert geometries. A warning without geometry remains in the list but cannot be drawn.
- The selected minimum-size filter is a display filter, not a forecast or risk score.
- Hail size describes the warning hazard, not a guarantee that hail will occur everywhere inside the polygon. Users should follow the full NWS warning and local instructions.

## Availability and reuse
The NWS API is an anonymous U.S. federal public-data service. NWS web information is generally public domain unless specifically noted. Attribution does not imply NOAA or NWS endorsement. The page fails visibly if the runtime request is unavailable and makes no claim that cached data are current.
