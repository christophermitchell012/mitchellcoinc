# Map 34 source and reuse notes

## Source contract
- **Source:** NOAA National Weather Service API, active freeze, frost, and cold alerts.
- **Alerts endpoint:** `https://api.weather.gov/alerts/active?event=Freeze%20Warning,Frost%20Advisory,Hard%20Freeze%20Warning,Freeze%20Watch,Cold%20Weather%20Advisory`
- **Geometry:** official alert geometry when supplied; otherwise the official URLs in each alert's `affectedZones` array.
- **Fields used:** event, area description, effective/expiry times, sender office, headline, description, instruction, alert geometry, affected-zone URLs, and NWS severity.
- **Runtime:** one anonymous, keyless alert request loads automatically. Exact zone geometry loads only after an explicit user action, with four-request concurrency, caching, and an 80-zone ceiling. No alert data are stored or proxied by MitchellCo.

## Semantics
- The map displays official alert categories and affected areas. Filters change only the display and are not a forecast or risk score.
- Alert text may describe potential effects on sensitive vegetation, outdoor plumbing, pets, livestock, travel, or people. The map does not inventory crops or pipes, estimate losses, or provide medical advice.
- Conditions are not uniform inside an alert area. Users should follow the full NWS alert and local instructions.
- If the alert or zone service fails, the page reports the failure and does not substitute cached information.

## Availability and reuse
The NWS API is an anonymous U.S. federal public-data service. NWS web information is generally public domain unless specifically noted. Attribution does not imply NOAA or NWS endorsement.
