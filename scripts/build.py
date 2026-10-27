#!/usr/bin/env python3
"""Genera una web estática, accesible y sin dependencias de ejecución para Credisnet."""
from __future__ import annotations
import html
import json
from pathlib import Path
from urllib.parse import quote
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
CONFIG = json.loads((ROOT / "config" / "site.json").read_text(encoding="utf-8"))
DOMAIN = CONFIG["canonical_domain"].rstrip("/")
WHATSAPP = str(CONFIG["whatsapp"])
BRAND = CONFIG["brand"]
if not WHATSAPP.isdecimal() or not 8 <= len(WHATSAPP) <= 15:
    raise ValueError("El WhatsApp debe contener entre 8 y 15 dígitos sin + ni espacios")

# Una sola fuente para la información de líneas; el sitio NO publica montos o aprobaciones
# no verificados, ni calculadoras sin tasas y CFT reales.
LINES = [
    dict(slug='prestamos-empleados-publicos', short='Empleados públicos', title='Préstamos para empleados públicos nacionales', group='Administración pública', code='01', icon='◧',
         summary='Opciones de préstamos para personal de la Administración Pública Nacional con operatorias de descuento de haberes, según el organismo y la entidad otorgante.',
         audience='Personal de organismos de la Administración Pública Nacional que percibe haberes y tiene una línea de descuento habilitada.', legal='Nacional, según operatoria y convenio aplicables.', related=['prestamos-fuerzas-armadas','prestamos-fuerzas-de-seguridad']),
    dict(slug='prestamos-fuerzas-armadas', short='Fuerzas Armadas', title='Préstamos para Fuerzas Armadas', group='Fuerzas Armadas', code='02', icon='✳',
         summary='Asesoramiento para integrantes del Ejército Argentino, Armada Argentina y Fuerza Aérea, con gestión digital y evaluación de la entidad.',
         audience='Personal activo, retirado y civil de las Fuerzas Armadas, sujeto a la operatoria correspondiente.', legal='Régimen nacional y convenios de cada organismo, cuando corresponda.', related=['prestamos-ejercito-argentino','prestamos-armada-argentina','prestamos-fuerza-aerea-argentina']),
    dict(slug='prestamos-fuerzas-de-seguridad', short='Fuerzas de seguridad', title='Préstamos para fuerzas de seguridad', group='Fuerzas de seguridad', code='03', icon='✦',
         summary='Consultá alternativas de financiación para integrantes de fuerzas federales de seguridad con descuento en haberes, cuando la línea esté disponible.',
         audience='Personal de Policía Federal, Gendarmería, Prefectura, PSA y Servicio Penitenciario Federal.', legal='Normativa nacional y condiciones de la entidad y del organismo.', related=['prestamos-policia-federal','prestamos-gendarmeria-nacional','prestamos-prefectura-naval-argentina']),
    dict(slug='prestamos-para-docentes-y-auxiliares', short='Docentes y auxiliares', title='Préstamos para docentes y auxiliares DGCyE', group='Provincia de Buenos Aires', code='04', icon='✎',
         summary='Opciones para docentes y auxiliares del sistema educativo bonaerense que perciben haberes a través de DGCyE.',
         audience='Docentes y auxiliares DGCyE de la Provincia de Buenos Aires, según situación de revista y margen disponible.', legal='Operatoria provincial, incluida la regulación aplicable de descuentos sobre haberes.', related=['prestamos-personal-salud','prestamos-policia-provincia-buenos-aires']),
    dict(slug='prestamos-policia-provincia-buenos-aires', short='Policía bonaerense', title='Préstamos para Policía de la Provincia de Buenos Aires', group='Provincia de Buenos Aires', code='05', icon='◈',
         summary='Gestión orientada a personal de la Policía bonaerense, según disponibilidad de operatorias con descuento en haberes.',
         audience='Personal activo y retirado de la Policía de la Provincia de Buenos Aires alcanzado por las líneas ofrecidas.', legal='Normativa provincial y convenio aplicable.', related=['prestamos-servicio-penitenciario-bonaerense','prestamos-para-docentes-y-auxiliares']),
    dict(slug='prestamos-personal-salud', short='Personal de salud', title='Préstamos para personal de salud', group='Provincia de Buenos Aires', code='06', icon='✚',
         summary='Información y acompañamiento para profesionales y trabajadores de salud del sector público con descuentos de haberes habilitados.',
         audience='Personal del sector público de salud, incluidos profesionales, técnicos y administrativos, según el organismo.', legal='Normativa y convenios del organismo empleador.', related=['prestamos-para-docentes-y-auxiliares','prestamos-empleados-publicos']),
    dict(slug='prestamos-jubilados-pensionados-ips', short='Jubilados IPS', title='Préstamos para jubilados y pensionados IPS', group='Jubilados y retirados', code='07', icon='◎',
         summary='Consultá alternativas de crédito con descuento sobre haberes previsionales para jubilados y pensionados del IPS bonaerense.',
         audience='Jubilados y pensionados del Instituto de Previsión Social (IPS), si su beneficio admite la operatoria.', legal='Normativa previsional y condiciones específicas del beneficio.', related=['prestamos-personal-retirado-fuerzas']),
    dict(slug='prestamos-ejercito-argentino', short='Ejército Argentino', title='Préstamos para Ejército Argentino', group='Fuerzas Armadas', code='08', icon='✳',
         summary='Líneas para integrantes del Ejército Argentino. Conocé qué información se necesita para evaluar una gestión por descuento de haberes.',
         audience='Cuadros permanentes, soldados voluntarios, personal civil y retirados, según las condiciones de cada línea.', legal='Régimen nacional y convenios vigentes.', related=['prestamos-fuerzas-armadas','prestamos-armada-argentina']),
    dict(slug='prestamos-armada-argentina', short='Armada Argentina', title='Préstamos para Armada Argentina', group='Fuerzas Armadas', code='09', icon='≈',
         summary='Orientación para personal de Armada Argentina sobre alternativas de financiación y descuento en haberes.',
         audience='Personal de la Armada, según condición laboral o de retiro y habilitación de la línea.', legal='Régimen nacional y convenios vigentes.', related=['prestamos-fuerzas-armadas','prestamos-fuerza-aerea-argentina']),
    dict(slug='prestamos-fuerza-aerea-argentina', short='Fuerza Aérea', title='Préstamos para Fuerza Aérea Argentina', group='Fuerzas Armadas', code='10', icon='✧',
         summary='Consulta de alternativas para personal de Fuerza Aérea Argentina, con acompañamiento durante la preparación de la solicitud.',
         audience='Personal de Fuerza Aérea, incluido personal civil y retirado cuando el convenio lo permita.', legal='Régimen nacional y convenios vigentes.', related=['prestamos-fuerzas-armadas','prestamos-ejercito-argentino']),
    dict(slug='prestamos-policia-federal', short='Policía Federal', title='Préstamos para Policía Federal Argentina', group='Fuerzas de seguridad', code='11', icon='✦',
         summary='Alternativas de crédito destinadas a personal de la Policía Federal Argentina, con evaluación de margen y requisitos.',
         audience='Personal activo o retirado de Policía Federal alcanzado por las operatorias disponibles.', legal='Normativa nacional, previsional o convenio que corresponda.', related=['prestamos-fuerzas-de-seguridad','prestamos-gendarmeria-nacional']),
    dict(slug='prestamos-gendarmeria-nacional', short='Gendarmería', title='Préstamos para Gendarmería Nacional', group='Fuerzas de seguridad', code='12', icon='✦',
         summary='Asesoramiento para integrantes de Gendarmería Nacional sobre préstamos con descuento en haberes, sujetos a evaluación.',
         audience='Personal de Gendarmería Nacional con haberes y operador habilitado para el convenio.', legal='Régimen nacional y convenios vigentes.', related=['prestamos-fuerzas-de-seguridad','prestamos-prefectura-naval-argentina']),
    dict(slug='prestamos-prefectura-naval-argentina', short='Prefectura Naval', title='Préstamos para Prefectura Naval Argentina', group='Fuerzas de seguridad', code='13', icon='≈',
         summary='Consulta de líneas de crédito para personal de Prefectura Naval Argentina, mediante descuentos autorizados.',
         audience='Personal activo y retirado de Prefectura, según el convenio y beneficio aplicables.', legal='Régimen nacional y convenios vigentes.', related=['prestamos-fuerzas-de-seguridad','prestamos-gendarmeria-nacional']),
    dict(slug='prestamos-policia-seguridad-aeroportuaria', short='Policía Aeroportuaria', title='Préstamos para Policía de Seguridad Aeroportuaria', group='Fuerzas de seguridad', code='14', icon='✦',
         summary='Información sobre financiación para integrantes de la PSA y documentación necesaria para iniciar la consulta.',
         audience='Personal de Policía de Seguridad Aeroportuaria según elegibilidad de cada línea.', legal='Normativa y convenios vigentes.', related=['prestamos-fuerzas-de-seguridad','prestamos-policia-federal']),
    dict(slug='prestamos-servicio-penitenciario-federal', short='Servicio Penitenciario Federal', title='Préstamos para Servicio Penitenciario Federal', group='Fuerzas de seguridad', code='15', icon='▦',
         summary='Asesoramiento para personal del Servicio Penitenciario Federal sobre préstamos sujetos a descuento en haberes.',
         audience='Personal del Servicio Penitenciario Federal con línea disponible y margen compatible.', legal='Normativa nacional y convenios vigentes.', related=['prestamos-fuerzas-de-seguridad','prestamos-policia-federal']),
    dict(slug='prestamos-policia-de-la-ciudad', short='Policía de la Ciudad', title='Préstamos para Policía de la Ciudad', group='Fuerzas de seguridad', code='16', icon='◈',
         summary='Orientación para personal de la Policía de la Ciudad de Buenos Aires sobre operatorias vigentes y requisitos.',
         audience='Personal de la Policía de la Ciudad que resulte alcanzado por una línea habilitada.', legal='Normativa del organismo y convenio de la entidad.', related=['prestamos-policia-provincia-buenos-aires','prestamos-fuerzas-de-seguridad']),
    dict(slug='prestamos-servicio-penitenciario-bonaerense', short='Penitenciario bonaerense', title='Préstamos para Servicio Penitenciario Bonaerense', group='Provincia de Buenos Aires', code='17', icon='▦',
         summary='Alternativas de crédito por descuento de haberes para el personal del Servicio Penitenciario Bonaerense.',
         audience='Personal del Servicio Penitenciario Bonaerense, sujeto a convenio, requisitos y evaluación crediticia.', legal='Normativa provincial y convenios vigentes.', related=['prestamos-policia-provincia-buenos-aires','prestamos-personal-salud']),
    dict(slug='prestamos-personal-retirado-fuerzas', short='Personal retirado', title='Préstamos para personal retirado de fuerzas', group='Jubilados y retirados', code='18', icon='◎',
         summary='Información para personal retirado de fuerzas armadas y de seguridad acerca de operatorias sobre haberes de retiro.',
         audience='Personal retirado y pensionado de fuerzas con beneficios compatibles con una línea habilitada.', legal='Régimen previsional y convenio aplicable.', related=['prestamos-jubilados-pensionados-ips','prestamos-fuerzas-armadas']),
]
LINE_BY_SLUG = {line['slug']: line for line in LINES}

