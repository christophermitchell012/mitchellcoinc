#!/usr/bin/env python3
"""Build and verify Map 88's deterministic ACS county language snapshot."""
from __future__ import annotations
import argparse,gzip,json,math
from pathlib import Path
from map87_build_snapshot import STATE_NAMES,canonical_bytes,number,read_boundaries,read_table,sha256

SCHEMA="map88-acs-language-proficiency-v1"
METRICS=("language_other_than_english","limited_english","spanish_home","indo_european_home","asian_pacific_home","other_languages_home")

def verify_snapshot(path:Path)->None:
    compressed=path.read_bytes(); raw=gzip.decompress(compressed); document=json.loads(raw)
    if raw!=canonical_bytes(document) or compressed!=gzip.compress(raw,compresslevel=9,mtime=0): raise SystemExit("snapshot is not canonical deterministic gzip")
    if document.get("schema")!=SCHEMA or document.get("source_year")!=2024: raise SystemExit("unexpected schema or source year")
    features=document.get("counties",{}).get("features",[])
    if len(features)!=document.get("county_count") or len(features)<3200: raise SystemExit("unexpected county count")
    seen=set()
    for feature in features:
        p=feature.get("properties",{}); geoid=p.get("id"); total=p.get("population_age_5_plus")
        if not isinstance(geoid,str) or len(geoid)!=5 or geoid in seen: raise SystemExit(f"invalid or duplicate county GEOID: {geoid}")
        seen.add(geoid)
        counts=[p.get(k+"_count") for k in METRICS]
        if not isinstance(total,int) or total<0 or any(not isinstance(v,int) or v<0 for v in counts): raise SystemExit(f"invalid population counts: {geoid}")
        if p["english_only_count"]+p["language_other_than_english_count"]!=total: raise SystemExit(f"language categories do not partition population: {geoid}")
        if p["spanish_home_count"]+p["indo_european_home_count"]+p["asian_pacific_home_count"]+p["other_languages_home_count"]!=p["language_other_than_english_count"]: raise SystemExit(f"language groups do not partition non-English total: {geoid}")
        if p["limited_english_count"]>p["language_other_than_english_count"]: raise SystemExit(f"invalid English proficiency count: {geoid}")
        for k in METRICS:
            v=p.get(k)
            if v is not None and not (0<=v<=100 and math.isfinite(v)): raise SystemExit(f"invalid percentage: {geoid} {k}")
        if feature.get("geometry",{}).get("type") not in {"Polygon","MultiPolygon"}: raise SystemExit(f"invalid geometry: {geoid}")
    print(json.dumps({"verified":str(path),"bytes":len(compressed),"sha256":sha256(path),"counties":len(features)},indent=2))

def main()->None:
    parser=argparse.ArgumentParser(); parser.add_argument("--verify-only",action="store_true"); parser.add_argument("output",type=Path); parser.add_argument("language_table",type=Path,nargs="?"); parser.add_argument("county_boundaries",type=Path,nargs="?"); args=parser.parse_args()
    if args.verify_only: verify_snapshot(args.output); return
    if None in (args.language_table,args.county_boundaries): parser.error("language_table and county_boundaries are required when building")
    rows=read_table(args.language_table); boundaries=read_boundaries(args.county_boundaries); features=[]
    for geoid in sorted(set(rows)&set(boundaries)):
        row,(name,geometry)=rows[geoid],boundaries[geoid]; fields={i:number(row,f"C16001_E{i:03d}") for i in range(1,39)}
        if any(v is None for v in fields.values()): continue
        total=fields[1]; language_totals=list(range(3,39,3)); limited_fields=list(range(5,39,3))
        counts={"language_other_than_english":sum(fields[i] for i in language_totals),"limited_english":sum(fields[i] for i in limited_fields),"spanish_home":fields[3],"indo_european_home":sum(fields[i] for i in range(6,18,3)),"asian_pacific_home":sum(fields[i] for i in range(18,33,3)),"other_languages_home":sum(fields[i] for i in range(33,39,3))}
        if fields[2]+counts["language_other_than_english"]!=total: continue
        state_name,state_abbr=STATE_NAMES[geoid[:2]]; p={"id":geoid,"name":name,"state":state_name,"abbr":state_abbr,"population_age_5_plus":total,"english_only_count":fields[2]}
        for key,count in counts.items(): p[key+"_count"]=count; p[key+"_denominator"]=total; p[key]=round(count*100/total,1) if total else None
        features.append({"type":"Feature","properties":p,"geometry":geometry})
    document={"schema":SCHEMA,"source_year":2024,"source_vintage":"2020–2024 ACS 5-year","county_count":len(features),"counties":{"type":"FeatureCollection","features":features}}
    args.output.write_bytes(gzip.compress(canonical_bytes(document),compresslevel=9,mtime=0)); verify_snapshot(args.output)
if __name__=="__main__": main()
