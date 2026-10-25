# MitchellCo Interactive Data Maps

Interactive, standalone public-data maps for weather, wildfire, earthquakes, drought, floods, geology, infrastructure, environment, public risk, space weather, marine conditions, astronomy context, and current events.

## Published collection

Browse: https://mitchellcoinc.com/maps/

The collection contains Maps 00 through 57:

- 00 WildfireWatch
- 01 Flash Flood & River Flood Risk
- 02 Extreme Heat Health Risk
- 03 Wildfire Smoke Exposure
- 04 Hurricane & Storm Surge Impact
- 05 Breaking News Geography
- 06 Severe Storm & Tornado Exposure
- 07 Wildfire Evacuation Risk
- 08 Drought & Water Supply Stress
- 09 Power Grid Stress & Extreme Weather
- 10 Drinking Water Quality Risk
- 11 Internet Outage Watch
- 12 Coastal Flooding & High Tide Risk
- 13 Earthquake Impact
- 14 FEMA Disaster Declarations
- 15 Air Quality Health Risk
- 16 Reservoir Water Shortage Monitor
- 17 Agricultural Drought & Farm Exposure
- 18 National Weather Alert Impact
- 19 Aurora & Geomagnetic Impact
- 20 Earthquake Shaking Impact
- 21 Northern Hemisphere Snow & Ice Conditions
- 22 MarineWatch
- 23 VolcanoWatch
- 24 Deep Time Under Your Feet
- 25 Watershed Explorer
- 26 Dark Sky Tonight
- 27 Your Compass Lies
- 28 Daylight Explorer
- 29 Groundwater Level & Drought Stress
- 30 River Ice Jam History & Current Conditions
- 31 Tornado Climatology & Current Severe Weather Context
- 32 Hail Warning Exposure & Property Risk Context
- 33 High Wind Alerts & Infrastructure Impact Context
- 34 Freeze & Frost Alerts: Crop, Pipe & Health Context
- 35 Beach & Surf Hazard Alerts: Shoreline Safety Context
- 36 Dense Fog Alerts: Transportation Visibility Context
- 37 Fire Weather Alerts: Wildfire Readiness Context
- 38 Gale & Storm Marine Alerts: Coastal Operations Context
- 39 Superfund National Priorities List Sites & Cleanup Status
- 40 Global Natural Events: NASA EONET Open Events
- 41 Stream Temperature Explorer: Latest USGS Measurements
- 42 Dissolved Oxygen Explorer: Recent USGS Measurements
- 43 Stream pH Explorer: Recent USGS Measurements
- 44 Specific Conductance Explorer: Recent USGS Measurements
- 45 Streamflow Explorer: Recent USGS Discharge Measurements
- 46 River Gage Height Explorer: Recent USGS Measurements
- 47 Stream Turbidity Explorer: Recent USGS Measurements
- 48 Dissolved Oxygen Saturation Explorer: Recent USGS Measurements
- 49 Nitrate + Nitrite Explorer: Recent USGS Measurements
- 50 Precipitation Observation Explorer: Recent USGS Values
- 51 Global Soil Moisture & Drought Watch
- 52 California Coastal Erosion & Shoreline Change
- 53 U.S. Beach Water Quality & Advisory History
- 54 Global Marine Heatwave & Ocean Temperature Watch
- 55 U.S. Rail Network Weather & Hazard Exposure
- 56 U.S. Highway Weather & Bridge Exposure
- 57 Global Port Performance & Hazard Exposure

## Repository architecture

The authoritative repository is `christophermitchell012/mitchellcoinc`, branch `main`. Numbered maps live under `maps/` as `NN-map-name.html`. Saved snapshots and reusable reference data live under `maps/data/`. Topic identity SVGs live under `maps/assets/icons/` and are linked as resources rather than embedded in HTML.

Publication is intentionally simple: prepare the complete map/data/index/sitemap/docs state, run `python3 maps/scripts/check_publication.py`, commit the coherent tree, then let the read-only publication Action validate it and GitHub Pages deploy the exact committed tree. Actions do not generate, commit, or push repository content.

