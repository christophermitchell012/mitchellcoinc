# Map 33 source and reuse notes

## Source contract
- **Source:** NOAA National Weather Service API, active wind-related alerts.
- **Alerts endpoint:** `https://api.weather.gov/alerts/active?event=High%20Wind%20Warning,Wind%20Advisory,Extreme%20Wind%20Warning,Severe%20Thunderstorm%20Warning`
- **Zone fallback:** official URLs in each alert's `affectedZones` array, limited to the first 80 unique NWS zones per page load.
- **Fields used:** event, area description, effective/expiry times, sender office, headline, description, instruction, alert geometry, affected-zone URLs, and structured `parameters.maxWindGust` when present.
- **Runtime:** the visitor's browser makes anonymous, keyless requests. No alert data are stored or proxied by MitchellCo.

## Semantics
- Alert polygons are used when NWS supplies them. Alerts without polygons use official NWS zone geometry, subject to the documented 80-zone cap.
- The category filter changes only what is displayed. It is not a forecast or risk score.
- The largest-gust statistic uses only structured `maxWindGust` values. Missing values are not inferred from prose.
- Alert descriptions may identify potential effects on trees, power lines, roofs, vehicles, marine operations, or travel. The map does not inventory infrastructure or estimate damage.
- A warning or advisory describes a hazard across an area; conditions are not uniform at every location. Users should follow the full NWS alert and local instructions.

## Availability and reuse
The NWS API is an anonymous U.S. federal public-data service. NWS web information is generally public domain unless specifically noted. Attribution does not imply NOAA or NWS endorsement. The page reports runtime failures and does not substitute cached information for current alerts.