FAQ = [
    ('¿Qué es un préstamo por descuento de haberes?', 'Es una modalidad en la que, si el organismo y la entidad lo permiten, la cuota se descuenta de los haberes según una autorización y un convenio aplicables. Las condiciones se informan antes de contratar.'),
    ('¿Credisnet es quien presta el dinero?', 'No. Credisnet se presenta como comercializadora y gestora de solicitudes. La evaluación, aprobación, desembolso y cobranza corresponden a la entidad otorgante.'),
    ('¿Puedo consultar sin compromiso?', 'Sí. La consulta y el asesoramiento se presentan como gratuitos. Antes de aceptar cualquier crédito, pedí los costos, la tasa, el Costo Financiero Total (CFT), el plazo y el total a devolver por escrito.'),
    ('¿Qué documentos suelen solicitar?', 'Habitualmente pueden pedir DNI, recibo de haberes, constancia del organismo y un CBU a nombre del solicitante. No compartas documentación sensible hasta verificar el canal y la entidad interviniente.'),
    ('¿Cuánto puedo solicitar y cuántas cuotas son?', 'Depende de la línea habilitada, la entidad otorgante, tu margen disponible, tu situación y la evaluación crediticia. No hay un monto o una cantidad de cuotas que pueda garantizarse para todas las personas.'),
    ('¿Cuánto tarda la respuesta?', 'Los plazos dependen de la validación de la documentación y de la entidad otorgante. Una consulta inicial no equivale a aprobación ni garantiza una fecha de acreditación.'),
    ('¿Puedo solicitarlo si tengo antecedentes crediticios?', 'La evaluación depende de las políticas de la entidad y la operatoria disponible. Un antecedente negativo no asegura ni descarta por sí solo la aprobación.'),
    ('¿Qué tengo que revisar antes de firmar?', 'Solicitá el monto neto a recibir, cantidad e importe de cuotas, TNA/TEA cuando correspondan, CFT, entidad otorgante, cargos adicionales, condiciones de cancelación anticipada y copia del contrato.'),
]

