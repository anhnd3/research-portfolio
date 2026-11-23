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
VIT=BASE+"articles/vision-transformers-facial-expression-recognition/"
GDEM=BASE+"articles/gdem-graph-distillation-reproduction/"
UFCE=BASE+"articles/verified-counterfactual-explanations-ufce-ff/"
NS="http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("",NS)
def tag(name): return f"{{{NS}}}{name}"

page=SITE/"articles/compact-domain-reranking/index.html"
image=SITE/"assets/research-reranking-og.png"
assert page.is_file(), "Research article missing from _site"
assert image.is_file() and image.stat().st_size>10000, "Social card missing from _site"
text=page.read_text(encoding="utf-8")
assert "<title>Compact Models for Domain-Specific Reranking | Qwen3-0.6B | Aiden</title>" in text, "Reranking SEO title missing"
assert re.search(r'<meta\b(?=[^>]*\bname="robots")(?=[^>]*\bcontent="index,follow,max-image-preview:large")[^>]*>',text), "Reranking must be indexable"
assert re.search(r'<link\b(?=[^>]*\brel="canonical")(?=[^>]*\bhref="'+re.escape(ARTICLE)+r'")[^>]*>',text), "Reranking canonical missing"
assert re.search(r'<meta\b(?=[^>]*\bproperty="og:image")(?=[^>]*\bcontent="'+re.escape(BASE+'assets/research-reranking-og.png')+r'")[^>]*>',text), "Reranking OG card missing"
assert re.search(r'<meta\b(?=[^>]*\bname="twitter:card")(?=[^>]*\bcontent="summary_large_image")[^>]*>',text), "Reranking Twitter card missing"
assert 'CONTENT PREVIEW' not in text and 'noindex' not in text, "Reranking draft metadata present"
assert 'What worked' in text and 'What still falls short' in text and 'class="key-takeaways-grid"' in text, "v3.1 balanced key takeaways absent"
assert 'E5 + Laya' in text and 'Qwen Direct' in text, "Full-pipeline evidence absent"
# Validate every internal article fragment and the header routes.
article_ids=set(re.findall(r'\bid="([^"]+)"',text))
local_links=re.findall(r'href="#([^"]+)"',text)
missing_anchors=sorted({anchor for anchor in local_links if anchor not in article_ids})
assert not missing_anchors, f"Broken article anchors: {missing_anchors}"
assert '<a href="#contract">Method</a>' in text and '<a href="#systems">Results</a>' in text and '<a href="#references">References</a>' in text, "Article header navigation targets changed"

match=re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>',text)
assert match, "Missing article JSON-LD"
data=json.loads(match.group(1))
assert data.get("@type")=="Article" and data.get("author",{}).get("name")=="Aiden"
assert data.get("datePublished")=="2026-11-02"
from datetime import date
modified = date.fromisoformat(data["dateModified"])
assert modified >= date.fromisoformat(data["datePublished"]), "dateModified precedes datePublished"

# The second publication is a standalone HTML resource, just like the reranking article.
vit_page=SITE/"articles/vision-transformers-facial-expression-recognition/index.html"
assert vit_page.is_file(), "ViT article missing from _site"
vit_text=vit_page.read_text(encoding="utf-8")
assert '<meta content="index,follow,max-image-preview:large" name="robots"' in vit_text, "ViT must be indexable"
assert f'href="{VIT}" rel="canonical"' in vit_text, "ViT canonical missing"
assert 'Vision Transformers for FER-2013:' in vit_text, "ViT SEO title missing"
vit_match=re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', vit_text)
assert vit_match, "ViT JSON-LD missing"
vit_data=json.loads(vit_match.group(1))
assert vit_data.get("@type")=="Article" and vit_data.get("author",{}).get("name")=="Aiden", "ViT JSON-LD invalid"
assert vit_data.get("datePublished")=="2026-11-22", "ViT publication date should not be research date"

# Standalone GDEM article: distinct social card, public status, research/publication dates.
gdem_page=SITE/"articles/gdem-graph-distillation-reproduction/index.html"
gdem_cover=SITE/"assets/research-gdem-og.png"
assert gdem_page.is_file(), "GDEM publication missing"
assert gdem_cover.is_file() and gdem_cover.stat().st_size>10000, "GDEM cover missing"
gdem_text=gdem_page.read_text(encoding="utf-8")
assert re.search(r'<meta[^>]+content="index,follow,max-image-preview:large"[^>]+name="robots"',gdem_text), "GDEM noindex"
assert f'href="{GDEM}" rel="canonical"' in gdem_text, "GDEM canonical missing"
assert 'Research period: Dec 2025' in gdem_text and 'CONTENT PREVIEW' not in gdem_text
assert f'content="{BASE}assets/research-gdem-og.png" property="og:image"' in gdem_text, "GDEM OG cover not configured"
gdem_match=re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>',gdem_text)
assert gdem_match, "GDEM Article structured data missing"
gdem_schema=json.loads(gdem_match.group(1))
gdem_data=next((n for n in gdem_schema.get("@graph",[]) if n.get("@type")=="Article"),None)
assert gdem_data and gdem_data.get("datePublished")=="2026-11-22" and gdem_data.get("temporalCoverage")=="2025-12"
assert gdem_data.get("author",{}).get("name")=="Aiden"


