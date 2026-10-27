#!/usr/bin/env python3
"""Build Map 59's compact USACE NLD alignment snapshot.

The NLD public search page embeds its generalized nationwide alignment topology.
This script decodes that documented public-page payload, converts Web Mercator
coordinates to WGS 84, and assigns an approximate state only for filtering by
testing each line midpoint against the repository's Census county reference.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
from html.parser import HTMLParser
from pathlib import Path


class SearchMapProps(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.props: str | None = None

    def handle_starttag(self, tag, attrs) -> None:
        values = dict(attrs)
        if tag == "astro-island" and "SearchMap" in values.get("component-url", ""):
            self.props = values.get("props")


def decode_astro(value):
    if isinstance(value, list) and len(value) == 2 and isinstance(value[0], int):
        tag, payload = value
        if tag == 0:
            return {key: decode_astro(item) for key, item in payload.items()} if isinstance(payload, dict) else payload
        if tag == 1:
            return [decode_astro(item) for item in payload]
        if tag == 3:
            return payload
    if isinstance(value, dict):
        return {key: decode_astro(item) for key, item in value.items()}
    if isinstance(value, list):
        return [decode_astro(item) for item in value]
    return value


def mercator_to_lonlat(x: float, y: float) -> list[float]:
    radius = 6378137.0
    lon = math.degrees(x / radius)
    lat = math.degrees(2 * math.atan(math.exp(y / radius)) - math.pi / 2)
    return [round(lon, 5), round(lat, 5)]


def ring_contains(point, ring) -> bool:
    x, y = point
    inside = False
    j = len(ring) - 1
    for i, (xi, yi) in enumerate(ring):
        xj, yj = ring[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


def polygon_contains(point, coordinates) -> bool:
    return bool(coordinates and ring_contains(point, coordinates[0]) and not any(ring_contains(point, hole) for hole in coordinates[1:]))


def geometry_contains(point, geometry) -> bool:
    if geometry["type"] == "Polygon":
        return polygon_contains(point, geometry["coordinates"])
    return any(polygon_contains(point, polygon) for polygon in geometry["coordinates"])


def midpoint(line):
    return line[len(line) // 2]


def state_for(point, counties) -> str:
    x, y = point
    for minx, miny, maxx, maxy, state, geometry in counties:
        if minx <= x <= maxx and miny <= y <= maxy and geometry_contains(point, geometry):
            return state
    return "Other / unassigned"


def bounds(geometry):
    rings = geometry["coordinates"] if geometry["type"] == "Polygon" else [r for polygon in geometry["coordinates"] for r in polygon]
    points = [point for ring in rings for point in ring]
    return min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_html", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("counties", nargs="+", type=Path)
    args = parser.parse_args()

    parser_ = SearchMapProps()
    parser_.feed(args.source_html.read_text())
    if not parser_.props:
        raise ValueError("SearchMap Astro props not found")
    topology = decode_astro(json.loads(parser_.props))["mapFeatures"]
    obj = next(iter(topology["objects"].values()))
    scale, translate = topology["transform"]["scale"], topology["transform"]["translate"]

    county_index = []
    for path in args.counties:
        for feature in json.loads(path.read_text())["features"]:
            geometry = feature["geometry"]
            county_index.append((*bounds(geometry), feature["properties"]["state"], geometry))

    decoded_arcs = []
    for arc in topology["arcs"]:
        x = y = 0
        line = []
        for dx, dy in arc:
            x += dx
            y += dy
            line.append(mercator_to_lonlat(x * scale[0] + translate[0], y * scale[1] + translate[1]))
        decoded_arcs.append(line)

    codes = []
    states = []
    feature_count = 0
    for geometry in obj["geometries"]:
        arc_groups = geometry["arcs"] if geometry["type"] == "MultiLineString" else [geometry["arcs"]]
        lines = []
        for arc_group in arc_groups:
            line = []
            for index in arc_group:
                part = decoded_arcs[index] if index >= 0 else list(reversed(decoded_arcs[~index]))
                line.extend(part if not line else part[1:])
            if len(line) >= 2:
                lines.append(line)
        if not lines:
            continue
        longest = max(lines, key=len)
        code = geometry.get("properties", {}).get("code")
        codes.append(code)
        states.append(state_for(midpoint(longest), county_index))
        geometry.pop("properties", None)
        feature_count += 1

    payload = {
        "schema": "map59-usace-nld-public-alignment-v1",
        "source_retrieved_on": "2026-10-27",
        "feature_count": feature_count,
        "state_method": "line midpoint in Census 2025 20m county reference; display filter only",
        "codes": codes,
        "states": states,
        "topology": topology,
    }
    serialized = (json.dumps(payload, ensure_ascii=True, separators=(",", ":")) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    boundaries = [len(serialized) * index // 3 for index in range(4)]
    outputs = []
    for index in range(3):
        path = args.output.with_name(f"{args.output.name}.part{index + 1}-of-3.gz")
        path.write_bytes(gzip.compress(serialized[boundaries[index]:boundaries[index + 1]], compresslevel=9, mtime=0))
        outputs.append({"path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)})
    print(json.dumps({"outputs": outputs, "source_sha256": sha256(args.source_html),
                      "feature_count": feature_count}, indent=2))


if __name__ == "__main__":
    main()
