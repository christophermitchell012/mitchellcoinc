#!/usr/bin/env python3
"""Build map sitemap and Jekyll date manifest from page metadata.

When publishing a map or significantly changing its content, links, or data,
set its last-modified meta tag to the actual change timestamp (ISO 8601).
Then run this script to update both sitemaps\' shared date source.
Do not advance dates for a rebuild or merely to make dates distinct.
"""

import argparse
import json
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mitchellcoinc.com/maps/"


class GalleryLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.maps = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "a" and "maprow" in values.get("class", "").split():
            self.maps.append(values["href"])


class ModifiedDate(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("name") == "last-modified":
            self.values.append(attrs.get("content", ""))


def page_dates():
    dates = {}
    for page in sorted(ROOT.glob("*.html")):
        if page.name == "404.html":
            continue
        parser = ModifiedDate()
        parser.feed(page.read_text())
        if len(parser.values) != 1:
            raise ValueError(f"{page.name}: require exactly one last-modified meta tag")
        value = parser.values[0]
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None or parsed > datetime.now(timezone.utc):
            raise ValueError(f"{page.name}: require a non-future timestamp with timezone")
        dates["/maps/" + page.name] = value
    return dates


def build():
    parser = GalleryLinks()
    parser.feed((ROOT / "index.html").read_text())
    maps = parser.maps
    files = sorted(p.name for p in ROOT.glob("[0-9][0-9]-*.html"))
    if len(maps) != len(set(maps)) or sorted(maps) != files:
        raise ValueError("Gallery links and numbered map files differ")
    urls = [BASE] + [BASE + name for name in maps]
    urls += [BASE + name for name in ("data-sources-licenses.html", "earthdata-eula-policy.html")]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    dates = page_dates()
    for url in urls:
        name = url.removeprefix(BASE) or "index.html"
        modified = dates["/maps/" + name]
        lines.append(f"  <url><loc>{escape(url)}</loc><lastmod>{escape(modified)}</lastmod></url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--check", action="store_true", help="Fail if the committed sitemap is stale")
    options = args.parse_args()
    output = build()
    destination = ROOT / "sitemap.xml"
    manifest = ROOT.parent / "_data" / "map_lastmod.json"
    manifest_output = json.dumps(page_dates(), indent=2) + "\n"
    if options.check:
        if not manifest.exists() or manifest.read_text() != manifest_output:
            raise SystemExit("_data/map_lastmod.json is stale; run maps/scripts/build_sitemap.py")
        if destination.read_text() != output:
            raise SystemExit("sitemap.xml is stale; run python scripts/build_sitemap.py")
        print("sitemap.xml matches the gallery and published pages")
    else:
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(manifest_output)
        destination.write_text(output)
        print(f"Wrote {destination}")