DOCS.mkdir(exist_ok=True, parents=True)

def esc(s): return html.escape(str(s), quote=True)
def path(slug=''): return '/' + (slug.strip('/') + '/' if slug else '')
def url(slug=''): return DOMAIN + path(slug)
def wa(message='Hola, quisiera recibir información sobre préstamos por descuento de haberes.'):
    return f'https://wa.me/{WHATSAPP}?text={quote(message, safe="")}'
def link(slug, label=None, cls=''):
    line = LINE_BY_SLUG[slug]
    return f'<a class="{esc(cls)}" href="{path(slug)}">{esc(label or line["short"])} <span aria-hidden="true">↗</span></a>'

def schema(data):
    return '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')+'</script>'

def base_page(title, description, slug, content, *, page_type='website', social='Credisnet | Soluciones para el sector público', extra_schema=None):
    canonical=url(slug)
    desc=description[:158]
    seo_title=title if 'Credisnet' in title else title+' | Credisnet'
    # JSON-LD solo Organization / WebSite / Service según contenido representado, sin ratings inventados.
    web_schema={"@context":"https://schema.org","@type":"WebSite","name":"Credisnet","url":DOMAIN+'/',"inLanguage":"es-AR"}
    org_schema={"@context":"https://schema.org","@type":"Organization","name":"Credisnet","url":DOMAIN+'/',"description":"Gestión y comercialización de solicitudes de préstamos por descuento de haberes en Argentina."}
    if extra_schema: extra=schema(extra_schema)
    else: extra=''
    return f'''<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#f7f8f3">
<title>{esc(seo_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(canonical)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="Credisnet">
<meta property="og:title" content="{esc(seo_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{DOMAIN}/assets/og-card.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="stylesheet" href="/css/site.css">
{schema(web_schema)}
{schema(org_schema)}
{extra}
</head>
<body>
<a class="skip-link" href="#contenido">Saltar al contenido principal</a>
{header()}
<main id="contenido">{content}</main>
{footer()}
<script src="/js/site.js" defer></script>
</body></html>'''

def header():
    return f'''<div class="topbar"><div class="container topbar-inner"><span><span class="topbar-dot"></span> Asesoramiento para personal del sector público</span><span>Argentina · Gestión digital</span></div></div>
<header class="site-header"><div class="container header-inner">
<a href="/" class="brand" aria-label="Credisnet — inicio"><span class="brand-mark"><span></span><span></span><span></span></span><span>credisnet<span class="brand-stop">.</span></span></a>
<nav aria-label="Navegación principal" id="primary-nav" class="nav-links">
<a href="/#lineas">Líneas de crédito</a><a href="/#como-funciona">Cómo funciona</a><a href="/quienes-somos/">Nosotros</a><a href="/preguntas-frecuentes/">Preguntas frecuentes</a></nav>
<div class="nav-actions"><a class="btn btn-dark nav-cta" href="{wa('Hola, quiero consultar opciones de préstamos por descuento de haberes.')}" target="_blank" rel="noopener noreferrer">Consultar por WhatsApp <span aria-hidden="true">↗</span></a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Abrir menú"><span></span><span></span><span></span></button></div>
</div></header>'''

