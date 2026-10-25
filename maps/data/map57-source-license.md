# Map 57 source and use notes

## Source contract

Map 57 joins the World Bank's **Container Port Performance Index (CPPI) 2020–2024 Annex** to the World Bank's **Global International Ports** point layer. Both files were downloaded anonymously on October 25, 2026. The CPPI Annex was published September 22, 2025. The coordinate file was last updated July 10, 2020 and its catalog metadata was updated January 19, 2023.

The build script retains 338 of 403 CPPI rows: 331 join by exact UN/LOCODE, six by unique normalized port name plus territory/country, and one by a unique normalized port name. It omits 65 CPPI rows without a defensible match. No coordinates are geocoded, guessed, or manually placed.

## Provenance and integrity

- CPPI 2020–2024 Annex page: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099092225114541281
- Direct CPPI workbook: https://thedocs.worldbank.org/en/doc/ad77c384b22e0d83d2a8e5e850e063e3-0400022025/original/CPPI-2020-to-2024-Annex.xlsx
- Global International Ports catalog: https://datacatalog.worldbank.org/search/dataset/0038118/global-international-ports
- World Bank Data Access and Licensing: https://datacatalog.worldbank.org/public-licenses
- Direct World Bank ports GeoJSON: https://datacatalogfiles.worldbank.org/ddh-published/0038118/1/DR0046414/attributed_ports.geojson
- NASA EONET v3 documentation: https://eonet.gsfc.nasa.gov/docs/v3
- CPPI workbook SHA-256: `6ac577884a8f6fd839626923ae02a020dfe28b95c234e06189700dd236d8aa9e`
- International Ports GeoJSON SHA-256: `9b877f76ffb9decce60ce5bd8d499e3ccd67599819b8eace12f4b52df055ca42`
- Normalized snapshot SHA-256: `7a6ffd56d3ec55133262fc5412c2ceda1bb8e481c83292b28a493da8ce6b954d`
- Rebuild script: `maps/scripts/map57_build_snapshot.py`

## Rights and attribution

The World Bank page classifies the CPPI Annex as a **Dataset**. The World Bank Data Catalog states that CC BY 4.0 is the default license for datasets produced by the World Bank and distributed as open data unless another license is identified; the CPPI Annex page identifies no different dataset license. The International Ports catalog expressly marks its coordinate dataset **Creative Commons Attribution 4.0**. World Bank dataset names, authorship, links, dates, transformation notes, coverage limits, and integrity hashes are retained. NASA EONET exposes public NASA Earth-observation event metadata and source links. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain OpenStreetMap attribution.

## Runtime behavior

The joined CPPI/port snapshot is a same-origin static JSON file. The browser makes no credentialed request. Open NASA EONET events are requested only after the visitor presses **Load open EONET events**. The request is capped at 500 open records, and the map uses each event's latest supplied point or polygon geometry. It performs no port-distance, intersection, severity, exposure, loss, or impact calculation.

## Limits

The World Bank describes CPPI as a comparable measure based on observed vessel time in port. It is an annual relative benchmark, not current congestion, throughput, capacity, reliability, a service guarantee, financial performance, or a safety rating. The 2020 coordinate layer may be approximate or outdated and does not represent port boundaries. Score colors are display bins created for this map, not World Bank grades or thresholds. EONET is an event catalog rather than a warning service. Geographic proximity or overlap does not establish disruption, delay, damage, closure, capacity change, cargo loss, exposure severity, route safety, or operating conditions. Consult port authorities, carriers, emergency managers, and official notices for operational decisions.
