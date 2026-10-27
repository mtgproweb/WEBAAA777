#!/usr/bin/env python3
"""Validación estática reproducible del proyecto generado."""
from pathlib import Path
from urllib.parse import urlparse, unquote
import json, re, sys, xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
HTML=list(DOCS.rglob('*.html'))
errors=[]; warns=[]; nlinks=0; jsld=0
routes=set()
for f in HTML:
    rel=f.relative_to(DOCS)
    route='/' if rel.name=='index.html' and str(rel.parent)=='.' else ('/'+str(rel.parent).replace('\\','/')+'/' if rel.name=='index.html' else '/'+str(rel))
    routes.add(route)
    soup=BeautifulSoup(f.read_text(encoding='utf-8'),'html.parser')
    if not soup.html or soup.html.get('lang')!='es-AR':errors.append(f'{rel}: language missing')
    if len(soup.find_all('h1'))!=1:errors.append(f'{rel}: requires single H1')
    if not soup.title or not soup.title.text.strip():errors.append(f'{rel}: title missing')
    if not soup.find('meta',attrs={'name':'description'}):errors.append(f'{rel}: description missing')
    if not soup.find('meta',attrs={'name':'viewport'}):errors.append(f'{rel}: viewport missing')
    if not soup.find('main',attrs={'id':'contenido'}):errors.append(f'{rel}: main landmark missing')
    if not soup.find('a',attrs={'href':'#contenido'}):errors.append(f'{rel}: skip link missing')
    if f.name=='404.html':
      robot=soup.find('meta',attrs={'name':'robots'})
      if not robot or 'noindex' not in robot.get('content',''):errors.append(f'{rel}: 404 should noindex')
    else:
      c=soup.find('link',attrs={'rel':'canonical'})
      if not c or c.get('href')!='https://www.credisnet.com.ar'+route:errors.append(f'{rel}: wrong canonical')
    for sc in soup.find_all('script',attrs={'type':'application/ld+json'}):
      jsld+=1
      try: json.loads(sc.string or sc.text)
      except Exception as e:errors.append(f'{rel}: invalid JSON-LD: {e}')
    for img in soup.find_all('img'):
      if not img.has_attr('alt'): errors.append(f'{rel}: img without alt')
    for a in soup.find_all('a',href=True):
      nlinks+=1; href=a['href']; p=urlparse(href)
      if p.scheme or href.startswith('//') or href.startswith('#'):continue
      target=p.path
      if not target.startswith('/'):warns.append(f'{rel}: relative link {target}');continue
      if target.endswith('/'):dest=DOCS/target.strip('/')/'index.html' if target!='/' else DOCS/'index.html'
      else:dest=DOCS/target.strip('/')
      if not dest.is_file():errors.append(f'{rel}: broken internal link: {href}')
    for asset in soup.find_all(['script','link']):
      att='src' if asset.name=='script' else 'href'
      raw=asset.get(att,'')
      if raw.startswith('/'):
        dest=DOCS/raw.strip('/')
        if not dest.is_file():errors.append(f'{rel}: missing resource {raw}')
    for sel in soup.find_all('select'):
      if not sel.get('id') or not soup.find('label',attrs={'for':sel['id']}): errors.append(f'{rel}: select without label')
    for b in soup.find_all('button'):
      if not b.get_text(' ',strip=True) and not b.get('aria-label'): errors.append(f'{rel}: unlabeled button')

sitemap=DOCS/'sitemap.xml'
try:
 tree=ET.parse(sitemap)
 ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
 locs=[x.text for x in tree.findall('.//s:loc',ns)]
 if len(locs)!=len(set(locs)):errors.append('Duplicate sitemap loc')
 for route in routes-{'/404.html'}:
  if 'https://www.credisnet.com.ar'+route not in locs:errors.append(f'Sitemap missing {route}')
 if len(locs)!=len(routes)-1:errors.append(f'Sitemap count {len(locs)} != routes {len(routes)-1}')
except Exception as e: errors.append(f'Invalid sitemap: {e}')

# Basic security / content checks
for file in ['_headers','_redirects','robots.txt','css/site.css','js/site.js','assets/favicon.svg','assets/og-card.png']:
 if not (DOCS/file).is_file():errors.append(f'Missing {file}')
markup='\n'.join(f.read_text(encoding='utf-8') for f in HTML)
for claim in ['4.9 estrellas','+10.000 personas','Martín R. Sargento','aprobación garantizada']:
 if claim.lower() in markup.lower(): errors.append('Unverified claim found: '+claim)
print('HTML files:',len(HTML),'| indexable routes:',len(routes)-1,'| checked links:',nlinks,'| valid JSON-LD blocks:',jsld)
print('WARNINGS:',len(warns),'| ERRORS:',len(errors))
for x in warns[:10]:print('WARN',x)
for x in errors[:40]:print('ERROR',x)
sys.exit(1 if errors else 0)
