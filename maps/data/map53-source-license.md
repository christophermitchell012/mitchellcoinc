# Map 53 source and use notes

## Source contract

Map 53 is a dated, same-origin directory of U.S. EPA BEACH Program beach profiles. The source is EPA's anonymous national OGC GeoPackage download linked from the WATERS Geospatial Data Downloads page. EPA labels the extract **April 28, 2024**; the download URL is named `beach_20240228_gpkg.zip`, and its member is `beach_20240229.gpkg`. The page was downloaded on October 21, 2026.

The local compressed JSON retains only Beach ID, name, county, jurisdiction code, historical-ID flag, reported length, latest beach year, public/owner access labels, and the source start coordinate. It contains 8,450 records with valid coordinates and omits two source records lacking valid coordinates. All retained profiles report a latest beach year of 2023. State contact names, phone numbers, email addresses, internal join keys, hydrographic-event geometry, and other unused fields are intentionally excluded.

Each point links to EPA BEACON 2.0's official Beach Actions (advisories and closures) report and Water Quality Data (Monitoring) report for that Beach ID. Those reports remain on EPA's site; their rows are not copied into the local snapshot. A report may return no rows when EPA has no matching action or monitoring records.

## Provenance and integrity

- EPA fact sheet: https://www.epa.gov/waterdata/fact-sheet-beach-act-locational-data
- EPA download page: https://www.epa.gov/waterdata/waters-geospatial-data-downloads
- EPA BEACON 2.0: https://ordspub.epa.gov/ords/beacon2/r/beacon_apex/beacon2/report-page
- Source archive: https://dmap-data-commons-ow.s3.amazonaws.com/data/beach/geospatial/beach_20240228_gpkg.zip
- Archive SHA-256: `c0f0475706bf5895f81080604a1a3f2b588a7abd54b245d45b05d02910a16bc1`
- GeoPackage SHA-256: `8fe250cd76c6f389113502c297a3a40da76d19033a292ff89ae9d76e1d557f91`

The deterministic normalizer is `maps/scripts/map53_build_snapshot.py`; it verifies the extracted GeoPackage hash before writing the JSON.

## Rights and attribution

EPA materials produced by federal employees are generally public domain unless otherwise noted. EPA asks users to cite the source and not imply endorsement. This map retains EPA attribution and links users to the authoritative records. OpenStreetMap basemap tiles are attributed to OpenStreetMap contributors under the ODbL; Leaflet is BSD-2-Clause software.

## Limits

The map is a beach-profile directory, not a live advisory feed, current closure list, current sampling feed, beach boundary, monitoring-station map, contamination footprint, health assessment, forecast, or statement that swimming is safe. The source coordinate is a beach reference point. “Historical ID” is an EPA record flag, not a closure or safety status. Conditions and reporting frequency vary by jurisdiction. Consult the linked EPA report and the responsible state, tribal, territorial, or local beach program before making a recreation decision.
