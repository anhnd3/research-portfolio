"""Ensure standalone HTML is present in the Quarto sitemap; validate SEO artifacts."""
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import json
import re

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"_site"
BASE="https://anhnd3.github.io/research-portfolio/"
ARTICLE=BASE+"articles/compact-domain-reranking/"
NS="http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("",NS)
def tag(name): return f"{{{NS}}}{name}"

page=SITE/"articles/compact-domain-reranking/index.html"
image=SITE/"assets/research-reranking-og.png"
assert page.is_file(), "Research article missing from _site"
assert image.is_file() and image.stat().st_size>10000, "Social card missing from _site"
text=page.read_text(encoding="utf-8")
assert re.search(r"<title>Compact Models for Domain-Specific Reranking · Aiden · v[0-9]+\.[0-9]+</title>", text), "Versioned article title missing"
assert '<meta name="robots" content="index,follow' in text
assert f'<link rel="canonical" href="{ARTICLE}"' in text
assert f'<meta property="og:image" content="{BASE}assets/research-reranking-og.png"' in text
assert 'name="twitter:card" content="summary_large_image"' in text
match=re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>',text)
assert match, "Missing article JSON-LD"
data=json.loads(match.group(1))
assert data.get("@type")=="Article" and data.get("author",{}).get("name")=="Aiden"
assert data.get("datePublished")=="2026-11-02"
from datetime import date
modified = date.fromisoformat(data["dateModified"])
assert modified >= date.fromisoformat(data["datePublished"]), "dateModified precedes datePublished"

path=SITE/"sitemap.xml"
if path.exists():
    tree=ET.parse(path)
    root=tree.getroot()
    assert root.tag==tag("urlset"), f"Unrecognized sitemap namespace {root.tag}"
else:
    root=ET.Element(tag("urlset"))
    tree=ET.ElementTree(root)

entries={}
for item in root.findall(tag("url")):
    loc=item.findtext(tag("loc"))
    if loc: entries.setdefault(loc.rstrip("/"),[]).append(item)
for group in entries.values():
    for duplicate in group[1:]: root.remove(duplicate)

required={
    BASE:"index.html",
    BASE+"articles.html":"articles.html",
    BASE+"notes.html":"notes.html",
    BASE+"about.html":"about.html",
    BASE+"policy.html":"policy.html",
    ARTICLE:"articles/compact-domain-reranking/index.html",
}
for url,relative in required.items():
    assert (SITE/relative).is_file(), f"Missing rendered page: {relative}"
    if url.rstrip("/") not in entries:
        item=ET.SubElement(root,tag("url"))
        ET.SubElement(item,tag("loc")).text=url
        entries[url.rstrip("/")]=[item]
    if url==ARTICLE:
        item=entries[url.rstrip("/")][0]
        lastmod=item.find(tag("lastmod"))
        if lastmod is None: lastmod=ET.SubElement(item,tag("lastmod"))
        lastmod.text=data["dateModified"]

locs=[e.text for e in root.findall(f'{tag("url")}/{tag("loc")}')]
assert len(locs)==len(set(url.rstrip("/") for url in locs)), "Duplicate URLs"
assert all(urlparse(url).hostname=="anhnd3.github.io" for url in locs), "Wrong sitemap host"
path.write_bytes(ET.tostring(root,encoding="utf-8",xml_declaration=True))
print(f"SEO verified: {len(locs)} URLs; article, metadata, JSON-LD, social card OK.")