# UFCE thesis retrospective: research timing and publication timing are separate.
ufce_page=SITE/"articles/verified-counterfactual-explanations-ufce-ff/index.html"
ufce_cover=SITE/"assets/research-ufce-og.png"
assert ufce_page.is_file(), "UFCE retrospective not rendered"
assert ufce_cover.is_file() and ufce_cover.stat().st_size>10000, "UFCE social card missing"
ufce_text=ufce_page.read_text(encoding="utf-8")
assert re.search(r'<meta\b(?=[^>]*name="robots")(?=[^>]*content="index,follow,max-image-preview:large")[^>]*>',ufce_text), "UFCE noindex"
assert f'href="{UFCE}" rel="canonical"' in ufce_text, "UFCE canonical missing"
assert f'content="{BASE}assets/research-ufce-og.png" property="og:image"' in ufce_text, "UFCE OG image missing"
assert "CONTENT PREVIEW" not in ufce_text and "noindex" not in ufce_text, "UFCE draft markers"
assert "Thesis defended: Sep 2026" in ufce_text, "UFCE defense period missing"
assert "https://github.com/anhnd3/conversational-ufce" in ufce_text, "UFCE public code link missing"
assert ufce_text.count('class="research-provenance"') == 1, "Duplicate UFCE provenance"
assert len(re.findall(r'<li id="ref-\d+"', ufce_text))==34, "UFCE references incomplete"
assert 'id="cf-animated-demo"' in ufce_text and 'id="appendix"' in ufce_text, "UFCE interactive demo/appendix missing"
ufce_ids=set(re.findall(r'\bid="([^"]+)"',ufce_text))
assert not ({a for a in re.findall(r'href="#([^"]+)"',ufce_text) if a not in ufce_ids}), "UFCE broken local anchors"
ufce_match=re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>',ufce_text)
assert ufce_match, "UFCE ScholarlyArticle schema missing"
ufce_data=json.loads(ufce_match.group(1))
assert ufce_data.get("@type")=="ScholarlyArticle" and ufce_data.get("author",{}).get("name")=="Aiden"
assert ufce_data.get("datePublished")=="2026-11-23", "Do not backdate publication to thesis defense month"
assert ufce_data.get("dateModified")=="2026-11-23", "UFCE modified date missing"

home_text=(SITE/"index.html").read_text(encoding="utf-8")
assert "04 PUBLISHED STUDIES" in home_text and all(v in home_text for v in (VIT,GDEM,UFCE)), "Homepage publication index is stale"
assert '<h3 id="research-year-2026">2026</h3>' in home_text and '<h3 id="research-year-2025">2025</h3>' in home_text, "Research year groups missing"
assert home_text.index('id="research-year-2026"') < home_text.index('id="research-year-2025"'), "Research years must be newest first"
assert home_text.index(f'class="publication-entry" href="{ARTICLE}"') < home_text.index(f'class="publication-entry" href="{UFCE}"') < home_text.index(f'class="publication-entry" href="{GDEM}"') < home_text.index(f'class="publication-entry" href="{VIT}"'), "Research chronology is not reverse-ordered"
home_schema_match=re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>',home_text)
assert home_schema_match and [i["url"] for i in next(n for n in json.loads(home_schema_match.group(1))["@graph"] if n["@type"]=="CollectionPage")["mainEntity"]["itemListElement"]]==[ARTICLE,UFCE,GDEM,VIT], "Homepage structured data order differs from display"
assert f'href="{BASE}" rel="canonical"' in home_text, "Homepage canonical missing"
assert '<script type="application/ld+json">' in home_text, "Homepage JSON-LD missing"

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
    VIT:"articles/vision-transformers-facial-expression-recognition/index.html",
    GDEM:"articles/gdem-graph-distillation-reproduction/index.html",
    UFCE:"articles/verified-counterfactual-explanations-ufce-ff/index.html",
}
for url,relative in required.items():
    assert (SITE/relative).is_file(), f"Missing rendered page: {relative}"
    if url.rstrip("/") not in entries:
        item=ET.SubElement(root,tag("url"))
        ET.SubElement(item,tag("loc")).text=url
        entries[url.rstrip("/")]=[item]
    if url in (ARTICLE,VIT,GDEM,UFCE):
        item=entries[url.rstrip("/")][0]
        lastmod=item.find(tag("lastmod"))
        if lastmod is None: lastmod=ET.SubElement(item,tag("lastmod"))
        lastmod.text=data["dateModified"] if url==ARTICLE else (vit_data["dateModified"] if url==VIT else (gdem_data["dateModified"] if url==GDEM else ufce_data["dateModified"]))

locs=[e.text for e in root.findall(f'{tag("url")}/{tag("loc")}')]
assert len(locs)==len(set(url.rstrip("/") for url in locs)), "Duplicate URLs"
assert all(urlparse(url).hostname=="anhnd3.github.io" for url in locs), "Wrong sitemap host"
path.write_bytes(ET.tostring(root,encoding="utf-8",xml_declaration=True))
print(f"SEO verified: {len(locs)} URLs; homepage, four articles, canonicals and social cards OK.")