Static, slow-changing, rate-limited, or browser-incompatible source data should be acquired and normalized at build time. Runtime cross-origin requests are reserved for authoritative anonymous/keyless browser-CORS sources with safe client fan-out.

## Current roadmap

The approved sequence below governs the next releases. Numbers identify sequence, not a promise to publish a candidate that fails the source gate. A failed candidate is documented and deferred without consuming its number; the next feasible candidate inherits the lowest unused number.

| Sequence | Candidate | Primary source | Status |
|---|---|---|---|
| 51 | Global Soil Moisture & Drought Watch | NOAA CPC | Published |
| 52 | Coastal Erosion & Shoreline Change | USGS Coastal Change Hazards | Published |
| 53 | Beach Water Quality & Advisory History | EPA BEACON | Published |
| 54 | Global Marine Heatwave & Ocean Temperature Watch | NOAA OISST / Coral Reef Watch | Published |
| 55 | Rail Network Weather & Hazard Exposure | BTS NTAD / NOAA | Published |
| 56 | Highway Weather & Bridge Exposure | FHWA NBI / NOAA | Published |
| 57 | Global Port Performance & Hazard Exposure | World Bank CPPI | Published |
| 58 | Global Dams, Reservoirs & Water Exposure | FAO | Next |
| 59 | Levee & Flood-Control Infrastructure Risk | USACE National Levee Database | Planned |
| 60 | Global Water Stress & Supply Pressure | FAO AQUASTAT | Planned |

Lightning Activity & Wildfire Ignition Potential is deferred until a stable authoritative lightning source passes the anonymous/keyless, browser-safe source gate.

Assign each passing candidate the lowest unused map number after checking the published collection; if a candidate is deferred, do not reserve its number.

Global Landslide Hazard & Rainfall Trigger Watch is at the bottom of the unnumbered backlog until a stable anonymous/keyless NASA LHASA path passes the source gate. Global Aviation Weather remains deferred. BloomWatch remains deferred until observation-record licensing/redistribution is clearly compatible with commercial/public reuse.

Civil Emergency Alerts & Public Safety Context is deferred because the active NWS-distributed alert tested on 2026-10-05 supplied neither polygon geometry nor resolvable affected-zone URLs. Reconsider only when the source supports a truthful map rather than an area-name list.

Open Emergency Shelters was evaluated on 2026-10-07. FEMA's public Open Shelters service exposed the needed points through an ArcGIS FeatureServer rather than a qualifying zero-Esri source, while the guessed OpenFEMA endpoint returned 404. It remains unnumbered and deferred until an authoritative non-Esri snapshot or API passes the source gate.

Stream Velocity Explorer was evaluated on 2026-10-15 using USGS parameter 00055. The recent nationwide stream-site query returned only one series, so it remains unnumbered and deferred until the source supplies enough current observations for a useful geographic view.

The filtered-water nitrate-plus-nitrite series candidate was evaluated on 2026-10-17 using USGS parameter 00631. The recent nationwide stream-site query returned no series, so that parameter remains deferred. Map 49 instead uses the distinct in-situ parameter 99133 after its source contract and geographic coverage passed review.

## Recent source contracts

