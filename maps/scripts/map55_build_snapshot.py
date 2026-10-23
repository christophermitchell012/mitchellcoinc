#!/usr/bin/env python3
"""Build Map 55's dated rail raster and compact state summary from BTS NARN."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import geopandas as gpd
from PIL import Image, ImageDraw

WORLD = 20_037_508.342789244
SIZE = 8192


def rail_class(row) -> str:
    if row.get("PASSNGR") not in (None, "", "None"):
        return "passenger"
    if row.get("STRACNET") not in (None, "", "None"):
        return "stracnet"
    return "other"


def pixel(x: float, y: float) -> tuple[int, int]:
    return (round((x + WORLD) / (2 * WORLD) * SIZE), round((WORLD - y) / (2 * WORLD) * SIZE))


def line_parts(geometry):
    if geometry.geom_type == "LineString":
        yield geometry
    elif geometry.geom_type == "MultiLineString":
        yield from geometry.geoms


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("gdb", type=Path, help="Extracted BTS NARN file geodatabase")
    parser.add_argument("png", type=Path, help="Destination transparent Web Mercator PNG")
    parser.add_argument("summary", type=Path, help="Destination state-summary JSON")
    args = parser.parse_args()

    layers = gpd.list_layers(args.gdb)
    layer = next(name for name in layers.name if "lines" in name.lower())
    rails = gpd.read_file(
        args.gdb,
        layer=layer,
        columns=["COUNTRY", "STATEAB", "PASSNGR", "STRACNET", "MILES"],
    )
    rails = rails.loc[rails["COUNTRY"].eq("US") & rails.geometry.notna()].copy()
    rails["class"] = rails.apply(rail_class, axis=1)
    rails["geometry"] = rails.geometry.simplify(500, preserve_topology=False)

    image = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    styles = {
        "other": ((201, 216, 222, 205), 1),
        "stracnet": ((255, 191, 105, 235), 2),
        "passenger": ((87, 212, 255, 245), 2),
    }
    for category in ("other", "stracnet", "passenger"):
        color, width = styles[category]
        for geometry in rails.loc[rails["class"].eq(category), "geometry"]:
            for part in line_parts(geometry):
                coords = [pixel(x, y) for x, y in part.coords]
                if len(coords) > 1:
                    draw.line(coords, fill=color, width=width)

    args.png.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.png, optimize=True)

    rails4326 = rails.to_crs(4326)
    states = []
    for state, group in rails4326.groupby("STATEAB"):
        bounds = [round(float(v), 5) for v in group.total_bounds]
        counts = group.groupby("class").size().to_dict()
        miles = group.groupby("class")["MILES"].sum().to_dict()
        states.append({
            "state": state,
            "bounds": bounds,
            "segments": {key: int(counts.get(key, 0)) for key in styles},
            "source_miles": {key: round(float(miles.get(key, 0)), 1) for key in styles},
        })
    payload = {
        "source": "BTS/FRA North American Rail Network",
        "source_vintage": "2024-10-16",
        "render": "Transparent 8192 px Web Mercator overview; line geometry simplified to 500 m before drawing.",
        "source_segment_count": int(len(rails)),
        "source_miles_sum": round(float(rails["MILES"].fillna(0).sum()), 1),
        "states": states,
    }
    args.summary.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False) + "\n")
    print(json.dumps({"png": str(args.png), "png_bytes": args.png.stat().st_size,
                      "summary": str(args.summary), "summary_bytes": args.summary.stat().st_size,
                      **{key: payload[key] for key in ("source_vintage", "source_segment_count", "source_miles_sum")}}, indent=2))


if __name__ == "__main__":
    main()
