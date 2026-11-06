#!/usr/bin/env python3
"""Validate the built site (standard library only). Exit code 1 on any error.

Checks: lang, title, description, canonical, hreflang reciprocity and x-default,
Open Graph, JSON-LD parsing and required fields, one h1 and no skipped heading
levels, img alt/width/height, internal links and fragments, sitemap.xml,
robots.txt, 404 page, app-ads.txt.

Usage: python3 site/validate.py [--dist dist] [--base-url https://moris94.github.io] [--external]
"""
from __future__ import annotations

import argparse
import json
import re
import pathlib
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = ""
        self._in_title = False
        self._in_ld = False
        self._ld_buf = ""
        self.meta: dict[str, str] = {}
        self.links: list[dict] = []
        self.hrefs: list[str] = []
        self.ids: set[str] = set()
        self.headings: list[int] = []
        self.imgs: list[dict] = []
        self.jsonld: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link":
            self.links.append(a)
        elif tag == "a" and "href" in a:
            self.hrefs.append(a["href"])
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append(int(tag[1]))
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
            self._ld_buf = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_ld:
            self._in_ld = False
            self.jsonld.append(self._ld_buf)

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_ld:
            self._ld_buf += data


def url_to_file(dist: pathlib.Path, base: str, url: str) -> pathlib.Path | None:
    if not url.startswith(base + "/") and url != base:
        return None
    path = urllib.parse.urlparse(url).path or "/"
    return dist / (path.lstrip("/") + "index.html" if path.endswith("/") else path.lstrip("/"))