def footer():
    cats=[('Empleados públicos','prestamos-empleados-publicos'),('Fuerzas Armadas','prestamos-fuerzas-armadas'),('Fuerzas de seguridad','prestamos-fuerzas-de-seguridad'),('Docentes y auxiliares','prestamos-para-docentes-y-auxiliares'),('Personal de salud','prestamos-personal-salud'),('Jubilados IPS','prestamos-jubilados-pensionados-ips')]
    items=''.join(f'<li><a href="/{s}/">{esc(n)}</a></li>' for n,s in cats)
    return f'''<footer class="footer"><div class="container">
<div class="footer-main"><div class="footer-about"><a class="brand brand-footer" href="/"><span class="brand-mark"><span></span><span></span><span></span></span><span>credisnet<span class="brand-stop">.</span></span></a>
<p>Información clara para dar el próximo paso. Gestionamos solicitudes de crédito para personal del sector público argentino.</p>
<a href="{wa()}" class="footer-contact" target="_blank" rel="noopener noreferrer">Hablar con un asesor <span aria-hidden="true">↗</span></a></div>
<div><h2 class="footer-heading">Líneas</h2><ul>{items}</ul></div>
<div><h2 class="footer-heading">Credisnet</h2><ul><li><a href="/quienes-somos/">Quiénes somos</a></li><li><a href="/preguntas-frecuentes/">Preguntas frecuentes</a></li><li><a href="/guia-descuento-de-haberes/">Guía del descuento</a></li><li><a href="/contacto/">Contacto</a></li></ul></div>
<div><h2 class="footer-heading">Información legal</h2><ul><li><a href="/terminos-y-condiciones/">Términos y condiciones</a></li><li><a href="/politica-de-privacidad/">Política de privacidad</a></li></ul></div></div>
<div class="footer-disclaimer">Credisnet actúa como intermediario comercial y gestor de solicitudes; no es la entidad que otorga el crédito. Toda financiación está sujeta a la evaluación, aprobación y condiciones de la entidad otorgante. No se garantiza un monto, tasa ni plazo de aprobación. Verificá siempre el CFT y el contrato antes de aceptar.</div>
<div class="footer-bottom"><span>© {date.today().year} Credisnet. Todos los derechos reservados.</span><span>Hecho para personas, no para promesas.</span></div>
</div></footer>'''

def mini_label(t):return f'<div class="eyebrow"><span class="eyebrow-line"></span>{esc(t)}</div>'
def faq_html(items=FAQ):
    return ''.join(f'<details class="faq-item"><summary>{esc(q)}<span class="faq-plus" aria-hidden="true"></span></summary><div class="faq-answer"><p>{esc(a)}</p></div></details>' for q,a in items)

def closing_cta(t='Primero, hablemos de tus opciones.', sub='Una consulta clara puede ayudarte a tomar una mejor decisión. Sin obligación de contratar.'):
    return f'''<section class="final-cta"><div class="container cta-layout"><div>{mini_label('SIGUIENTE PASO')}<h2>{esc(t)}</h2><p>{esc(sub)}</p></div><div><a class="btn btn-lime btn-big" href="{wa('Hola, quiero conocer las opciones disponibles para mi organismo.') }" target="_blank" rel="noopener noreferrer">Consultar por WhatsApp <span aria-hidden="true">↗</span></a><small>La consulta no implica aprobación de crédito.</small></div></div></section>'''

def card(line, index=None):
    return f'''<a class="line-card" href="{path(line['slug'])}"><div class="line-card-head"><span class="line-icon" aria-hidden="true">{esc(line['icon'])}</span><span class="line-arrow" aria-hidden="true">↗</span></div><div class="line-card-meta">{esc(line['group'])}</div><h3>{esc(line['short'])}</h3><p>{esc(line['summary'])}</p><span class="text-link">Ver esta línea <span aria-hidden="true">→</span></span></a>'''

