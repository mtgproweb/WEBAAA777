#!/usr/bin/env python3
"""Validador simple para Credisnet v4: sitemap = páginas, enlaces internos válidos."""
import re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/"docs"
pages=sorted(DOCS.rglob("index.html"))
sitemap=(DOCS/"sitemap.xml").read_text(encoding="utf-8")
urls=set(re.findall(r"<loc>([^<]+)</loc>", sitemap))
page_urls=set()
for p in pages:
    rel=p.parent.relative_to(DOCS)
    page_urls.add("https://www.credisnet.com.ar/" + ("" if str(rel)=="." else str(rel)+"/"))
assert urls==page_urls, f"sitemap != páginas: {urls ^ page_urls}"
for p in pages:
    t=p.read_text(encoding="utf-8")
    assert re.search(r"<title>([^<]+)</title>", t), p
    assert re.search(r'name="description" content="[^"]+"', t), p
    for href in re.findall(r'href="([^"]+)"', t):
        if href.startswith(('http','tel:','mailto:','#','assets/','../assets/')): continue
        if href in ('', '.', './', '../'): continue
        fp=(p.parent / href / "index.html")
        assert fp.exists(), f"{p}: enlace roto {href} -> {fp}"
print(f"OK: {len(pages)} HTML, {len(urls)} URLs en sitemap, enlaces internos válidos.")
