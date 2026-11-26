#!/usr/bin/env python3
"""Build and verify Map 90's deterministic ACS county rent snapshot."""
from __future__ import annotations
import argparse,gzip,json,math
from pathlib import Path
from map87_build_snapshot import STATE_NAMES,canonical_bytes,number,read_boundaries,read_table,sha256
SCHEMA="map90-acs-median-gross-rent-v1"
def verify_snapshot(path:Path)->None:
    compressed=path.read_bytes();raw=gzip.decompress(compressed);document=json.loads(raw)
    if raw!=canonical_bytes(document) or compressed!=gzip.compress(raw,compresslevel=9,mtime=0):raise SystemExit("snapshot is not canonical deterministic gzip")
    if document.get("schema")!=SCHEMA or document.get("source_year")!=2024:raise SystemExit("unexpected schema or source year")
    features=document.get("counties",{}).get("features",[])
    if len(features)!=document.get("county_count") or len(features)!=3222:raise SystemExit("unexpected county count")
    seen=set()
    for f in features:
        p=f.get("properties",{});g=p.get("id");estimate=p.get("median_gross_rent");moe=p.get("margin_of_error");relative=p.get("relative_margin_of_error")
        if not isinstance(g,str) or len(g)!=5 or g in seen:raise SystemExit(f"invalid or duplicate GEOID: {g}")
        seen.add(g)
        if estimate is not None and (not isinstance(estimate,int) or estimate<0):raise SystemExit(f"invalid estimate: {g}")
        if moe is not None and (not isinstance(moe,int) or moe<0):raise SystemExit(f"invalid margin: {g}")
        expected=round(moe*100/estimate,1) if estimate and moe is not None else None
        if relative!=expected or relative is not None and (not math.isfinite(relative) or relative<0):raise SystemExit(f"relative margin mismatch: {g}")
        if f.get("geometry",{}).get("type") not in {"Polygon","MultiPolygon"}:raise SystemExit(f"invalid geometry: {g}")
    print(json.dumps({"verified":str(path),"bytes":len(compressed),"sha256":sha256(path),"counties":len(features)},indent=2))
def main()->None:
    parser=argparse.ArgumentParser();parser.add_argument("--verify-only",action="store_true");parser.add_argument("output",type=Path);parser.add_argument("rent_table",type=Path,nargs="?");parser.add_argument("county_boundaries",type=Path,nargs="?");args=parser.parse_args()
    if args.verify_only:verify_snapshot(args.output);return
    if None in (args.rent_table,args.county_boundaries):parser.error("rent_table and county_boundaries are required")
    rows=read_table(args.rent_table);boundaries=read_boundaries(args.county_boundaries);features=[]
    for geoid in sorted(boundaries):
        row=rows.get(geoid,{});name,geometry=boundaries[geoid];estimate=number(row,"B25064_E001");moe=number(row,"B25064_M001");state_name,state_abbr=STATE_NAMES[geoid[:2]];relative=round(moe*100/estimate,1) if estimate and moe is not None else None
        p={"id":geoid,"name":name,"state":state_name,"abbr":state_abbr,"median_gross_rent":estimate,"margin_of_error":moe,"relative_margin_of_error":relative};features.append({"type":"Feature","properties":p,"geometry":geometry})
    document={"schema":SCHEMA,"source_year":2024,"source_vintage":"2020–2024 ACS 5-year","dollar_basis":"2024 inflation-adjusted dollars","confidence_level":"90%","county_count":len(features),"counties":{"type":"FeatureCollection","features":features}}
    args.output.write_bytes(gzip.compress(canonical_bytes(document),compresslevel=9,mtime=0));verify_snapshot(args.output)
if __name__=="__main__":main()
