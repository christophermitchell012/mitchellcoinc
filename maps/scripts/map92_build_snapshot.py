#!/usr/bin/env python3
"""Build and verify Map 92's deterministic ACS county income-inequality snapshot."""
from __future__ import annotations
import argparse,csv,gzip,json,math,re
from pathlib import Path
from map87_build_snapshot import canonical_bytes,sha256

SCHEMA="map92-acs-income-inequality-v1"
COUNTY_ID=re.compile(r"^0500000US(\d{5})$")

def value(row:dict[str,str],field:str)->float|None:
    try: result=float(row[field])
    except (KeyError,TypeError,ValueError): return None
    return result if math.isfinite(result) and result>=0 else None

def read_table(path:Path)->dict[str,dict[str,str]]:
    rows={}
    with path.open(encoding="utf-8",newline="") as handle:
        for row in csv.DictReader(handle,delimiter="|"):
            match=COUNTY_ID.match(row.get("GEO_ID",""))
            if match: rows[match.group(1)]=row
    return rows

def read_geometry_snapshot(path:Path)->dict[str,dict]:
    document=json.loads(gzip.decompress(path.read_bytes()))
    features=document.get("counties",{}).get("features",[])
    return {f["properties"]["id"]:f for f in features}

def verify_snapshot(path:Path)->None:
    compressed=path.read_bytes(); raw=gzip.decompress(compressed); document=json.loads(raw)
    if raw!=canonical_bytes(document) or compressed!=gzip.compress(raw,compresslevel=9,mtime=0): raise SystemExit("snapshot is not canonical deterministic gzip")
    if document.get("schema")!=SCHEMA or document.get("source_year")!=2024: raise SystemExit("unexpected schema or source year")
    features=document.get("counties",{}).get("features",[])
    if len(features)!=document.get("county_count") or len(features)!=3222: raise SystemExit("unexpected county count")
    seen=set()
    for feature in features:
        p=feature.get("properties",{}); geoid=p.get("id"); estimate=p.get("gini_index"); moe=p.get("margin_of_error"); relative=p.get("relative_margin_of_error")
        if not isinstance(geoid,str) or len(geoid)!=5 or geoid in seen: raise SystemExit(f"invalid or duplicate GEOID: {geoid}")
        seen.add(geoid)
        if estimate is not None and (not isinstance(estimate,float) or not 0<=estimate<=1): raise SystemExit(f"invalid Gini estimate: {geoid}")
        if moe is not None and (not isinstance(moe,float) or moe<0): raise SystemExit(f"invalid margin: {geoid}")
        expected=round(moe*100/estimate,1) if estimate and moe is not None else None
        if relative!=expected or relative is not None and (not math.isfinite(relative) or relative<0): raise SystemExit(f"relative margin mismatch: {geoid}")
        if feature.get("geometry",{}).get("type") not in {"Polygon","MultiPolygon"}: raise SystemExit(f"invalid geometry: {geoid}")
    print(json.dumps({"verified":str(path),"bytes":len(compressed),"sha256":sha256(path),"counties":len(features)},indent=2))

def main()->None:
    parser=argparse.ArgumentParser(); parser.add_argument("--verify-only",action="store_true"); parser.add_argument("output",type=Path); parser.add_argument("inequality_table",type=Path,nargs="?"); parser.add_argument("geometry_snapshot",type=Path,nargs="?"); args=parser.parse_args()
    if args.verify_only: verify_snapshot(args.output); return
    if None in (args.inequality_table,args.geometry_snapshot): parser.error("inequality_table and geometry_snapshot are required")
    rows=read_table(args.inequality_table); geometries=read_geometry_snapshot(args.geometry_snapshot); features=[]
    for geoid in sorted(geometries):
        source=geometries[geoid]; old=source["properties"]; row=rows.get(geoid,{}); estimate=value(row,"B19083_E001"); moe=value(row,"B19083_M001"); relative=round(moe*100/estimate,1) if estimate and moe is not None else None
        props={"id":geoid,"name":old["name"],"state":old["state"],"abbr":old["abbr"],"gini_index":estimate,"margin_of_error":moe,"relative_margin_of_error":relative}
        features.append({"type":"Feature","properties":props,"geometry":source["geometry"]})
    document={"schema":SCHEMA,"source_year":2024,"source_vintage":"2020–2024 ACS 5-year","universe":"households","confidence_level":"90%","county_count":len(features),"counties":{"type":"FeatureCollection","features":features}}
    args.output.write_bytes(gzip.compress(canonical_bytes(document),compresslevel=9,mtime=0)); verify_snapshot(args.output)

if __name__=="__main__": main()