- **Map 21:** U.S. National Ice Center IMS daily chart images, displayed directly; no snow-depth or ice-thickness claim.
- **Map 24:** Macrostrat surface geology plus EarthByte/GPlates reconstruction context.
- **Map 25:** USGS NLDI connected-flowline navigation with bounded distance.
- **Map 26:** NASA VIIRS Black Marble reference radiance, NOAA/NWS cloud forecast, and derived Sun/Moon context. Its build tooling may use the user-authorized `EARTHDATA_TOKEN`; the token is never published.
- **Map 27:** NOAA/BGS WMM2025 coefficients and official test vectors loaded same-origin.
- **Map 28:** Client-side solar geometry with no runtime weather claims.
- **Map 29:** USGS Water Data OGC `latest-continuous`, parameter 72019, loaded only on explicit user action; raw groundwater depth is not converted into a drought score.
- **Map 30:** USACE CRREL Ice Jam Database. The map uses a dated same-origin factual subset of the anonymous Water Year 2026 report. It is not a forecast, live closure feed, or exhaustive copy. See `data/map30-source-license.md`.
- **Map 31:** NOAA SPC `1950-2025_actual_tornadoes.csv`, stored as a dated same-origin snapshot (`scripts/map31_build_snapshot.py` rebuilds it). Historical counts are 1-degree start-point counts with no forecast or risk score. A live layer requests active NWS tornado alerts from `api.weather.gov` in the visitor's browser and degrades to a status message if it fails. See `data/map31-source-license.md`.
- **Map 32:** NOAA/NWS active Severe Thunderstorm Warnings requested anonymously from `api.weather.gov` in the visitor's browser. The page displays only warnings with a positive structured `maxHailSize`, preserves NWS geometry and wording, and calculates no forecast, damage estimate, or proprietary risk score. See `data/map32-source-license.md`.
- **Map 33:** NOAA/NWS active wind-related alerts requested anonymously from `api.weather.gov`. Official alert polygons are used when present; a bounded 80-zone fallback retrieves official affected-zone geometry for alerts such as Wind Advisories. Structured gusts are displayed without inferring missing values, and no outage, damage, or proprietary risk score is calculated. See `data/map33-source-license.md`.
- **Map 34:** NOAA/NWS active Freeze Warnings, Frost Advisories, Hard Freeze Warnings, Freeze Watches, and Cold Weather Advisories. The alert feed loads anonymously; exact NWS affected-zone geometry loads only on explicit user action with caching, four-request concurrency, and an 80-zone ceiling. The page calculates no crop, plumbing, health, or loss score. See `data/map34-source-license.md`.
- **Map 35:** NOAA/NWS active Rip Current Statements, Beach Hazards Statements, High Surf Advisories, and High Surf Warnings. The alert feed loads anonymously; exact NWS affected-zone geometry loads only on explicit user action with caching, four-request concurrency, and an 80-zone ceiling. The page reports no lifeguard, closure, rescue, proprietary risk, or personal-safety claim. See `data/map35-source-license.md`.
- **Map 36:** NOAA/NWS active Dense Fog Advisories and Freezing Fog Advisories. The alert feed loads anonymously; exact NWS affected-zone geometry loads only on explicit user action with caching, four-request concurrency, and an 80-zone ceiling. The page reports no measured visibility, crash, closure, delay, pavement-condition, proprietary risk, or route-safety claim. See `data/map36-source-license.md`.
- **Map 37:** NOAA/NWS active Red Flag Warnings and Fire Weather Watches. The alert feed loads anonymously; exact NWS affected-zone geometry loads only on explicit user action with caching, four-request concurrency, and an 80-zone ceiling. The page reports no active-fire, ignition, spread, evacuation, restriction, loss, proprietary-risk, or readiness recommendation. See `data/map37-source-license.md`.
- **Map 38:** NOAA/NWS active Gale Warnings/Watches, Storm Warnings/Watches, Hurricane Force Wind Warnings/Watches, Hazardous Seas Warnings/Watches, and Special Marine Warnings. The alert feed loads anonymously; exact NWS marine-zone geometry loads only on explicit user action with caching, four-request concurrency, and an 80-zone ceiling. The page provides no vessel routing, port-closure, inferred wave-height, loss, proprietary-risk, or operating recommendation. See `data/map38-source-license.md`.
- **Map 39:** U.S. EPA Envirofacts SEMS proposed, final, and deleted National Priorities List site records. A dated, normalized same-origin snapshot contains 1,840 official source points retrieved anonymously on 2026-10-07; the page calculates no contamination boundary, exposure, cleanup-completion, liability, health-risk, or property-safety score. See `data/map39-source-license.md`.
- **Map 40:** NASA EONET v3 open natural-event records requested anonymously at runtime, capped at 500 records. The page displays each event's latest supplied geometry and treats “open” only as an EONET lifecycle status; it calculates no alert, forecast, risk, exposure, loss, or evacuation guidance. See `data/map40-source-license.md`.
- **Map 41:** USGS Water Data OGC `latest-continuous`, parameter 00010, requested anonymously only after explicit user action for the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. Temperature bands are descriptive labels, not safety, ecological, regulatory, or biological thresholds. See `data/map41-source-license.md`.
- **Map 42:** USGS Water Data OGC `latest-continuous`, parameter 00300, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map preserves time-series IDs and treats value colors only as descriptive display bands, not ecological, safety, impairment, or regulatory thresholds. See `data/map42-source-license.md`.
- **Map 43:** USGS Water Data OGC `latest-continuous`, parameter 00400, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map preserves time-series IDs and treats pH colors only as descriptive display bands, not ecological, drinking-water, recreational-safety, impairment, corrosivity, or regulatory thresholds. See `data/map43-source-license.md`.
- **Map 44:** USGS Water Data OGC `latest-continuous`, parameter 00095, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map excludes missing and negative values, preserves time-series IDs, and treats colors only as descriptive bins, not salinity, ecological, drinking-water, agricultural, contamination, impairment, or regulatory thresholds. See `data/map44-source-license.md`.
- **Map 45:** USGS Water Data OGC `latest-continuous`, parameter 00060, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map excludes missing and negative values, preserves time-series IDs, and treats colors only as descriptive magnitude bins, not low-flow, normal-flow, flood, navigability, safety, ecological, drought, or regulatory thresholds. See `data/map45-source-license.md`.
- **Map 46:** USGS Water Data OGC `latest-continuous`, parameter 00065, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map preserves finite negative values because gage height is relative to a local datum, preserves time-series IDs, and uses one marker color to avoid implying cross-site flood, bankfull, navigation, safety, ecological, or regulatory thresholds. See `data/map46-source-license.md`.
- **Map 47:** USGS Water Data OGC `latest-continuous`, parameter 63680, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map excludes missing and negative values, preserves time-series IDs, normalizes the API's `_FNU` display string to the official `FNU` unit, and treats colors only as descriptive bands, not water-clarity, drinking-water, ecological, recreational, impairment, or regulatory thresholds. See `data/map47-source-license.md`.
- **Map 48:** USGS Water Data OGC `latest-continuous`, parameter 00301, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map excludes missing and negative values, preserves time-series IDs, expands the API's `%` unit label to `% saturation`, and treats colors only as descriptive bands, not oxygen-stress, ecosystem-health, impairment, treatment, safety, or regulatory thresholds. See `data/map48-source-license.md`.
- **Map 49:** USGS Water Data OGC `latest-continuous`, parameter 99133, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map excludes missing and negative values, preserves time-series IDs, and treats colors only as descriptive bands, not drinking-water, aquatic-life, health, agricultural, impairment, treatment, or regulatory thresholds. See `data/map49-source-license.md`.
- **Map 50:** USGS Water Data OGC `latest-continuous`, parameter 00045, requested anonymously only after explicit user action for stream sites in the visible map area and prior 48 hours, capped at 500 records with a 60-second client cooldown. The map excludes missing and negative values, preserves time-series and supplied statistic IDs, and uses one marker color because the parameter definition supplies no universal accumulation time basis. It makes no storm-total, daily-total, rate, intensity, forecast, flood, damage, safety, or compliance claim. See `data/map50-source-license.md`.
- **Map 51:** NOAA CPC Global Land Surface Monitor soil-moisture percentile and anomaly images, loaded one at a time directly from the official source without credentials. The interface preserves the official embedded date and legend, does not sample or georegister image pixels, and makes no sensor-reading, parcel, drought-declaration, flash-drought, crop-loss, fire, water-availability, forecast, safety, or regulatory claim. See `data/map51-source-license.md`.
- **Map 52:** USGS Data Report 1187 long-term California shoreline-change summary statistics, stored as a dated same-origin snapshot. The map presents the three regional rates, erosional/accretional shares, confidence intervals, and six named maximum-rate locations. Location markers are approximate orientation points, not source transects, parcels, hazard boundaries, live shorelines, forecasts, surveys, setback maps, engineering assessments, or property estimates. See `data/map52-source-license.md`.
- **Map 53:** EPA BEACH Program national geospatial download, stored as a dated same-origin snapshot of 8,450 beach profiles with valid reference coordinates. Each point links to EPA BEACON's official advisory/closure and monitoring reports; those report rows are not copied locally. The map is a directory, not a live advisory feed, current closure list, sampling feed, beach boundary, monitoring-station map, contamination footprint, or swimming-safety determination. See `data/map53-source-license.md`.
- **Map 54:** NOAA Coral Reef Watch Marine Heatwave Watch v1.0.1, stored as the dated 2026-10-18 same-origin global 5 km category pixel image. Click identification uses NOAA's exact palette; category is not degrees Celsius. The map is not live, a forecast, local sensor reading, coral-bleaching alert, fishery/navigation advisory, or safety determination. See `data/map54-source-license.md`.
- **Map 55:** BTS/FRA North American Rail Network, stored as a dated 2024-10-16 same-origin generalized transparent rail raster plus state summary. Active NOAA/NWS land-weather polygons load only after explicit user action. Geographic overlap does not establish rail disruption, closure, delay, track condition, damage, or operating restriction. See `data/map55-source-license.md`.
- **Map 56:** FHWA 2025 National Bridge Inventory, stored as three dated same-origin generalized transparent condition rasters plus a state summary. Active NOAA/NWS land-weather polygons load only after explicit user action. Condition labels reproduce FHWA's source field; geographic overlap does not establish damage, closure, restriction, condition change, route clearance, accessibility, or safety. See `data/map56-source-license.md`.
- **Map 57:** World Bank CPPI 2020–2024 Annex joined to the CC BY 4.0 World Bank International Ports coordinate layer. The dated same-origin snapshot retains 338 of 403 CPPI rows; 65 unmatched rows are omitted rather than geocoded or guessed. Open NASA EONET event geometries load only after explicit user action. Geographic coincidence does not establish disruption, delay, damage, closure, capacity change, cargo loss, route safety, or operating conditions. See `data/map57-source-license.md`.

