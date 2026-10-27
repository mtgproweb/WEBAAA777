# Credisnet v4 — sitio TOTALMENTE NUEVO desde cero (SOLO PARA PRUEBA)

Este no es el sitio viejo con otro CSS. HTML, CSS y copy son nuevos, escritos para v4.
Solo se respetó el logo existente y los hechos verificados (montos, decretos, cargos, organismos, contacto, legales en fondo).

## Arquitectura nueva (13 páginas, no 25 clonadas)
- Home: https://www.credisnet.com.ar/
- Empleados públicos: /empleados-publicos/ (nacionales, salud $6.000.000, penitenciario bonaerense $10.000.000)
- Docentes DGCyE: /docentes-dgcye/ ($10.000.000, 6 cargos explícitos)
- IPS y jubilados: /ips-jubilados/ ($10.000.000)
- Fuerzas Armadas: /fuerzas-armadas/ ($20.000.000: Ejército, Armada, Fuerza Aérea)
- Fuerzas de Seguridad: /fuerzas-seguridad/ ($20.000.000: PFA, Gendarmería, Prefectura, PSA, SPF)
- Policía: /policia/ (Provincia $6.000.000, Ciudad $10.000.000, sin mezclar)
- Retirados y Caja: /retirados-caja/ ($20.000.000, 11 organismos)
- Quiénes somos: /quienes-somos/
- Preguntas frecuentes: /preguntas-frecuentes/
- Legales: /politica-privacidad/, /terminos-condiciones/, /informacion-financiera/

Cada página de grupo tiene: hero propio, para quién es, monto orientativo, requisitos, 3 pasos y CTA final.
Home en 10 segundos: qué es, para quién es, montos orientativos, cómo se paga, 3 pasos, CTA.

## Diseño nuevo (por qué puede ser un éxito)
- Paleta propia: azul marino #0F2A44, verde #0EA47A, ámbar #FFC53D para montos y acentos, fondo blanco y secciones #EEF2F7.
- Tipografía propia: Sora para títulos, Inter para texto, base 18px (17px en móvil), interlineado 1,65.
- Mobile-first, header simple con pocos enlaces para que no apriete el menú, CTA de WhatsApp grande desde el primer pantallazo, botón flotante, sin carrusel infinito que corte tarjetas, sin secciones interminables repetidas.
- Sin fotos con uniformes ni insignias oficiales: solo el logo original y formas/colores CSS. Así no parece un sitio oficial.
- Un solo CSS nuevo (docs/assets/style.css) y un JS mínimo (menú móvil + aria), sin frameworks pesados.

## Qué prácticas del prompt SEO/CRO apliqué (adaptadas, no copiadas)
APLIQUÉ:
- SEO on-page: títulos con keyword adelante, todos ≤60 caracteres; metas únicas por página, todas ≤155, empezando con verbo (Consultá, Conocé, Resolvé, Leé, Entendé) y cerrando con "¡Consulta tu disponible ahora!".
- Jerarquía H1/H2 clara y respuesta directa arriba: cada página tiene "En pocas palabras" con 40-50 palabras que responde quién, qué y cómo.
- FAQ semántica: FAQ visible con <details> y schema FAQPage en las páginas que tienen FAQ, con el mismo texto visible y en schema.
- Schema JSON-LD completo: Organization, WebSite, WebPage, BreadcrumbList, Service en páginas de grupo y FAQPage donde corresponde.
- CRO suave para préstamos: CTA "¡Consulta tu disponible ahora!" por WhatsApp, siempre con "Sujeto a aprobación crediticia", sin CTA duro tipo "Buy Now", sin inventar montos, tasas ni plazos.
- Copy PAS suave: home ("¿Te pasa esto?") y retirados ("Con calma, sin apuro"), sin presión ni miedo, especialmente con público vulnerable.
- Copy escaneable: párrafos cortos, bullets, tarjetas, pasos en 3, secciones cortas.
- Tecnología actual: HTML semántico (header/nav/main/footer/section), CSS moderno sin frameworks, JS mínimo, una sola imagen (el logo, 8,2 KB), sin librerías innecesarias, fuentes con display=swap, responsive real.
- Accesibilidad: alto contraste (texto oscuro sobre fondo claro), foco visible con ámbar, enlace "Saltar al contenido", alt en el logo, aria-expanded/aria-controls en el menú móvil, FAQ nativa accesible.
- Performance / Core Web Vitals: sin carrusel con JS pesado, sin imágenes grandes, CSS único pequeño, JS de 272 bytes, sin shifts por logo con width/height.

DESCARTÉ (y por qué):
- CTA duro de compra ("Buy Now" y similares): no aplica a préstamos y genera desconfianza; se reemplazó por consulta por WhatsApp.
- Comparaciones objetivas de blog y tablas complejas: no aplican a este sitio de conversión y alargan sin vender; se usaron tarjetas y listas simples.
- Copiar el prompt en inglés o su estructura tal cual: se adaptó todo a español rioplatense, HTML estático y a las reglas duras de Credisnet.
- Cualquier cosa que contradiga montos, decretos, cargos, organismos, legales o el logo: descartado siempre.

## Qué hechos mantuve (sin inventar nada)
- Montos orientativos y hasta 36 cuotas fijas, según evaluación y sujeto a aprobación de la entidad otorgante.
- Decretos 352/2026 nacional y 988/2021 Provincia de Buenos Aires.
- Docentes: DOCENTE TITULAR, DOCENTE TITULAR INTERINO, DOCENTE PROVISIONAL, DOCENTE SUPLENTE, AUXILIAR TITULAR, AUXILIAR MENSUALIZADO.
- Caja: 11 organismos (PFA, PNA, Gendarmería, PSA civil y seguridad, SPF, Personal Civil de Inteligencia FFAA, Personal Militar FFAA, Policía de Establecimientos Navales según anexos, AFI, SIDE, SINEP), $20.000.000. Nunca "un crédito por mes" (verificado ausente).
- Requisitos: DNI vigente, último recibo, comprobante de servicios, CBU, certificado de haberes. Acreditación en cuenta, en el día hábil o 24-48 h hábiles según documentación.
- Contacto real: WhatsApp https://wa.me/541122845514, 11 6970-7265, info@credisnet.com. Sin formularios que envíen datos.
- Legales nuevos y serios en fondo (Ley 25.326, BCRA, CFT, TNA), sin copiar los textos viejos palabra por palabra y sin inventar CUIT, dirección ni otros datos de empresa que no se tienen.

## Validación
- scripts/validate_site.py (nuevo para v4): OK, 13 HTML, 13 URLs en sitemap, enlaces internos válidos.
- Títulos únicos, todos ≤60; metas únicas, todas ≤155; respuesta directa 40-50 palabras en las 13 páginas; sitemap = páginas; sin enlaces a páginas viejas; sin "un crédito por mes".
- Caveat: no se hizo revisión visual renderizada en navegador en vivo por el subagente; conviene abrir la prueba en Pages y confirmar visualmente home, Docentes y Caja antes de cualquier paso a producción.
