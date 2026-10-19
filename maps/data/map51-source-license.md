# Map 51 source and use notes

## Product

Map 51 displays two official NOAA Climate Prediction Center (CPC) global land-surface monitoring images:

- Global soil-moisture percentile: `https://www.cpc.ncep.noaa.gov/products/Drought/leaky/leaky/smp/Global_smp.png`
- Current global soil-moisture anomaly: `https://www.cpc.ncep.noaa.gov/soilmst/glb_d/curr.w.a_gl.gif`

The browser requests one selected image at a time directly from NOAA CPC. No account, API key, token, Esri service, proxy, or background polling is used.

## Method

CPC describes the product as a one-layer leaky-bucket hydrological model driven by observed global precipitation and surface-air temperature on a 0.5° grid. The model uses spatially constant parameters, including a 760 mm maximum water-holding capacity. CPC defines percentile against the 1979–2019 modeled soil-moisture record and anomaly as departure from climatology.

Official documentation:

- https://www.cpc.ncep.noaa.gov/products/Drought/leaky/
- https://www.cpc.ncep.noaa.gov/products/Drought/leaky/smp/
- https://www.cpc.ncep.noaa.gov/products/Soilmst_Monitoring/introduction.shtml

## Interpretation limits

The page preserves the official raster, embedded valid date, legend and units. It does not sample pixels, interpolate the 0.5° grid, or align the graphic to a parcel basemap. Values are modeled land-surface estimates, not in-ground sensor readings. The map does not infer a drought declaration, flash-drought onset, crop loss, wildfire ignition, water availability, cause, forecast, property condition, safety condition or regulatory status.

NOAA's own documentation notes limitations associated with real-time station inputs, spatial analysis near gradients and boundaries, and the model's spatially constant parameters. Visitors should consult local observations and official drought products before making decisions.

## Attribution and reuse

Source: NOAA/NWS Climate Prediction Center, Global Land Surface Monitor and Prediction. U.S. federal government source material is presented with source attribution and links to the original products. MitchellCo's interface and explanatory text are © 2026 MitchellCo Inc.
