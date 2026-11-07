# Map 71 source and reuse contract

## Scope

Map 71 is an on-demand explorer for georeferenced wildlife occurrence records. A visitor selects a point and a 5, 10, or 25 kilometre radius. Nothing loads until the visitor presses **Load observations**. One bounded iNaturalist request and one bounded GBIF request are made, except that a GBIF box crossing the antimeridian may be split into two bounded requests. Each source contributes at most 30 displayed records.

## iNaturalist

- Endpoint: `https://api.inaturalist.org/v1/observations`
- Query: selected latitude, longitude and radius; Research Grade; newest observation date first; `per_page=30`; observation licence restricted to CC0 or CC BY.
- Reuse: each displayed record retains its source record link, observer, date, record licence, public coordinates and public positional accuracy when supplied. Photos are not displayed because an observation's media can have a separate licence.
- Access: anonymous and keyless. The interaction stays far below iNaturalist's published request guidance and is not bulk scraping.

## GBIF

- Endpoint: `https://api.gbif.org/v1/occurrence/search`
- Query: a bounded latitude/longitude box enclosing the selected radius; coordinates required; occurrence status PRESENT; `limit=30`; record licence restricted to CC0 1.0 or CC BY 4.0.
- Reuse: each displayed record retains its GBIF occurrence link, event date, dataset/publisher or recorded-by attribution, record licence, coordinates and coordinate uncertainty when supplied. Multimedia is not displayed because its licence can differ from the occurrence record.
- Access: anonymous and keyless. Search results, not the authenticated download service, are used.

## Accuracy and interpretation

Points are source-supplied public coordinates and can be rounded, obscured, generalized, uncertain, misidentified, old or duplicated across aggregators. The radius selects records by their displayed public coordinates; GBIF's rectangle is filtered client-side to the requested radius. A marker is evidence of a submitted occurrence record, not proof that a species is currently present, absent, common, safe, native, threatened, or accessible at that location. No live tracking, habitat boundary, population estimate, exhaustive inventory, safety advice, or regulatory determination is provided.

## Source material

- iNaturalist API documentation and recommended practices: <https://www.inaturalist.org/pages/api+recommended+practices>
- iNaturalist terms: <https://www.inaturalist.org/terms>
- iNaturalist observation data and GBIF export policy: <https://www.inaturalist.org/pages/help#gbif>
- GBIF Occurrence API: <https://techdocs.gbif.org/en/openapi/v1/occurrence>
- GBIF API rate limits: <https://techdocs.gbif.org/en/openapi/>
- GBIF data user agreement: <https://www.gbif.org/terms/data-user>
- Creative Commons CC0 1.0: <https://creativecommons.org/publicdomain/zero/1.0/>
- Creative Commons Attribution 4.0: <https://creativecommons.org/licenses/by/4.0/>

Source-policy review: 2026-11-07. Browser CORS and representative Austin-area queries were tested on 2026-11-07. The local JSON file stores only the stable query contract; live occurrence records are not republished by MitchellCo.
