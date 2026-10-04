# MitchellCo Interactive Data Maps

Interactive, standalone public-data maps for weather, wildfire, earthquakes, drought, floods, geology, infrastructure, environment, public risk, space weather, marine conditions, astronomy context, and current events.

## Published collection

Browse: https://mitchellcoinc.com/maps/

The collection contains Maps 00 through 36:

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

## Repository architecture

The authoritative repository is `christophermitchell012/mitchellcoinc`, branch `main`. Numbered maps live under `maps/` as `NN-map-name.html`. Saved snapshots and reusable reference data live under `maps/data/`. Topic identity SVGs live under `maps/assets/icons/` and are linked as resources rather than embedded in HTML.

Publication is intentionally simple: prepare the complete map/data/index/sitemap/docs state, run `python3 maps/scripts/check_publication.py`, commit the coherent tree, then let the read-only publication Action validate it and GitHub Pages deploy the exact committed tree. Actions do not generate, commit, or push repository content.

Static, slow-changing, rate-limited, or browser-incompatible source data should be acquired and normalized at build time. Runtime cross-origin requests are reserved for authoritative anonymous/keyless browser-CORS sources with safe client fan-out.

## Current roadmap

Next candidates:
- No number is reserved. Select the next feasible public-issue candidate after source-gate review.

Lightning Activity & Wildfire Ignition Potential is deferred until a stable authoritative lightning source passes the anonymous/keyless, browser-safe source gate.

Assign each passing candidate the lowest unused map number after checking the published collection; if a candidate is deferred, do not reserve its number.

Global Landslide Hazard & Rainfall Trigger Watch is at the bottom of the unnumbered backlog until a stable anonymous/keyless NASA LHASA path passes the source gate. Global Aviation Weather remains deferred. BloomWatch remains deferred until observation-record licensing/redistribution is clearly compatible with commercial/public reuse.

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
