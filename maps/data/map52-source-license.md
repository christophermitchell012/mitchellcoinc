# Map 52 source and use notes

## Source contract

Map 52 is a dated, same-origin summary of **USGS Data Report 1187**, *National shoreline change—Summary statistics of shoreline change from the 1800s to the 2010s for the coast of California*, and its associated data release (DOI `10.5066/P94J0K7Z`). The report was first posted January 16, 2024. It summarizes 19,063 long-term shoreline-change transects using shoreline positions from the mid-1800s through 2016.

The local JSON snapshot retains the three regional counts, net long-term linear-regression rates and reduced-sample uncertainty, erosional/accretional shares and mean rates, and the maximum erosion/accretion values and named locations reported in table 2. Positive rates mean accretion (shoreline advance); negative rates mean erosion (shoreline retreat). Values are meters per year. Confidence intervals are 90 percent confidence intervals.

Marker coordinates for named maximum-rate locations are approximate orientation points supplied by MitchellCo. They are not copied transect coordinates, parcel locations, hazard boundaries, or predictions. Regional center markers are interface anchors, not measurement locations.

## Rights and attribution

USGS marks the associated data release as CC0 1.0 Universal, and USGS materials are generally public domain unless otherwise noted. Attribution is retained because it is useful provenance.

- Report: https://pubs.usgs.gov/publication/dr1187
- Data release: https://doi.org/10.5066/P94J0K7Z
- DSAS method: https://www.usgs.gov/centers/whcmsc/science/digital-shoreline-analysis-system-dsas
- CC0 deed: https://creativecommons.org/publicdomain/zero/1.0/

## Limits

This map is historical regional context, not a live shoreline, forecast, survey, setback map, parcel analysis, engineering assessment, evacuation product, property valuation, or site-specific erosion estimate. Net regional averages can conceal local erosion and accretion. A rate with a confidence interval spanning zero is not statistically significant at the report's stated confidence level. Users should consult the USGS transect dataset and qualified local professionals for site decisions.
