#!/usr/bin/env python3
"""Comprobaciones de semántica, fragmentos, JSON-LD y vista de prueba."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
class Parser(HTMLParser):
 def __init__(self):
  super().__init__(); self.ids=[]; self.links=[]; self.h1=0; self.ld=False; self.json=[]; self.buffer='';self.errors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='a':
   self.links.append(a.get('href',''))
   if a.get('target')=='_blank':assert 'noopener' in a.get('rel','')
  if tag=='img':assert 'alt' in a and 'width' in a and 'height' in a
  if tag=='script' and a.get('type')=='application/ld+json': self.ld=True; self.buffer=''
 def handle_data(self,d):
  if self.ld:self.buffer+=d
 def handle_endtag(self,tag):
  if tag=='script' and self.ld:self.json.append(json.loads(self.buffer));self.ld=False
pages={}
for f in (ROOT/'docs').rglob('*.html'):
 p=Parser();p.feed(f.read_text());pages[f.resolve()]=p
 assert p.h1==1,f'{f}: H1'
 assert len(set(p.ids))==len(p.ids),f'{f}: duplicate ids'
for f,p in pages.items():
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc or not u.fragment:continue
  target=(f.parent/unquote(u.path)).resolve() if u.path else f
  if target.is_dir(): target=target/'index.html'
  assert unquote(u.fragment) in pages[target].ids,(f,link)
for f in (ROOT/'_site').rglob('*.html'):
 text=f.read_text();assert text.count('name="robots"')==1 and 'noindex,nofollow,noarchive' in text
assert 'Disallow: /' in (ROOT/'_site/robots.txt').read_text()
print(f'OK: {len(pages)} páginas; H1, IDs únicos, imágenes, JSON-LD, enlaces con fragmentos y vista no indexable.')
