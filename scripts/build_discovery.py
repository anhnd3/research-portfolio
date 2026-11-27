"""Write _site/feed.xml (Atom) from each article's JSON-LD after `quarto render`.

Articles are self-contained HTML resources, so Quarto does not list them in a feed.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
BASE = "https://anhnd3.github.io/research-portfolio/"
ABOUT = BASE + "about/"

entries = []
for page in sorted((SITE / "articles").glob("*/index.html")):
    text = page.read_text(encoding="utf-8")
    match = re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', text)
    assert match, f"{page}: missing JSON-LD"
    data = json.loads(match.group(1))
    art = next(n for n in data["@graph"] if n.get("@type") == "Article") if "@graph" in data else data
    url = BASE + page.parent.relative_to(SITE).as_posix() + "/"
    entries.append({
        "url": url,
        "title": art["headline"],
        "summary": art.get("abstract") or art.get("description", ""),
        "published": art["datePublished"],
        "updated": art.get("dateModified", art["datePublished"]),
    })

entries.sort(key=lambda e: (e["updated"], e["published"]), reverse=True)
feed_updated = max(e["updated"] for e in entries)
items = "".join(
    f"""
  <entry>
    <title>{escape(e['title'])}</title>
    <link href="{e['url']}"/>
    <id>{e['url']}</id>
    <published>{e['published']}T00:00:00Z</published>
    <updated>{e['updated']}T00:00:00Z</updated>
    <summary>{escape(e['summary'])}</summary>
  </entry>"""
    for e in entries
)
feed = f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Aiden Research Portfolio</title>
  <subtitle>Independent applied AI research: empirical studies and retrospectives.</subtitle>
  <link href="{BASE}feed.xml" rel="self"/>
  <link href="{BASE}"/>
  <id>{BASE}</id>
  <updated>{feed_updated}T00:00:00Z</updated>
  <author><name>Aiden (Nguyễn Duy Anh)</name><uri>{ABOUT}</uri></author>{items}
</feed>
"""
(SITE / "feed.xml").write_text(feed, encoding="utf-8")
print(f"Atom feed: {len(entries)} articles")
