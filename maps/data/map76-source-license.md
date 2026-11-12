# Map 76 source, calculation, and reuse notes

## Scope

Map 76 compares the estimated share of the civilian noninstitutionalized population without health-insurance coverage in 3,222 counties or county equivalents. It uses the U.S. Census Bureau 2020–2024 American Community Survey five-year table B27001 and 2024 1:20,000,000 cartographic county boundaries.

## Sources and acquisition

- ACS table-based summary file: `acsdt5y2024-b27001.dat`
- County boundaries: `cb_2024_us_county_20m.zip`
- Downloaded from `www2.census.gov` on 2026-11-12.
- Source SHA-256: ACS `af9b1cad8178ebc85fa96a32b615a3f7a5f98ead7afabc68922614c68eb976ad`; boundaries `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`.

Census Bureau data and cartographic products are public-domain U.S. government works. Census asks users to cite the Bureau as the source.

## Calculation contract

The denominator is the civilian noninstitutionalized population in each selected B27001 age band. The numerator sums the corresponding “No health insurance coverage” estimates for male and female source categories.

The eight displayed age bands are under 19, 19–25, 26–34, 35–44, 45–54, 55–64, 65–74, and 75 or older. Their populations reconcile exactly to B27001 estimate 001, and their uninsured counts reconcile to the displayed all-ages uninsured count. Rows with negative sentinel values, missing components, uninsured counts above their denominators, or failed reconciliation are rejected rather than inferred.

## Limits

ACS figures are survey estimates with sampling and nonsampling error. Margins of error are not displayed. Coverage status is not a measure of health, care availability, affordability, adequacy, utilization, current enrollment, eligibility, or individual coverage. County averages hide household and neighborhood differences. The population universe excludes institutionalized people. Cartographic shapes are generalized and are not legal or service boundaries.

The runtime uses the dated same-origin compressed snapshot. It makes no Census API request, requires no key, and uses no Esri service. OpenStreetMap is used only as a contextual basemap.

## Rebuild

```bash
python3 maps/scripts/map76_build_snapshot.py \
  maps/data/map76-uninsured-by-age-2024.json.gz \
  acsdt5y2024-b27001.dat cb_2024_us_county_20m.zip
python3 maps/scripts/map76_build_snapshot.py --verify-only \
  maps/data/map76-uninsured-by-age-2024.json.gz
```

The canonical snapshot uses sorted keys, compact UTF-8 JSON, one trailing newline, gzip level 9, and gzip timestamp zero. Snapshot SHA-256: `78e15d4873f841bc76a224d90479870b3ce1a0195578bf479c509f29f6a756b7`.