def home():
    options=''.join(f'<option value="{path(l["slug"])}">{esc(l["short"])}</option>' for l in LINES)
    featured_slugs=['prestamos-empleados-publicos','prestamos-fuerzas-armadas','prestamos-fuerzas-de-seguridad','prestamos-para-docentes-y-auxiliares','prestamos-personal-salud','prestamos-jubilados-pensionados-ips']
    featured=''.join(card(LINE_BY_SLUG[s]) for s in featured_slugs)
    small_lines=''.join(f'<a class="chip-link" href="{path(l["slug"])}">{esc(l["short"])} <span aria-hidden="true">↗</span></a>' for l in LINES if l['slug'] not in featured_slugs)
    return f'''
<section class="home-hero"><div class="container home-hero-grid">
<div class="hero-copy">{mini_label('PRÉSTAMOS · DESCUENTO DE HABERES')}<h1>Hacer planes empieza por <em>tener claridad.</em></h1>
<p class="hero-lead">Te ayudamos a consultar opciones de financiación para quienes trabajan o trabajaron en el sector público. Información directa, atención personal y decisiones a tu ritmo.</p>
<div class="hero-buttons"><a class="btn btn-dark btn-big" href="#lineas">Explorar líneas <span aria-hidden="true">↗</span></a><a class="subtle-link" href="#como-funciona">Conocé cómo funciona <span aria-hidden="true">↓</span></a></div>
<div class="hero-notice"><span class="circle-check" aria-hidden="true">✓</span><span>Consulta inicial gratuita. Cada préstamo está sujeto a aprobación crediticia.</span></div>
</div>
<div class="hero-art"><div class="art-orbit orbit-one"></div><div class="art-orbit orbit-two"></div><div class="art-shape art-shape-a"></div><div class="art-shape art-shape-b"></div>
<div class="selector-card"><div class="selector-top"><span class="micro-tag"><span class="mini-signal"></span> ENCONTRÁ TU LÍNEA</span><span class="selector-index">01 / 03</span></div>
<div class="selector-illustration" aria-hidden="true"><div class="ill-tile tile-left"><span>✓</span><span></span><span></span></div><div class="ill-coin"><span>+</span></div><div class="ill-tile tile-right"><span>↗</span><span></span><span></span></div></div>
<h2>¿En qué sector trabajás?</h2><p>Elegí tu actividad para ver información relevante.</p>
<form class="selector-form" id="sector-form"><label class="field-label" for="sector-select">TU SECTOR</label><div class="select-wrap"><select id="sector-select" name="sector" required><option value="">Seleccioná una opción</option>{options}</select><span aria-hidden="true">⌄</span></div><button type="submit" class="btn btn-lime btn-block">Ver opciones para mí <span aria-hidden="true">↗</span></button><div class="form-feedback" id="selector-message" role="status" aria-live="polite"></div></form>
<div class="selector-foot">Cada consulta se evalúa de forma individual.</div>
</div><div class="art-sticker"><span class="sticker-dot"></span> ASESORAMIENTO HUMANO</div></div>
</div></section>
<section class="trust-strip"><div class="container trust-grid"><div><span class="trust-icon" aria-hidden="true">01</span><p><strong>Escuchamos tu caso</strong><span>Sin respuestas genéricas</span></p></div><div><span class="trust-icon" aria-hidden="true">02</span><p><strong>Te explicamos las opciones</strong><span>Con condiciones para comparar</span></p></div><div><span class="trust-icon" aria-hidden="true">03</span><p><strong>Vos decidís</strong><span>Sin presiones ni compromiso</span></p></div></div></section>
<section id="lineas" class="section section-lines"><div class="container"><div class="section-header"><div>{mini_label('HECHO PARA TU ACTIVIDAD')}<h2>Una línea de crédito<br>para cada <em>realidad.</em></h2></div><p>El punto de partida es conocer tu organismo. Explorá las opciones y descubrí qué conviene consultar antes de iniciar una gestión.</p></div><div class="lines-grid">{featured}</div>
<div class="more-lines"><h3>¿Buscás tu organismo específico?</h3><p>También tenemos información para estas áreas y fuerzas.</p><div class="chip-list">{small_lines}</div></div></div></section>
<section id="como-funciona" class="process-section"><div class="container process-layout"><div class="process-intro">{mini_label('SIN VUELTAS INNECESARIAS')}<h2>Un proceso simple.<br><em>Una decisión informada.</em></h2><p>No necesitás saber de finanzas para empezar. Nuestro trabajo es ayudarte a entender el recorrido y las condiciones antes de avanzar.</p><a href="/guia-descuento-de-haberes/" class="light-outline-link">Entender el descuento de haberes <span aria-hidden="true">↗</span></a></div><div class="steps-list">
<div class="step"><span class="step-no">01</span><div><h3>Contanos tu situación</h3><p>Elegí tu sector y consultá por WhatsApp. Te orientamos sobre la documentación y alternativas que podrían aplicar.</p></div></div>
<div class="step"><span class="step-no">02</span><div><h3>Conocé las condiciones</h3><p>La entidad evalúa la solicitud. Pedí que te expliquen el importe, las cuotas, el CFT y el total a devolver.</p></div></div>
<div class="step"><span class="step-no">03</span><div><h3>Elegí si querés avanzar</h3><p>Solo si aceptás una propuesta, se continúa con el trámite. La entidad otorgante define la aprobación y acreditación.</p></div></div>
</div></div></section>
<section class="section clarity-section"><div class="container clarity-grid"><div><div class="clarity-shape"><div class="clarity-label">PARA DECIDIR<br>MEJOR.</div><div class="clarity-disc"><span>?</span></div><div class="clarity-caption">Preguntar también es avanzar.</div></div></div><div>{mini_label('INFORMACIÓN QUE IMPORTA')}<h2>Antes de firmar, <em>entendé cada número.</em></h2><p>Una cuota conveniente no cuenta toda la historia. Compará el costo real y revisá quién te presta el dinero, cómo se paga y qué opciones tenés.</p>
<ul class="check-list"><li><span>✓</span> Monto neto que vas a recibir</li><li><span>✓</span> Cuota, plazo y costo financiero total (CFT)</li><li><span>✓</span> Entidad otorgante y condiciones del contrato</li><li><span>✓</span> Opciones de cancelación anticipada</li></ul><a href="/preguntas-frecuentes/" class="text-link larger">Ver preguntas frecuentes <span aria-hidden="true">↗</span></a></div></div></section>
<section class="section faq-section"><div class="container faq-layout"><div>{mini_label('RESPUESTAS CLARAS')}<h2>¿Te quedó alguna <em>duda?</em></h2><p>Acá van las preguntas que conviene resolver antes de empezar.</p><a href="/preguntas-frecuentes/" class="text-link">Ver todas las respuestas <span aria-hidden="true">↗</span></a></div><div class="faq-list">{faq_html(FAQ[:5])}</div></div></section>
{closing_cta()}'''

def crumb(slug,title):
    return f'<nav class="crumb" aria-label="Migas de pan"><a href="/">Inicio</a><span aria-hidden="true">/</span><a href="/#lineas">Líneas</a><span aria-hidden="true">/</span><span aria-current="page">{esc(title)}</span></nav>'

