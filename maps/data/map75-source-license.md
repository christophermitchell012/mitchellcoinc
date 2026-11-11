# Map 75 source, calculation, and reuse notes

## Scope

Map 75 compares the usual means of transportation to work reported for workers age 16 or older in 3,222 counties or county equivalents. It uses the U.S. Census Bureau 2020–2024 American Community Survey five-year table B08301 and 2024 1:20,000,000 cartographic county boundaries.

## Sources and acquisition

- ACS table-based summary file: `acsdt5y2024-b08301.dat`
- County boundaries: `cb_2024_us_county_20m.zip`
- Downloaded from `www2.census.gov` on 2026-11-11.
- Source SHA-256: ACS `552b24c135b6e7c566910914a861cda6fc798ba0cd47801b1eb64295a128c2ee`; boundaries `c9a54fd95422436b8822e0b070a45a9bc3de08eb13f943cdba66e7a9c2a135ff`.

Census Bureau data and cartographic products are public-domain U.S. government works. Census asks users to cite the Bureau as the source.

## Calculation contract

The denominator is B08301 estimate 001: workers age 16 or older. The map preserves counts and calculates one-decimal percentages for:

- Drove alone: estimate 003.
- Carpooled: estimate 004.
- Public transportation: estimate 010.
- Walked: estimate 019.
- Bicycle: estimate 018.
- Worked from home: estimate 021.
- Taxi or ride-hailing, motorcycle, or other means: estimates 016 + 017 + 020.

These seven groups are mutually exclusive and reconcile exactly to the table total for every retained county. Rows with missing or negative sentinel values or a failed reconciliation are rejected rather than estimated.

## Limits

ACS figures are survey estimates with sampling and nonsampling error. Margins of error are not displayed. The data describe usual means of transportation to work, not every trip or every remote-work day, and do not measure traffic, congestion, commute time, emissions, road safety, employment status, transit quality, or service availability. County averages hide local and individual differences. Cartographic shapes are generalized and are not legal or service boundaries.

The runtime uses the dated same-origin compressed snapshot. It makes no Census API request, requires no key, and uses no Esri service. OpenStreetMap is used only as a contextual basemap.

## Rebuild

```bash
python3 maps/scripts/map75_build_snapshot.py \
  maps/data/map75-commute-mode-2024.json.gz \
  acsdt5y2024-b08301.dat cb_2024_us_county_20m.zip
python3 maps/scripts/map75_build_snapshot.py --verify-only \
  maps/data/map75-commute-mode-2024.json.gz
```

The canonical snapshot uses sorted keys, compact UTF-8 JSON, one trailing newline, gzip level 9, and gzip timestamp zero. Snapshot SHA-256: `20eec7fea03515d2d041cbb23a61e3254f231f7dfcff9c0cb47f78fc4c2958d5`.
