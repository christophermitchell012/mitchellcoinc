# Map 40 source and license notes

## Map

**Global Natural Events: NASA EONET Open Events**  
Public URL: <https://mitchellcoinc.com/maps/40-global-natural-events-nasa-eonet.html>

Initial publication: 2026-10-08

## Runtime source

Map 40 makes one anonymous browser request to the NASA Earth Observatory Natural Event Tracker (EONET) version 3 API:

`https://eonet.gsfc.nasa.gov/api/v3/events?status=open&limit=500`

EONET is a NASA-maintained, open-source API that curates metadata about natural events from multiple source organizations. The map displays up to 500 records whose EONET `closed` value is null at request time. It uses each event's latest supplied geometry for display, retains the source category and geometry date, and links to source URLs supplied in the record.

- EONET API documentation: <https://eonet.gsfc.nasa.gov/docs/v3>
- EONET project page: <https://eonet.gsfc.nasa.gov/>
- NASA Earthdata EONET listing: <https://www.earthdata.nasa.gov/data/tools/eonet>
- NASA Images and Media Usage Guidelines: <https://www.nasa.gov/nasa-brand-center/images-and-media/>

NASA-authored material is generally not subject to copyright in the United States, subject to NASA's media-usage guidance and third-party rights. EONET records can include links or metadata from external source organizations; those organizations retain their own rights. No NASA insignia, logotype, seal, or third-party logo is used as MitchellCo identity, and no endorsement is implied.

## Basemap and renderer

- OpenStreetMap tiles and data: © OpenStreetMap contributors, Open Database License. <https://www.openstreetmap.org/copyright>
- Leaflet 1.9.4: BSD-2-Clause. <https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE>

## Scope and limitations

- “Open” is EONET's curation lifecycle status. It is not an emergency declaration, warning, evacuation notice, or proof that conditions persist everywhere associated with the event.
- The API request is capped at 500 records. When the source returns 500, additional open events may exist outside this view.
- The map uses only the latest geometry supplied for each event. A point can be a reference location rather than the event's footprint, and an event may have multiple historical geometries not drawn here.
- EONET curates and groups source reports; its event boundaries, names, dates, and grouping may differ from an originating organization.
- The map does not calculate a risk score, forecast, loss estimate, exposure, closure, evacuation advice, or emergency alert. Open source links and consult relevant authorities before making decisions.
- Runtime data are not cached by MitchellCo. If the EONET request fails, the page reports the feed as unavailable rather than presenting a stale snapshot.