def line_page(l):
    wa_msg=f'Hola, quisiera consultar opciones para {l["short"]}. ¿Me pueden orientar?'
    how=f'''<div class="cond-row"><span>¿Para quién?</span><strong>{esc(l['audience'])}</strong></div><div class="cond-row"><span>Operatoria</span><strong>Descuento de haberes, si está habilitado para tu organismo.</strong></div><div class="cond-row"><span>Normativa</span><strong>{esc(l['legal'])}</strong></div><div class="cond-row"><span>Costos y cuotas</span><strong>Se informan en una propuesta de la entidad otorgante.</strong></div><div class="cond-row"><span>Aprobación</span><strong>Sujeta a evaluación crediticia y margen disponible.</strong></div>'''
    related=''.join(card(LINE_BY_SLUG[s]) for s in l['related'])
    specific=[
      (f'¿Quiénes pueden consultar por esta línea de {l["short"]}?', l['audience']+' La disponibilidad se confirma caso por caso.'),
      ('¿Cómo sé qué monto me corresponde?', 'No se puede establecer sin revisar las condiciones de la entidad, el margen de descuento disponible y tu perfil. Antes de decidir, solicitá una propuesta por escrito.'),
      ('¿Tengo que contratar al consultar?', 'No. Podés pedir información y comparar alternativas. Consultar no te obliga a firmar ni garantiza la aprobación.'),
    ]
    return f'''<section class="subhero"><div class="container">{crumb(l['slug'],l['short'])}<div class="subhero-layout"><div>{mini_label(l['group'].upper())}<h1>{esc(l['title'])}<span class="h1-period">.</span></h1><p class="subhero-lead">{esc(l['summary'])}</p><div class="hero-buttons"><a class="btn btn-dark btn-big" href="{wa(wa_msg)}" target="_blank" rel="noopener noreferrer">Consultar mi caso <span aria-hidden="true">↗</span></a><a class="subtle-link" href="#requisitos">Ver requisitos <span aria-hidden="true">↓</span></a></div><p class="legal-small">Consulta sin compromiso. No implica oferta ni aprobación de crédito.</p></div>
<div class="subhero-art" aria-hidden="true"><span class="s-art-kicker">CREDISNET / LÍNEA {esc(l['code'])}</span><span class="s-art-mark">{esc(l['icon'])}</span><span class="s-art-group">{esc(l['short'])}</span><div class="s-art-orbit"></div><div class="s-art-bottom">TU ACTIVIDAD. TUS OPCIONES. <span>↗</span></div></div></div></div></section>
<section class="section conditions-section"><div class="container conditions-grid"><div>{mini_label('INFORMACIÓN ESENCIAL')}<h2>¿Cómo funciona esta <em>línea?</em></h2><p>La disponibilidad depende de cada organismo, del convenio aplicable y de la evaluación de la entidad. Esta información es orientativa y no reemplaza una propuesta formal.</p><div class="note-card"><span class="note-symbol">i</span><div><strong>Credisnet acompaña tu solicitud.</strong><p>La entidad otorgante evalúa, aprueba, acredita el dinero y administra el crédito.</p></div></div></div><div class="conditions-table">{how}</div></div></section>
<section class="section docs-section" id="requisitos"><div class="container docs-layout"><div>{mini_label('PARA EMPEZAR')}<h2>La información que pueden <em>solicitarte.</em></h2><p>Los requisitos específicos varían. Consultá primero y verificá el canal antes de compartir datos personales.</p></div><div class="docs-panel"><ul class="document-list"><li><span>01</span> DNI vigente</li><li><span>02</span> Recibo de haberes reciente</li><li><span>03</span> Constancia o certificado del organismo, si corresponde</li><li><span>04</span> CBU de una cuenta a nombre del solicitante</li></ul><p class="doc-footnote">Nunca realices pagos anticipados para “asegurar” una aprobación. Pedí información sobre quién solicita tus datos y con qué finalidad.</p></div></div></section>
<section class="section faq-section"><div class="container faq-layout"><div>{mini_label('CONSULTAS FRECUENTES')}<h2>Antes de <em>avanzar.</em></h2><p>Estas respuestas son orientativas. Tu propuesta final depende de la entidad otorgante.</p></div><div class="faq-list">{faq_html(specific)}</div></div></section>
<section class="section related-section"><div class="container">{mini_label('SEGUÍ EXPLORANDO')}<h2>Otras líneas que podrían interesarte.</h2><div class="lines-grid related-grid">{related}</div></div></section>
{closing_cta('Tu próxima decisión puede empezar con una pregunta.', 'Consultá la línea para '+l['short']+'. Te ayudamos a entender los pasos y condiciones disponibles.')}'''

def generic_hero(title,eyebrow,lead):
    return f'''<section class="general-hero"><div class="container">{mini_label(eyebrow)}<h1>{esc(title)}<span class="h1-period">.</span></h1><p>{esc(lead)}</p></div></section>'''

def faq_page():
    c=generic_hero('Preguntas frecuentes','LO IMPORTANTE, SIN LETRA CHICA','Las respuestas que te ayudan a comparar, entender y tomar una decisión informada.')
    c+=f'''<section class="section"><div class="container narrow"><div class="faq-list">{faq_html()}</div><div class="inline-support"><h2>¿Tenés una situación particular?</h2><p>Consultanos qué información necesitamos para orientarte en tu caso.</p><a class="btn btn-dark" href="{wa('Hola, tengo una pregunta sobre préstamos por descuento de haberes.') }" target="_blank" rel="noopener noreferrer">Hacer una consulta <span aria-hidden="true">↗</span></a></div></div></section>'''
    return c

def about_page():
    c=generic_hero('Personas primero. Decisiones claras.','QUÉ HACEMOS Y CÓMO TRABAJAMOS','Credisnet acompaña la gestión comercial de solicitudes de préstamos destinadas a quienes trabajan o trabajaron en el sector público argentino.')
    c+='''<section class="section"><div class="container about-grid"><div class="about-emblem"><span>HABLAR CLARO<br>ES EMPEZAR<br>BIEN.</span><div>↗</div></div><div>'''+mini_label('NUESTRA FORMA DE TRABAJAR')+'''<h2>La confianza empieza por entender.</h2><p>Sabemos que cada recibo y cada situación es diferente. Por eso organizamos la información por sector y explicamos el proceso antes de que decidas avanzar.</p><p>Credisnet actúa como intermediario comercial y gestor del legajo. No sustituye la evaluación ni la propuesta contractual de la entidad financiera otorgante.</p><ul class="check-list"><li><span>✓</span> Orientación según organismo</li><li><span>✓</span> Gestión y consultas digitales</li><li><span>✓</span> Condiciones sujetas a evaluación individual</li></ul></div></div></section>'''
    c+=closing_cta('Conocé las opciones de tu sector.','Podés hacer tu primera consulta sin obligación de contratar.')
    return c

