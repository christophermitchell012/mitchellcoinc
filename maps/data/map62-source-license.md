# Map 62 source and exception notes

## Scope

Map 62 geocodes a user-entered U.S. address, places one approximate point, and sends that point to three public polygon-query services. Each response requests GeoJSON geometry in WGS84 and verifies which electric, natural-gas and public-water polygons contain the searched point, and draws a separately selectable Leaflet layer per source-identified provider, with deterministic shades within each utility color family. A returned intersection or displayed polygon is a candidate territory match, not proof of retail service, eligibility, rates, account status, provider exclusivity, infrastructure connection, or service availability at a parcel, building, unit, or meter.

The page performs no internet-provider lookup. Its orange internet card links only to the U.S. Federal Communications Commission's National Broadband Map and accurately labels that separate resource.

## Runtime services

- OpenStreetMap Nominatim `search` converts address text to coordinates. Photon is used only as an anonymous fallback geocoder. The browser sends the typed address to the selected geocoder.
- Pacific Northwest National Laboratory's public `Electric_Retail_Service_Territories` FeatureServer performs an anonymous point-in-polygon query. The layer returned records labeled year 2020 during the October 29, 2026 feasibility check and cites EIA forms and Census TIGER/Line among its sources.
- The public `Natural_Gas_Local_Distribution_Company_Service_Territories` FeatureServer performs an anonymous point-in-polygon query. Service metadata reported a February 25, 2021 data edit during the feasibility check; sampled records cite EIA, corporate and American Gas Association inputs.
- The public `Water_System_Boundaries` FeatureServer performs an anonymous point-in-polygon query. Records include original data provider, method, public-water-system identifier, feature type and source-specific dates where supplied.
- OpenStreetMap tiles provide geographic context. Leaflet renders the map.

All calls are anonymous and browser initiated. Geometry is requested only for features intersecting the searched point. ArcGIS point-intersection results are checked again against returned GeoJSON polygons (including holes, boundaries, and multipolygons); nearby non-containing territories are excluded while real overlaps remain. Matching records are grouped by source-provided provider identifier where available or by name/state/phone otherwise. Requests paginate in batches of 100 up to 1,000 records per utility, with explicit partial-result warnings on truncation or paging failures. Each response is rejected client-side if it exceeds 4 MB. Very large territories or unavailable services can prevent rendering; this does not establish service absence. New searches clear prior overlays and ignore stale asynchronous responses. A user can enter a U.S. street address or decimal latitude/longitude; address geocoding is approximate and source boundaries may be generalized or outdated. No credential, key, token, address log, server-side proxy, local provider snapshot, or inferred territory is published.

## Narrow ArcGIS exception

This map is the sole user-approved exception to the collection's zero-Esri design rule. It uses the three named public FeatureServer query endpoints because the user explicitly accepted the working prototype and authorized publication on October 29, 2026. The exception does not apply to any other map or source candidate. Map 62 must not be described as zero-Esri compliant.

The endpoints returned HTTP 200, JSON features, anonymous query capability, and browser-compatible CORS headers during the October 29, 2026 pre-publication check. Endpoint availability and source terms can change. Public accessibility does not guarantee completeness, currency, parcel accuracy, commercial continuity, or provider confirmation.

## Source and policy links

- PNNL electric layer: https://eedgis.pnnl.gov/arcgis/rest/services/Hosted/Electric_Service_Territories/FeatureServer/0
- Natural-gas layer: https://services5.arcgis.com/HDRa0B57OVrv2E1q/arcgis/rest/services/Natural_Gas_Local_Distribution_Company_Service_Territories/FeatureServer/0
- Public-water layer: https://services.arcgis.com/cJ9YHowT8TU7DUyn/arcgis/rest/services/Water_System_Boundaries/FeatureServer/0
- Nominatim usage policy: https://operations.osmfoundation.org/policies/nominatim/
- OpenStreetMap copyright and license: https://www.openstreetmap.org/copyright
- Photon project: https://photon.komoot.io/
- FCC National Broadband Map: https://broadbandmap.fcc.gov/home

The electric and gas items are public and exposed no item-level license, access-information or terms text in the checked metadata. The EPA water item identifies U.S. EPA attribution and an MIT license. Map 62 retrieves only the attributes intersecting one user-selected point and does not redistribute bulk layer geometry. Users should consult the service owners and linked metadata for current terms. MitchellCo's HTML, CSS, JavaScript and original icon remain governed by the repository license notice; third-party services, data and marks are excluded.
