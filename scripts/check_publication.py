#!/usr/bin/env python3
"""Check post links and the cross-site discovery paths before publication."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"
MAPS = "https://christophermitchell012.github.io/maps/"


def main():
    posts = sorted(POSTS.glob("*.md"))
    routes = {"/", "/blog/"}
    for post in posts:
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}-.+\.md", post.name), post
        route = f"/blog/{post.name[:10].replace('-', '/')}/{post.stem[11:]}/"
        routes.add(route)

    for post in posts:
        for target in re.findall(r"\]\((/[^)\s]+)", post.read_text()):
            path = target.split("#", 1)[0].split("?", 1)[0]
            assert path in routes or (not path.startswith("/blog/") and
                                      (ROOT / path.lstrip("/")).is_file()), (
                f"Broken internal link in {post.name}: {target}"
            )

    for page in (ROOT / "index.html", ROOT / "blog/index.html", ROOT / "_layouts/post.html"):
        assert MAPS in page.read_text(), f"Map collection link missing: {page}"
    sitemap = (ROOT / "sitemap.xml").read_text()
    assert "{% for post in site.posts %}" in sitemap, "Sitemap omits the post collection"
    assert "{{ post.url }}" in sitemap, "Post URL missing in sitemap template"
    print(f"Validated {len(posts)} posts, internal links, and blog-to-map navigation")


if __name__ == "__main__":
    main()
