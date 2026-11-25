#!/usr/bin/env python3
"""Avisa a Bing/Yandex (IndexNow) de todas las URLs del sitemap.
Uso: python3 _tools/ping_indexnow.py   (después de publicar)"""
import json, re, urllib.request
from pathlib import Path
root = Path(__file__).resolve().parent.parent
key = (Path(__file__).parent / "indexnow.key").read_text().strip()
urls = re.findall(r"<loc>(.*?)</loc>", (root / "sitemap.xml").read_text())
body = json.dumps({"host": "visionatec.com", "key": key,
                   "keyLocation": f"https://visionatec.com/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req) as r:
    print(r.status, len(urls), "URLs enviadas")
