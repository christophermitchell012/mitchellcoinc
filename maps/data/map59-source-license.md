# Map 59 source and use notes

## Source contract

Map 59 uses the generalized nationwide alignment topology embedded in the public U.S. Army Corps of Engineers National Levee Database (NLD) search page. The page and payload were retrieved anonymously on October 27, 2026. NLD's public interface also offers CSV, GeoJSON and GeoPackage downloads, and its documentation states that NLD data can be downloaded, shared and used by anyone.

The dated same-origin snapshot contains 6,102 generalized alignment features. It preserves the source feature codes and geometry. It does not copy inspection, rating, accreditation, risk, population, financial, structure, or operating-status fields.

For the state filter only, the build script locates each alignment's middle coordinate in the repository's generalized 2025 U.S. Census county reference. This is an approximate display assignment; it is not an NLD attribute and can be wrong for lines that cross boundaries or fall outside the county reference.

## Provenance and integrity

- NLD public search and download interface: https://levees.sec.usace.army.mil/search
- NLD public data documentation: https://levees.sec.usace.army.mil/about/about-the-data/
- NLD public data services: https://nld.sec.usace.army.mil/data-services/services/
- NLD public API reference: https://levees.sec.usace.army.mil/developer/
- USACE Open Technology / open data: https://www.usace.army.mil/Business-With-Us/Open-Technology/
- Source HTML SHA-256: `f3185286ab2b32c7b9c690b75466490a2b26e3b433f632e5b2e6148afecfd685`
- Normalized compressed snapshot part SHA-256 values: part 1 `8297144608afd014525d1e1327aac7071a054cdac691cd4629e99d1a7ccfa3d4`; part 2 `b0430aa513264a5f5b046d64f3b38160b0b78377b25e040121aa0ddcf1cbdc2b`; part 3 `ce3ab90d830c0ff5c0a434783ba5a77e12db5c2808d0a82b0e3335a4a5b772b1`
- Rebuild script: `maps/scripts/map59_build_snapshot.py`

## Rights and attribution

USACE states that NLD data may be downloaded, shared and used by anyone. USACE open-data material is produced by the federal government and is generally not subject to U.S. copyright protection. The map attributes USACE NLD, describes its transformation, and does not use an agency logo or imply endorsement. Leaflet is BSD-2-Clause software; OpenStreetMap tiles retain visible OpenStreetMap attribution.

## Runtime behavior

The alignment snapshot is a same-origin deterministically compressed JSON file. The browser uses its native gzip decompressor and makes no credentialed request. Active NOAA/NWS flood-related alert polygons are requested only after the visitor presses **Load active NWS flood alerts**. Only alert records that already include polygon or multipolygon geometry are drawn; affected-zone fallbacks are not requested.

## Limits

USACE says NLD completeness, quality and update timing vary, information is the best available, and USACE does not independently validate every submitted value. Generalized lines are not surveyed boundaries, leveed-area polygons, inundation zones, property boundaries, evacuation zones, hydraulic models or engineering drawings. Feature presence or proximity does not establish ownership, accreditation, certification, maintenance, inspection, structural condition, flood protection, overtopping probability, failure probability or operating status. NWS alert overlap is geographic context only and does not establish levee loading, damage, failure, closure, breach, protection level or safety. Consult NLD detail pages, levee sponsors, emergency managers and official warnings for decisions.
