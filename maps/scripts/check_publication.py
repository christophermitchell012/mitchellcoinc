#!/usr/bin/env python3
"""Check map discovery, canonical metadata, and same-origin navigation."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
from xml.etree import ElementTree

from build_sitemap import BASE, ROOT, build


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.canonical = []
        self.description = []
        self.title = []
        self.metas = []
        self.ids = set()
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "a" and "href" in values:
            self.links.append(values["href"])
        if "id" in values:
            self.ids.add(values["id"])
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical.append(values.get("href"))
        if tag == "meta" and values.get("name") == "description":
            self.description.append(values.get("content"))
        if tag == "meta":
            self.metas.append(values)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)


def main():
    assert (ROOT / "sitemap.xml").read_text() == build(), "Sitemap is stale"
    listed = {node.text for node in ElementTree.parse(ROOT / "sitemap.xml").iter()
              if node.tag.endswith("loc")}
    files = [ROOT / "index.html", *sorted(ROOT.glob("[0-9][0-9]-*.html"))]
    expected = {BASE if p.name == "index.html" else BASE + p.name for p in files}
    expected.update(BASE + name for name in ("data-sources-licenses.html", "earthdata-eula-policy.html"))
    assert listed == expected, "Sitemap differs from published pages"
    pages = {}
    for file in files:
        page = Page()
        page.feed(file.read_text())
        pages[file.name] = page
        url = BASE if file.name == "index.html" else BASE + file.name
        assert page.canonical == [url], f"Canonical URL missing or incorrect: {file}"
        assert page.description and page.description[0], f"Description missing: {file}"
        if file.name != "index.html":
            assert "index.html" in page.links, f"Gallery link missing: {file}"
        assert "https://mitchellcoinc.com/blog/" in page.links, f"Blog link missing: {file}"
        for href in page.links:
            resolved = urlparse(urljoin(url, href))
            if resolved.netloc != urlparse(BASE).netloc or not resolved.path.startswith("/maps/"):
                continue
            target = unquote(resolved.path.removeprefix("/maps/")) or "index.html"
            assert (ROOT / target).is_file(), f"Broken local link in {file}: {href}"
            if resolved.fragment and target in pages:
                assert resolved.fragment in pages[target].ids, f"Missing anchor in {file}: {href}"
    latest = files[-1]
    page = pages[latest.name]
    title = "".join(page.title).strip()
    meta_name = {m.get("name"): m.get("content") for m in page.metas if m.get("name")}
    meta_prop = {m.get("property"): m.get("content") for m in page.metas if m.get("property")}
    url = BASE + latest.name
    assert title and meta_name.get("description"), f"SEO title/description missing: {latest}"
    assert meta_name.get("robots", "").replace(" ", "") == "index,follow", f"Robots metadata missing: {latest}"
    assert meta_name.get("author") == "MitchellCo Inc.", f"Author metadata missing: {latest}"
    assert meta_prop.get("article:published_time"), f"Publication timestamp missing: {latest}"
    assert meta_prop.get("og:type") == "website" and meta_prop.get("og:site_name"), f"Open Graph identity missing: {latest}"
    assert meta_prop.get("og:title") == title and meta_prop.get("og:description") == meta_name["description"], f"Open Graph text mismatch: {latest}"
    assert meta_prop.get("og:url") == url, f"Open Graph URL mismatch: {latest}"
    assert meta_name.get("twitter:card") == "summary", f"Twitter card missing: {latest}"
    assert meta_name.get("twitter:title") == title and meta_name.get("twitter:description") == meta_name["description"], f"Twitter metadata mismatch: {latest}"
    print(f"Validated {len(files)} map pages, local links, canonicals, and sitemap")


if __name__ == "__main__":
    main()
