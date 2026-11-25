#!/usr/bin/env python3
"""Build and verify Map 89's deterministic ACS county income snapshot."""
from __future__ import annotations
import argparse,gzip,json,math
from pathlib import Path
from map87_build_snapshot import STATE_NAMES,canonical_bytes,number,read_boundaries,read_table,sha256

SCHEMA="map89-acs-median-household-income-v1"

def verify_snapshot(path:Path)->None:
    compressed=path.read_bytes(); raw=gzip.decompress(compressed); document=json.loads(raw)
    if raw!=canonical_bytes(document) or compressed!=gzip.compress(raw,compresslevel=9,mtime=0): raise SystemExit("snapshot is not canonical deterministic gzip")
    if document.get("schema")!=SCHEMA or document.get("source_year")!=2024: raise SystemExit("unexpected schema or source year")
    features=document.get("counties",{}).get("features",[])
    if len(features)!=document.get("county_count") or len(features)!=3222: raise SystemExit("unexpected county count")
    seen=set()
    for feature in features:
        p=feature.get("properties",{}); geoid=p.get("id"); estimate=p.get("median_household_income"); moe=p.get("margin_of_error"); relative=p.get("relative_margin_of_error")
        if not isinstance(geoid,str) or len(geoid)!=5 or geoid in seen: raise SystemExit(f"invalid or duplicate county GEOID: {geoid}")
        seen.add(geoid)
        if estimate is not None and (not isinstance(estimate,int) or estimate<0): raise SystemExit(f"invalid estimate: {geoid}")
        if moe is not None and (not isinstance(moe,int) or moe<0): raise SystemExit(f"invalid margin of error: {geoid}")
        if relative is not None and (not math.isfinite(relative) or relative<0): raise SystemExit(f"invalid relative margin of error: {geoid}")
        expected=round(moe*100/estimate,1) if estimate and moe is not None else None
        if relative!=expected: raise SystemExit(f"relative margin mismatch: {geoid}")
        if feature.get("geometry",{}).get("type") not in {"Polygon","MultiPolygon"}: raise SystemExit(f"invalid geometry: {geoid}")
    print(json.dumps({"verified":str(path),"bytes":len(compressed),"sha256":sha256(path),"counties":len(features)},indent=2))

def main()->None:
    parser=argparse.ArgumentParser(); parser.add_argument("--verify-only",action="store_true"); parser.add_argument("output",type=Path); parser.add_argument("income_table",type=Path,nargs="?"); parser.add_argument("county_boundaries",type=Path,nargs="?"); args=parser.parse_args()
    if args.verify_only: verify_snapshot(args.output); return
    if None in (args.income_table,args.county_boundaries): parser.error("income_table and county_boundaries are required when building")
    rows=read_table(args.income_table); boundaries=read_boundaries(args.county_boundaries); features=[]
    for geoid in sorted(boundaries):
        row=rows.get(geoid,{}); name,geometry=boundaries[geoid]; estimate=number(row,"B19013_E001"); moe=number(row,"B19013_M001")
        state_name,state_abbr=STATE_NAMES[geoid[:2]]; relative=round(moe*100/estimate,1) if estimate and moe is not None else None
        p={"id":geoid,"name":name,"state":state_name,"abbr":state_abbr,"median_household_income":estimate,"margin_of_error":moe,"relative_margin_of_error":relative}
        features.append({"type":"Feature","properties":p,"geometry":geometry})
    document={"schema":SCHEMA,"source_year":2024,"source_vintage":"2020–2024 ACS 5-year","dollar_basis":"2024 inflation-adjusted dollars","confidence_level":"90%","county_count":len(features),"counties":{"type":"FeatureCollection","features":features}}
    args.output.write_bytes(gzip.compress(canonical_bytes(document),compresslevel=9,mtime=0)); verify_snapshot(args.output)
if __name__=="__main__": main()
