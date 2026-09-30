#!/usr/bin/env python3
"""Verify deployed map HTML, local assets/data, and sitemap discovery."""
import concurrent.futures
import hashlib
import os
import time
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mitchellcoinc.com/maps/"
SHA = os.environ.get("GITHUB_SHA", "migration")

def fetch(url):
    req = Request(url + ("&" if "?" in url else "?") + "verify=" + SHA,
                  headers={"User-Agent": "MitchellCo-Deployment-Check/1.0"})
    with urlopen(req, timeout=30) as response:
        assert response.status == 200, (url, response.status)
        return response.read()

def verify_file(path):
    relative = path.relative_to(ROOT).as_posix()
    actual = fetch(BASE + relative)
    expected = path.read_bytes()
    assert hashlib.sha256(actual).digest() == hashlib.sha256(expected).digest(), relative
    return relative

def main():
    gallery = ROOT / "index.html"
    for attempt in range(20):
        try:
            verify_file(gallery)
            break
        except Exception as error:
            print(f"Waiting for deployed gallery ({attempt + 1}/20): {error}", flush=True)
            if attempt == 19:
                raise
            time.sleep(15)
    pages = [gallery, *sorted(ROOT.glob("[0-9][0-9]-*.html")),
             ROOT / "data-sources-licenses.html", ROOT / "earthdata-eula-policy.html"]
    assets = [p for folder in ("assets", "data") for p in (ROOT / folder).rglob("*")
              if p.is_file() and p.suffix != ".md"]
    files = pages + assets + [ROOT / "sitemap.xml", ROOT / "site.webmanifest"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        verified = list(pool.map(verify_file, files))
    sitemap = ET.fromstring(fetch("https://mitchellcoinc.com/sitemap.xml"))
    locs = {element.text for element in sitemap.iter() if element.tag.endswith("loc")}
    required = {BASE if p.name == "index.html" else BASE + p.name for p in pages}
    assert required <= locs, f"Main sitemap missing: {required - locs}"
    assert "https://mitchellcoinc.com/blog/" in locs, "Main sitemap omits blog"
    robots = fetch("https://mitchellcoinc.com/robots.txt").decode()
    assert "Sitemap: https://mitchellcoinc.com/sitemap.xml" in robots
    assert "Sitemap: " + BASE + "sitemap.xml" in robots
    print(f"PASS: {len(pages) - 3} numbered maps, {len(pages)} HTML pages, "
          f"{len(verified)} deployed files match repository bytes; both sitemaps and robots verified")

if __name__ == "__main__":
    main()
