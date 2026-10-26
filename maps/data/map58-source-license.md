# Map 58 source and use notes

## Source contract

Map 58 normalizes the nine regional Excel workbooks linked from the FAO AQUASTAT **Geo-referenced Database on Dams** page. They were downloaded anonymously on October 26, 2026. The accompanying FAO Data Catalog record identifies **Dams (Global - edition 2026)**, revision July 16, 2026, and documents the same dam, reservoir, purpose, latitude and longitude attributes.

The build retains 8,502 rows with valid latitude and longitude. It omits 6,078 rows without coordinates. No coordinate is geocoded, inferred, repaired or manually placed.

## Provenance and integrity

- AQUASTAT dam database and regional downloads: https://www.fao.org/aquastat/en/databases/dams
- FAO catalog record: https://data.fao.org/catalog/iso/f869d8a9-326b-4975-b84a-fd36c64d4e14
- Catalog API record: https://data.apps.fao.org/catalog/api/3/action/package_show?id=f869d8a9-326b-4975-b84a-fd36c64d4e14
- Creative Commons Attribution 4.0: https://creativecommons.org/licenses/by/4.0/
- NASA EONET v3 documentation: https://eonet.gsfc.nasa.gov/docs/v3
- Regional workbook SHA-256 values: Africa `2f7adc94ce89aa46e0ffd65e87310eb424262135c7a0eaf1620be4f4e68da817`; Central America and Caribbean `7074adeed96a83fb488d4f5754ece99abbdb85fbb80ee7aac2f32e9945851e0c`; Central Asia `33fb2bfb04179921b5c6ba8e665d69332bd77a396d3d23302e703c8dfa570a2d`; Europe `327e562b809773d5784aa0f6743febba41f8e903534cb8acd54e1c41c9418841`; Middle East `cbe469e2e4b5788a7818c23ee7cf3ae8fa9c45a094f3a38b0d22760c902c95d0`; Northern America `7a962b306555a1abd3e12c19524f6f132e09e7077eac28e5cf0d0a857279f6a8`; Oceania `e0ec02df9cf8fcd215a20b89083f3654f2067e211cc3a780e8223d5a7ac7c4c4`; Southern America `63823652f8db7724880850d1f57f4e1b8ea7f6ffe8db53c4f4e7def992e46bef`; Southern and Eastern Asia `dc05be7aeb0ff89935bcb6474aa43d6b0eef12f842248eeb5b481959cf259285`.
- Normalized compressed snapshot SHA-256: `914d95ffb83f5d59147031769cd6f94840cc0762abe45d154b5f7084d7630190`
- Rebuild script: `maps/scripts/map58_build_snapshot.py`

## Rights and attribution

The FAO catalog record expressly makes the dataset available under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. FAO/AQUASTAT names, links, edition, revision, transformation notes, omissions and integrity hashes are retained. NASA EONET exposes public NASA Earth-observation event metadata and source links. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain OpenStreetMap attribution.

## Runtime behavior

The normalized dam snapshot is a same-origin deterministically compressed JSON file. The browser uses its native gzip decompressor and makes no credentialed request. Open NASA EONET events are requested only after the visitor presses **Load open EONET events**. The map performs no proximity, intersection, severity, exposure, loss, inundation or downstream-impact calculation.

## Limits

FAO says the regional workbooks are neither complete nor error-free and that published reports and maps are not updated frequently. Missing rows, attributes and coordinates are expected; reservoir capacity, area, height, purpose and operational year may be absent or dated. Points are not dam or reservoir footprints, inspection findings, structural-condition observations, water levels, storage measurements, failure scenarios or inundation zones. Display bins are not FAO classes or safety thresholds. EONET is an event catalog rather than a warning service. Geographic proximity or overlap does not establish dam safety, failure probability, damage, storage status, water level, downstream impact or operating conditions. Consult dam owners, regulators and emergency managers for operational or safety decisions.
