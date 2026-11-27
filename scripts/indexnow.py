"""Notify IndexNow (Bing, Yandex, Seznam, Naver...) about every URL in the live sitemap.

Runs after deployment. Failure here never blocks publishing.
"""
from pathlib import Path
from xml.etree import ElementTree as ET
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://anhnd3.github.io/research-portfolio/"
keys = [p for p in ROOT.glob("*.txt") if p.stem == p.read_text(encoding="utf-8").strip() and len(p.stem) == 32]
assert len(keys) == 1, "Expected exactly one IndexNow key file (<key>.txt) at the repository root"
key = keys[0].stem

with urllib.request.urlopen(BASE + "sitemap.xml", timeout=30) as response:
    root = ET.fromstring(response.read())
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [loc.text for loc in root.findall("s:url/s:loc", ns)]

body = json.dumps({
    "host": "anhnd3.github.io",
    "key": key,
    "keyLocation": f"{BASE}{key}.txt",
    "urlList": urls,
}).encode()
request = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=body,
    headers={"Content-Type": "application/json; charset=utf-8"},
)
with urllib.request.urlopen(request, timeout=30) as response:
    print(f"IndexNow: HTTP {response.status} for {len(urls)} URLs")