def contact_page():
    c=generic_hero('Hablemos de tu consulta.','CONTACTO','Elegí el canal de consulta y contanos para qué organismo trabajás o de cuál te jubilaste. No hace falta enviar documentos personales en el primer mensaje.')
    c+=f'''<section class="section"><div class="container contact-grid"><div class="contact-card"><span class="contact-icon">↗</span><h2>WhatsApp</h2><p>Consultá por una línea, requisitos o cómo funciona el descuento de haberes. Atención comercial personalizada.</p><a class="btn btn-dark" href="{wa('Hola, quiero iniciar una consulta con Credisnet.') }" target="_blank" rel="noopener noreferrer">Abrir WhatsApp <span aria-hidden="true">↗</span></a><small>Canal definido en configuración. Confirmar titularidad antes de publicar.</small></div><div class="contact-card contact-card-light"><span class="contact-icon">?</span><h2>Antes de escribirnos</h2><p>Tené a mano el nombre de tu organismo y tu situación laboral. Un asesor te indicará si hace falta documentación adicional, siempre por un canal verificado.</p><a class="text-link" href="/preguntas-frecuentes/">Consultar preguntas frecuentes <span aria-hidden="true">↗</span></a></div></div></section>'''
    return c

def guide_page():
    c=generic_hero('Descuento de haberes, explicado.','GUÍA PRÁCTICA','Qué significa esta modalidad, cómo se analiza y qué deberías verificar antes de aceptar un préstamo.')
    sections=[('01','Qué es el descuento de haberes','Es una modalidad de pago de cuotas en la que se autoriza una deducción del haber, según las reglas del organismo y el convenio aplicable. No todos los organismos ni todas las personas tienen las mismas condiciones.'),('02','Quién define el crédito','La entidad otorgante analiza requisitos, margen, perfil y política crediticia; también fija tasas, cargos y plazos. Credisnet interviene en el asesoramiento y la gestión de la solicitud.'),('03','Qué datos revisar en una propuesta','Compará el monto que realmente recibirías, el importe y número de cuotas, la tasa, el Costo Financiero Total (CFT), el monto total a devolver y las condiciones de cancelación anticipada.'),('04','Qué pasa si no es aprobado','Una consulta o un margen aparente no garantizan el otorgamiento. Si una entidad rechaza la solicitud, pedí orientación sobre los motivos generales y evitá enviar documentación a terceros no verificados.')]
    c+='<section class="section"><div class="container guide-layout"><div class="guide-toc">'+mini_label('EN ESTA GUÍA')+'<p>Informate antes de comprometer tus haberes.</p></div><div class="guide-steps">'
    c+=''.join(f'<article class="guide-row"><span>{n}</span><div><h2>{esc(h)}</h2><p>{esc(p)}</p></div></article>' for n,h,p in sections)
    c+='''<div class="guide-notice"><strong>Nota importante</strong><p>La disponibilidad de una línea y sus condiciones dependen de normativa, convenios y aprobación. Esta guía es informativa, no asesoramiento legal o financiero personalizado.</p></div></div></div></section>'''
    c+=closing_cta('Entendé tus opciones antes de elegir.','Elegí tu sector y consultá la información disponible sin compromiso.')
    return c

def terms_page():
    c=generic_hero('Términos y condiciones','INFORMACIÓN LEGAL','Condiciones generales de uso del sitio y de la información sobre solicitudes de crédito.')
    terms=[('Objeto del sitio','Este sitio proporciona información general sobre la intermediación comercial y la gestión de solicitudes de préstamos por descuento de haberes. No constituye una oferta de crédito ni una garantía de disponibilidad.'),('Rol de Credisnet','Credisnet se presenta como comercializadora y gestora de solicitudes. La entidad otorgante es la responsable de evaluar, aprobar o rechazar, formalizar y acreditar el crédito, conforme a la normativa y contratos aplicables.'),('Condiciones crediticias','Los montos, tasas, costos, plazos, cuotas y demás condiciones corresponden a la propuesta de la entidad otorgante. El usuario debe consultar el CFT, contrato y documentación antes de aceptar.'),('Información del usuario','Para recibir asesoramiento, el usuario debe aportar información veraz. No deben enviarse claves, contraseñas ni códigos de autenticación.'),('Disponibilidad y cambios','El contenido puede actualizarse y ciertas operatorias pueden cambiar o dejar de estar disponibles. La información visible puede no reflejar en tiempo real todas las condiciones crediticias.'),('Limitaciones','El uso del sitio y el inicio de una consulta no constituyen aprobación, preaprobación ni una obligación de contratación.')]
    c+='<section class="section"><div class="container narrow legal-copy"><p class="legal-alert"><strong>Revisión previa a publicación:</strong> este texto es una base informativa de trabajo y debe ser validado por el responsable legal de Credisnet antes de reemplazar condiciones vigentes.</p>'
    c+=''.join(f'<section><h2>{esc(h)}</h2><p>{esc(p)}</p></section>' for h,p in terms)
    c+='</div></section>'
    return c

