#!/usr/bin/env python3
"""Pruebas de interfaz en Chromium mediante documento aislado (sin servidor HTTP)."""
from pathlib import Path
import sys
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'
ERRORS=[]

def embed(name):
    raw=(DOCS/name).read_text('utf-8')
    soup=BeautifulSoup(raw,'html.parser')
    tag=soup.find('link',href='/css/site.css')
    if tag:
        css=soup.new_tag('style');css.string=(DOCS/'css/site.css').read_text('utf-8');tag.replace_with(css)
    s=soup.find('script',src='/js/site.js')
    if s:
        script=soup.new_tag('script');script.string=(DOCS/'js/site.js').read_text('utf-8');s.replace_with(script)
    return str(soup)

def check(cond, msg):
    if not cond: ERRORS.append(msg)

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    desktop=browser.new_context(viewport={'width':1440,'height':900},device_scale_factor=1)
    page=desktop.new_page()
    page.on('pageerror', lambda e:ERRORS.append('JS desktop: '+str(e)))
    page.set_content(embed('index.html'),wait_until='load')
    check(page.title().startswith('Préstamos por descuento de haberes'),'Title homepage')
    check(page.get_by_role('heading',level=1).count()==1,'H1 homepage')
    check(page.locator('.line-card').count()==6,'Six featured category cards')
    check(page.locator('#sector-select option').count()==19,'Sector selector has 18 options plus prompt')
    page.screenshot(path=str(ROOT/'preview-desktop.png'),full_page=True)
    page.screenshot(path=str(ROOT/'preview-desktop-first-fold.png'))
    for width,height in [(390,844),(320,760),(768,1024)]:
        context=browser.new_context(viewport={'width':width,'height':height},device_scale_factor=1,is_mobile=True,has_touch=True)
        mobile=context.new_page()
        mobile.on('pageerror',lambda e:ERRORS.append(f'JS mobile {width}: '+str(e)))
        mobile.set_content(embed('index.html'),wait_until='load')
        if width==390:
            mobile.screenshot(path=str(ROOT/'preview-mobile.png'),full_page=True)
            mobile.screenshot(path=str(ROOT/'preview-mobile-first-fold.png'))
        scroll_width=mobile.evaluate('document.documentElement.scrollWidth')
        check(scroll_width<=width+1,f'Overflow at {width}px: {scroll_width}px')
        if width<=760:
            mobile.get_by_role('button',name='Abrir menú').click()
            check(mobile.get_by_role('button',name='Cerrar menú').get_attribute('aria-expanded')=='true',f'Menu open state at {width}')
            check(mobile.get_by_role('navigation',name='Navegación principal').is_visible(),f'Menu visible at {width}')
            mobile.keyboard.press('Escape')
            check(mobile.get_by_role('button',name='Abrir menú').get_attribute('aria-expanded')=='false',f'Escape closes menu {width}')
        else:
            check(mobile.get_by_role('navigation',name='Navegación principal').is_visible(),f'Tablet menu visible {width}')
        mobile.locator('details').first.locator('summary').click()
        check(mobile.locator('details').first.get_attribute('open') is not None,f'Details open at {width}')
        context.close()
    page.set_content(embed('prestamos-ejercito-argentino/index.html'),wait_until='load')
    check(page.locator('h1').inner_text().startswith('Préstamos para Ejército Argentino'),'Category h1')
    check(page.locator('details').count()==3,'Category FAQ count')
    page.set_content(embed('preguntas-frecuentes/index.html'),wait_until='load')
    check(page.locator('details').count()==8,'FAQ eight questions')
    page.set_content(embed('404.html'),wait_until='load')
    check('noindex' in page.locator('meta[name="robots"]').get_attribute('content'),'404 noindex')
    browser.close()
print('Chromium DOM+render tests: 1440 / 768 / 390 / 320, navigation, FAQ, content landmarks.')
print('Note: isolated HTML rendering; real HTTP routing and Cloudflare deployment not tested.')
print('Errors:',len(ERRORS))
for error in ERRORS:print('ERROR:',error)
sys.exit(1 if ERRORS else 0)
