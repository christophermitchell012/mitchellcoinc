# Map 39 source and license notes

## Map

**Superfund National Priorities List Sites & Cleanup Status**  
Public URL: <https://mitchellcoinc.com/maps/39-superfund-national-priorities-list-sites-cleanup-status.html>

Initial publication: 2026-10-07

## Snapshot source

Map 39 uses a dated, normalized snapshot of the U.S. Environmental Protection Agency Envirofacts Superfund Enterprise Management System (SEMS) `envirofacts_site` table. The snapshot was retrieved at `2026-10-07T14:25:33Z` from the anonymous, keyless Envirofacts Data Service API and includes the three National Priorities List status codes returned by separate source queries:

- `F`: Currently on the Final NPL
- `P`: Proposed for the NPL
- `D`: Deleted from the Final NPL

The build script is `maps/scripts/map39_build_snapshot.py`. It requests up to 2,500 rows for each status, validates coordinates, retains a compact factual field set, sorts deterministically, and writes `maps/data/map39-superfund-npl-sites.json`. The published snapshot contains 1,840 records with coordinates: 1,337 Final NPL, 37 Proposed NPL, and 466 Deleted-from-NPL records.

- EPA Envirofacts Data Service API: <https://www.epa.gov/enviro/envirofacts-data-service-api>
- EPA SEMS Search user guide: <https://www.epa.gov/enviro/sems-search-user-guide>
- EPA SEMS overview: <https://www.epa.gov/enviro/sems-overview>
- Snapshot endpoint pattern: `https://data.epa.gov/efservice/sems.envirofacts_site/npl_status_code/equals/{F|P|D}/1:2500/json`

SEMS is EPA's official repository for Superfund site and non-site data supporting CERCLA. EPA states that SEMS information can be freely accessed through its search. U.S. federal government data are treated as public-domain factual information unless otherwise marked. EPA does not endorse MitchellCo or this presentation, and EPA names and identifiers are not used as MitchellCo branding.

## Basemap and renderer

- OpenStreetMap tiles and data: © OpenStreetMap contributors, Open Database License. <https://www.openstreetmap.org/copyright>
- Leaflet 1.9.4: BSD-2-Clause. <https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE>

## Scope and limitations

- Points use the primary latitude/longitude values supplied by SEMS. They may represent a site reference point rather than every contaminated parcel, operable unit, plume, or affected boundary.
- Status is a program/listing status, not a current hazard rating. A deleted site is not necessarily absent from EPA records, and a proposed or final site does not imply the same conditions at every location.
- The snapshot is not live. Its retrieval timestamp and row counts are displayed in the map. Rebuild it to reflect later source changes.
- Records without usable coordinates are excluded. The source returned coordinates for all 1,840 retrieved NPL-status rows in this snapshot.
- The map does not determine exposure, contamination extent, cleanup completion, property safety, liability, health risk, distance-based risk, or regulatory compliance. Users should open the official EPA site record and consult relevant authorities for decisions.