def privacy_page():
    c=generic_hero('Política de privacidad','DATOS PERSONALES','Información general sobre el tratamiento de datos al utilizar este sitio y contactar al equipo comercial.')
    sections=[('Qué recopila este sitio','Esta versión estática no dispone de un formulario propio, una cuenta de usuario ni una base de datos de clientes. Al abrir WhatsApp, la conversación se gestiona en un servicio externo con sus propias condiciones y políticas.'),('Datos de la consulta','Si enviás información por WhatsApp, el responsable de la atención recibirá los datos y mensajes que decidas compartir. Evitá enviar DNI, CBU, recibos u otros documentos sensibles en el primer contacto sin verificar el canal.'),('Finalidades','La información proporcionada voluntariamente se utilizaría para responder consultas, orientar sobre requisitos y gestionar solicitudes cuando expresamente decidas continuar. La finalidad y los responsables deben informarse de manera específica antes de pedir documentos.'),('Cookies y medición','El sitio entregado no incorpora cookies publicitarias, rastreadores de terceros ni analítica de visitantes. Si posteriormente se integran servicios de medición, debe actualizarse esta política y evaluar el consentimiento que corresponda.'),('Derechos y contacto','Las solicitudes de acceso, rectificación y supresión deben canalizarse ante el responsable de los datos. Antes de publicar esta política, se deben incorporar los datos identificatorios, canales formales, plazos y demás información exigida por la normativa aplicable.')]
    c+='<section class="section"><div class="container narrow legal-copy"><p class="legal-alert"><strong>Revisión previa a publicación:</strong> incorporar razón social, datos del responsable, contacto específico para privacidad, proveedores y verificación legal antes de usar este texto como política definitiva.</p>'
    c+=''.join(f'<section><h2>{esc(h)}</h2><p>{esc(p)}</p></section>' for h,p in sections)
    c+='</div></section>'
    return c

pages={'':('Préstamos por descuento de haberes','Orientación sobre préstamos por descuento de haberes para empleados públicos, fuerzas, docentes, personal de salud y jubilados. Consultá tus opciones.',home())}
for l in LINES:
    pages[l['slug']]=(l['title'],l['summary'],line_page(l))
pages.update({
  'preguntas-frecuentes':('Preguntas frecuentes sobre préstamos','Respuestas claras sobre descuento de haberes, requisitos, costos, aprobación y condiciones de préstamos para el sector público.',faq_page()),
  'quienes-somos':('Quiénes somos','Conocé el enfoque de Credisnet para gestionar solicitudes de préstamos por descuento de haberes de forma clara y personalizada.',about_page()),
  'contacto':('Contacto y asesoramiento','Consultá opciones de préstamos para tu sector por WhatsApp. Una conversación para entender tus alternativas antes de decidir.',contact_page()),
  'guia-descuento-de-haberes':('Qué es el descuento de haberes','Guía sencilla para comprender los préstamos por descuento de haberes, los requisitos y qué revisar antes de firmar.',guide_page()),
  'terminos-y-condiciones':('Términos y condiciones','Información general sobre el uso del sitio y el rol de Credisnet como gestor comercial de solicitudes.',terms_page()),
  'politica-de-privacidad':('Política de privacidad','Cómo se tratan los datos al navegar el sitio y consultar por WhatsApp. Política pendiente de revisión legal.',privacy_page()),
})

for slug, (title,desc,body) in pages.items():
    target= DOCS / slug / 'index.html' if slug else DOCS / 'index.html'
    target.parent.mkdir(parents=True,exist_ok=True)
    extra=None
    if slug in LINE_BY_SLUG:
        l=LINE_BY_SLUG[slug]
        extra={'@context':'https://schema.org','@type':'Service','name':l['title'],'description':l['summary'],'provider':{'@type':'Organization','name':'Credisnet','url':DOMAIN+'/'} ,'areaServed':{'@type':'Country','name':'Argentina'},'serviceType':'Gestión comercial de solicitudes de préstamos por descuento de haberes'}
    target.write_text(base_page(title,desc,slug,body,extra_schema=extra),encoding='utf-8')

# Sitemap y robots: rutas con slash final para Cloudflare Pages, sin fechas de modificación inventadas.
(DOCS/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{esc(url(slug))}</loc></url>\n' for slug in pages)+'</urlset>\n',encoding='utf-8')
(DOCS/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+DOMAIN+'/sitemap.xml\n',encoding='utf-8')
(DOCS/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Content-Security-Policy: default-src \'self\'; img-src \'self\' data:; style-src \'self\'; script-src \'self\'; connect-src \'self\'; font-src \'self\'; frame-ancestors \'none\'; base-uri \'self\'; form-action \'self\'; object-src \'none\'\n',encoding='utf-8')
(DOCS/'_redirects').write_text('''# Opcional: verificar la lista de redirecciones históricas del repositorio de producción antes de migrar.
/prestamos/ /#lineas 301
/preguntas-frecuentes.html /preguntas-frecuentes/ 301
''',encoding='utf-8')
(DOCS/'404.html').write_text(base_page('Página no encontrada','La página que buscabas no existe en esta dirección.','404', '<section class="general-hero"><div class="container"><p class="error-num">404</p><h1>Esta página no está por acá.</h1><p>Volvé al inicio para encontrar las líneas disponibles.</p><a class="btn btn-dark" href="/">Ir al inicio <span aria-hidden="true">↗</span></a></div></section>').replace('<meta name="robots" content="index,follow,max-image-preview:large">','<meta name="robots" content="noindex,follow">').replace('<link rel="canonical" href="'+DOMAIN+'/404/">',''),encoding='utf-8')
print(f'Sitio generado: {len(pages)} páginas indexables, 404, CSS, JS, SEO y cabeceras Cloudflare.')
