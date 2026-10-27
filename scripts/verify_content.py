#!/usr/bin/env python3
"""Verifica que el rediseño conserve el contenido y enlaces aprobados."""
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
class Content(HTMLParser):
 def __init__(self):
  super().__init__();self.skip=0;self.words=[];self.links=[];self.meta=[];self.assets=[];self.ld=False;self.buffer='';self.structured=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('script','style'):
   self.skip+=1
   if tag=='script' and a.get('type')=='application/ld+json':self.ld=True;self.buffer=''
  if tag=='a':self.links.append(a.get('href',''))
  if tag=='meta':self.meta.append(sorted(a.items()))
  if tag=='img':self.assets.append(sorted(a.items()))
  if tag=='link' and a.get('rel')=='canonical':self.meta.append(sorted(a.items()))
 def handle_endtag(self,tag):
  if tag in ('script','style'):
   self.skip=max(0,self.skip-1)
   if self.ld:self.structured.append(json.loads(self.buffer));self.ld=False
 def handle_data(self,data):
  if self.ld:self.buffer+=data
  if not self.skip:
   text=' '.join(data.split())
   if text:self.words.append(text)
def signature(path):
 p=Content();p.feed(path.read_text())
 def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
 return {'textos':digest(dict(Counter(p.words))),'enlaces':digest(dict(Counter(p.links))),'metadatos':digest(sorted(p.meta)),'imagenes':digest(sorted(p.assets)),'datos_estructurados':digest(p.structured)}
if __name__=='__main__':
 baseline=ROOT/'auditoria/contenido-original.json'
 if len(sys.argv)==3 and sys.argv[1]=='--baseline':
  source=Path(sys.argv[2]);result={str(p.relative_to(source)):signature(p) for p in sorted(source.rglob('*.html'))};baseline.write_text(json.dumps(result,indent=2));print(f'Base original: {len(result)} páginas')
 else:
  data=json.loads(baseline.read_text());errors=[]
  for rel,expected in data.items():
   actual=signature(ROOT/'docs'/rel)
   for field in expected:
    if expected[field]!=actual[field]:errors.append(f'{rel}: cambió {field}')
  if errors:print('\n'.join(errors));sys.exit(1)
  print(f'OK: {len(data)} páginas conservan textos, enlaces, metadatos, imágenes y datos estructurados del original. El orden visual puede cambiar.')