## Site/search files

`index.html` is the crawlable collection directory. `sitemap.xml` lists the index and every numbered map. `robots.txt` points to the sitemap. `_config.yml` defines the `/maps` base URL. `scripts/check_publication.py` is the read-only integrity checker and `scripts/build_sitemap.py` deterministically builds the sitemap.

## Design goals

- Browser-first standalone HTML where practical
- Authoritative or explicitly approved public sources
- Same-origin snapshots for static/slow/rate-limited data
- No credentials in public runtime code
- Zero prohibited proprietary GIS platform dependencies
- Clear attribution and source semantics
- GA4 `G-8SVEH8WD1R`
- GitHub Pages friendly and crawlable

## License

See [LICENSE](LICENSE).


## Migration and deployed verification

The old `christophermitchell012/maps` repository preserves legacy URLs with immediate redirects and new canonical URLs. New maps must be published only in this repository's `maps/` directory. The root Jekyll sitemap retains blog discovery and includes the static map HTML; `maps/sitemap.xml` is deterministic and generated before committing.

Run `python3 scripts/check_publication.py`, `python3 maps/scripts/build_sitemap.py --check`, and `python3 maps/scripts/check_publication.py` before publication. Read-only CI additionally runs `python3 maps/scripts/check_deployment.py` after pushes to main, verifying all numbered maps, support pages, local assets/data, and both sitemaps against the published site. External runtime APIs and browser rendering require separate checks.
