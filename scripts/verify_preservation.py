#!/usr/bin/env python3
"""Comprueba conservación de contenido, contactos, metadata y paleta originales."""
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import hashlib,json,sys,re
R=Path(__file__).resolve().parents[1]
class P(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.text=[];self.links=[];self.meta=[];self.ld=False;self.buffer='';self.schemas=[];self.ids=[];self.options=[];self.cards=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if t in ('script','style'):
   self.skip+=1
   if t=='script' and a.get('type')=='application/ld+json':self.ld=True;self.buffer=''
  if t=='a':self.links.append(a.get('href',''))
  if t=='meta' or (t=='link' and a.get('rel')=='canonical'):self.meta.append([list(pair) for pair in sorted(a.items())])
  if t=='option' and a.get('value'):self.options.append(a['value'])
  if t=='a' and 'data-sector' in a:self.cards.append(a['href'].strip('/'))
 def handle_endtag(self,t):
  if t in ('script','style'):
   self.skip=max(0,self.skip-1)
   if self.ld:self.schemas.append(json.loads(self.buffer));self.ld=False
 def handle_data(self,d):
  if self.ld:self.buffer+=d
  if not self.skip and d.strip():self.text.append(' '.join(d.split()))
def read(p):
 parser=P();parser.feed(p.read_text());return parser
def data(p):
 x=read(p);return {'text':dict(Counter(x.text)),'links':dict(Counter(x.links)),'meta':x.meta,'schemas':x.schemas}
def hash(p):return hashlib.sha256(p.read_bytes()).hexdigest()
B=R/'auditoria/original.json'
if len(sys.argv)==3 and sys.argv[1]=='--baseline':
 source=Path(sys.argv[2]);out={'pages':{str(p.relative_to(source)):data(p) for p in source.rglob('*.html')},'files':{str(p.relative_to(source)):hash(p) for p in source.rglob('*') if p.is_file() and (p.suffix in ['.css','.png','.webp'] or p.name=='credis-assistant.js')}};B.write_text(json.dumps(out,ensure_ascii=False,indent=2));print('Base de conservación creada.')
else:
 original=json.loads(B.read_text())
 for rel,old in original['pages'].items():
  p=R/'docs'/rel;now=data(p)
  for field in ('text','links'):
   assert not (Counter(old[field])-Counter(now[field])),f'{rel}: contenido original perdido ({field})'
   if rel!='index.html':assert old[field]==now[field],f'{rel}: contenido alterado'
  for field in ('meta','schemas'):assert old[field]==now[field],f'{rel}: metadata alterada'
  ids=read(p).ids;assert len(ids)==len(set(ids)),f'{rel}: IDs duplicados'
 for rel,digest in original['files'].items():assert hash(R/'docs'/rel)==digest,f'{rel}: archivo original alterado'
 css=(R/'docs/css/mejoras.css').read_text();assert not re.search(r'#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(',css),'Nuevos colores literales'
 parsed=read(R/'docs/index.html');slugs={p['slug'] for p in json.loads((R/'content-pages.json').read_text())[:19]}
 assert set(parsed.options)==set(parsed.cards)==slugs
 print(f'OK: {len(original["pages"])} páginas; contenido y enlaces preservados, metadatos idénticos, CSS/colores e imágenes originales intactos; selector y buscador con 19 líneas.')