def file_to_url(dist: pathlib.Path, base: str, f: pathlib.Path) -> str:
    rel = f.relative_to(dist).as_posix()
    if rel.endswith("index.html"):
        rel = rel[: -len("index.html")]
    return base + "/" + rel


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(pathlib.Path(__file__).resolve().parents[1] / "dist"))
    ap.add_argument("--base-url", default="https://moris94.github.io")
    ap.add_argument("--external", action="store_true", help="also request external links (App Store, policies)")
    args = ap.parse_args()
    dist = pathlib.Path(args.dist)
    base = args.base_url.rstrip("/")

    pages: dict[pathlib.Path, Page] = {}
    for f in sorted(dist.rglob("*.html")):
        p = Page()
        p.feed(f.read_text(encoding="utf-8"))
        pages[f] = p

    titles: dict[str, str] = {}
    descs: dict[str, str] = {}
    canon_of: dict[pathlib.Path, str] = {}
    external: set[str] = set()

    for f, p in pages.items():
        name = f.relative_to(dist).as_posix()
        noindex = "noindex" in p.meta.get("robots", "")
        if p.lang not in ("ja", "en"):
            err(f"{name}: html lang missing or unexpected ({p.lang})")
        if not p.title.strip():
            err(f"{name}: empty <title>")
        if not p.meta.get("description"):
            err(f"{name}: missing meta description")
        if "viewport" not in p.meta:
            err(f"{name}: missing viewport")
        if not any(l.get("rel") == "icon" for l in p.links):
            err(f"{name}: missing favicon")
        if p.headings.count(1) != 1:
            err(f"{name}: expected exactly one h1, found {p.headings.count(1)}")
        prev = 0
        for h in p.headings:
            if h > prev + 1:
                err(f"{name}: heading level skips from h{prev} to h{h}")
            prev = h
        for img in p.imgs:
            if "alt" not in img:
                err(f"{name}: <img src={img.get('src')}> has no alt attribute")
            if not (img.get("width") and img.get("height")):
                err(f"{name}: <img src={img.get('src')}> lacks width/height")
            srcs = [img.get("src", "")] + [c.strip().split(" ")[0] for c in img.get("srcset", "").split(",") if c.strip()]
            for src in srcs:
                if src.startswith("/") and not (dist / src.lstrip("/").split("?")[0]).exists():
                    err(f"{name}: image not found {src}")
        for l in p.links:
            href = l.get("href", "")
            if href.startswith("/") and not (dist / href.lstrip("/").split("?")[0]).exists():
                err(f"{name}: linked asset not found {href}")
        for key in ("og:title", "og:description", "og:url", "og:image", "twitter:card"):
            if key not in p.meta:
                err(f"{name}: missing {key}")
        og_img = p.meta.get("og:image", "")
        if og_img and url_to_file(dist, base, og_img) and not url_to_file(dist, base, og_img).exists():
            err(f"{name}: og:image file not found {og_img}")

        if f.name == "404.html":
            if not noindex:
                err("404.html should be noindex")
        if not noindex:
            canon = [l["href"] for l in p.links if l.get("rel") == "canonical"]
            expected = file_to_url(dist, base, f)
            if canon != [expected]:
                err(f"{name}: canonical {canon} != {expected}")
            canon_of[f] = expected
            if p.meta.get("og:url") != expected:
                err(f"{name}: og:url {p.meta.get('og:url')} != canonical")
            if p.title in titles:
                err(f"{name}: duplicate title with {titles[p.title]}")
            titles[p.title] = name
            d = p.meta.get("description", "")
            if d in descs:
                err(f"{name}: duplicate description with {descs[d]}")
            descs[d] = name
            if len(p.title) > 90:
                warnings.append(f"{name}: long title ({len(p.title)} chars)")
            if not p.jsonld:
                err(f"{name}: no JSON-LD")
        for raw in p.jsonld:
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as e:
                err(f"{name}: JSON-LD parse error {e}")
                continue
            if data.get("@context") != "https://schema.org":
                err(f"{name}: JSON-LD @context")
            for u in re.findall(r'"(https?://[^"]+/static/[^"]+)"', raw):
                tf = url_to_file(dist, base, u)
                if tf and not tf.exists():
                    err(f"{name}: JSON-LD asset not found {u}")
            for node in data.get("@graph", [data]):
                if node.get("@type") == "MobileApplication":
                    for k in ("name", "operatingSystem", "applicationCategory", "offers", "url", "installUrl"):
                        if k not in node:
                            err(f"{name}: MobileApplication missing {k}")
                    for o in node.get("offers", []):
                        if "price" not in o or "priceCurrency" not in o:
                            err(f"{name}: Offer missing price/priceCurrency")
                    for k in ("aggregateRating", "review"):
                        if k in node:
                            err(f"{name}: {k} present; the apps have no ratings to show")
                    if node.get("url") != canon_of.get(f):
                        err(f"{name}: JSON-LD url differs from canonical")
                    if node.get("installUrl") not in p.hrefs:
                        err(f"{name}: installUrl is not linked visibly on the page")

        for href in p.hrefs:
            if href.startswith("mailto:"):
                continue
            if href.startswith("http"):
                external.add(href)
                if href.startswith(base):
                    err(f"{name}: internal link written as absolute URL {href}")
                continue
            target, _, frag = href.partition("#")
            if not target:
                tf = f
            else:
                abs_path = urllib.parse.urljoin("/" + f.relative_to(dist).as_posix(), target)
                tf = dist / (abs_path.lstrip("/") + "index.html" if abs_path.endswith("/") else abs_path.lstrip("/"))
            if not tf.exists():
                err(f"{name}: broken internal link {href}")
            elif frag and frag not in pages.get(tf, Page()).ids:
                err(f"{name}: missing fragment #{frag} in {href}")

    # hreflang reciprocity
    for f, p in pages.items():
        if f not in canon_of:
            continue
        alts = {l["hreflang"]: l["href"] for l in p.links if l.get("rel") == "alternate" and "hreflang" in l}
        if not alts:
            err(f"{f.relative_to(dist)}: no hreflang")
            continue
        if "x-default" not in alts:
            err(f"{f.relative_to(dist)}: no x-default")
        if alts.get(p.lang) != canon_of[f]:
            err(f"{f.relative_to(dist)}: hreflang for its own language is not self-referencing")
        for lang, href in alts.items():
            tf = url_to_file(dist, base, href)
            if not tf or not tf.exists():
                err(f"{f.relative_to(dist)}: hreflang {lang} target missing {href}")
                continue
            back = {l["hreflang"]: l["href"] for l in pages[tf].links if l.get("rel") == "alternate" and "hreflang" in l}
            if back.get(p.lang) != canon_of[f]:
                err(f"{f.relative_to(dist)}: hreflang {lang} target does not link back")

    # sitemap
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9", "x": "http://www.w3.org/1999/xhtml"}
    try:
        tree = ET.parse(dist / "sitemap.xml")
        locs = [u.find("s:loc", ns).text for u in tree.getroot().findall("s:url", ns)]
        if len(locs) != len(set(locs)):
            err("sitemap.xml has duplicate URLs")
        for link in tree.getroot().iter("{http://www.w3.org/1999/xhtml}link"):
            if link.get("href") not in set(canon_of.values()):
                err(f"sitemap.xml alternate is not an indexable page: {link.get('href')}")
        if set(locs) != set(canon_of.values()):
            missing = set(canon_of.values()) - set(locs)
            extra = set(locs) - set(canon_of.values())
            err(f"sitemap.xml mismatch: missing {sorted(missing)} extra {sorted(extra)}")
    except (ET.ParseError, FileNotFoundError, AttributeError) as e:
        err(f"sitemap.xml invalid: {e}")

    robots = (dist / "robots.txt").read_text(encoding="utf-8") if (dist / "robots.txt").exists() else ""
    if f"Sitemap: {base}/sitemap.xml" not in robots:
        err("robots.txt does not point to the sitemap")
    if re.search(r"^Disallow:\s*/\s*$", robots, re.M):
        err("robots.txt blocks the whole site")
    for must in ("404.html", "app-ads.txt", ".nojekyll"):
        if not (dist / must).exists():
            err(f"{must} missing")

    if args.external:
        for url in sorted(external):
            try:
                req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 site-validator"})
                with urllib.request.urlopen(req, timeout=30) as r:
                    if r.status >= 400:
                        err(f"external link {url} -> {r.status}")
            except Exception as e:  # noqa: BLE001
                if "429" in str(e):
                    warnings.append(f"external link rate-limited: {url}")
                else:
                    err(f"external link {url} -> {e}")

    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    print(f"checked {len(pages)} HTML files, {len(canon_of)} indexable; {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
