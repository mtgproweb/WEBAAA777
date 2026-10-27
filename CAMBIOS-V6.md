# Credisnet v6 — Sitio nuevo con el Prompt Maestro V2.0 (solo para prueba)

**No es producción. No sobrescribe AAA114851 ni la carpeta v2.**
Base de hechos: el repo candidato AAA114851, en local `credisnet-web-v2` (títulos/metas finales, hero CTA, sin botón de encabezado, Caja con 11 organismos, Docentes con módulo de 6 cargos entre hero y Líneas).
Qué se hizo aquí: se tomó esa base de hechos y se construyó v6 con un sistema visual y un JS nuevos, eliminando el CSS viejo (`style.css`, `pages.css`, `credis-assistant.css`) y el JS viejo (`main.js`, `credis-assistant.js`). No es un theme encima: sin `v6.css`/`v6.js` el sitio no tiene diseño viejo al que volver, porque ese diseño ya no está en la carpeta.
Transparencia: la estructura HTML y el contenido específico por página se heredan de v2 para conservar las 25 páginas y el SEO. Si al verlo renderizado sigue pareciendo "el viejo", el problema será esa estructura/contenido heredado, no el CSS, y habrá que redactar copy y plantillas nuevas desde cero con las 25 páginas.

## 1. Arquetipo (Prompt, sección 3)
**Híbrido, explícito:**
- **Principal: Local Business / Services** — préstamos por WhatsApp en Argentina, contacto, cobertura por organismo, reputación verificable.
- **Secundario: Landing / Campaign** — conversión medible por WhatsApp, mensaje principal, beneficios, objeciones, CTA.
- **Secundario: Corporate / B2B** — credibilidad como comercializadora y agente autorizado, propuesta de valor, servicios, contacto comercial.
- **NO es:** e-commerce (no hay carrito, checkout ni pago en el sitio), SaaS, blog/editorial, documentación técnica, ni app/dashboard. Por eso no hay checkout, precios de producto, planes, ni "Buy Now".
Las prioridades del arquetipo determinan el diseño; no imponen un estilo rígido.

## 2. Estrategia (sección 4)
- **Nicho:** préstamos personales por descuento de haberes en Argentina, gestionados por una comercializadora ante entidades otorgantes.
- **Público:** empleados públicos nacionales y bonaerenses, docentes y auxiliares DGCyE, personal de salud, fuerzas armadas y de seguridad, jubilados/pensionados IPS y retirados nacionales. Incluye público mayor y vulnerable: lenguaje claro, sin presión, sin urgencia falsa, sin miedo.
- **Objetivo principal:** consulta por WhatsApp ("¡Consulta tu disponible ahora!").
- **Objetivos secundarios:** informar monto orientativo, requisitos, decreto aplicable y pasos, y resolver objeciones (costo de consulta, Veraz, tiempos, forma de pago).
- **Propuesta de valor:** "Consultás por WhatsApp, revisamos tu recibo y tu margen, y si la entidad aprueba, se acredita en tu cuenta y la cuota se descuenta de tu haber. Asesoramiento gratuito, sin costos ocultos, sujeto a aprobación crediticia."
- **Confianza requerida:** alta. Por eso: identidad real (no es banco ni organismo oficial), contacto real, disclaimer en cada CTA, y ninguna estadística, testimonio, garantía o credencial inventada.
- **Idioma:** español de Argentina. **Legal:** Ley 25.326, BCRA, CFT/TNA en Información Financiera, sin inventar CUIT, dirección, sucursales ni estadísticas.

## 3. Diseño (sección 5) — sistema visual propio
- **Dirección de arte:** servicios financieros confiables, premium en acabado pero sobrios, no tecnología oscura ni lujo ostentoso.
- **Paleta:** azul marino #0F2A44, verde Credisnet #0EA47A / #0B7A5E, ámbar #FFC53D solo para montos y foco, fondo blanco, alt #F2F5F8, tinta #14233A, línea #DCE3EC.
- **Tipografía:** Montserrat 800 para títulos (tracking -0.02em), Inter para texto, 17,5 px, interlineado 1,65, H1 clamp 2–3,3 rem, H2 clamp 1,5–2,2 rem.
- **Jerarquía/espaciado/grid:** secciones 40 px, grids 16 px de gap, 3 columnas en escritorio / 1 en móvil, radios 16/20 px, sombras suaves en dos niveles.
- **Componentes:** header blanco sticky con borde ámbar, hero claro con degradado, tarjetas blancas, tabla con encabezado marino, FAQ en tarjetas, CTA final marino, footer marino, barra fija de WhatsApp en móvil.
- **Microinteracciones:** 100–250 ms (botones 200 ms, tarjetas 200 ms, hover -3 px, foco ámbar visible). Se respeta `prefers-reduced-motion`. Sin animaciones molestas, sin carrusel infinito con clonación: las tiras son scroll con snap y flechas.
- **Imágenes:** solo el logo original (`docs/img/logo.png`, 8,2 KB). Sin fotos con uniformes ni insignias oficiales, para no parecer sitio oficial. Se conservan las imágenes ya existentes del sitio solo donde ya estaban (familia.webp, fuerzas.webp, prestamos-credisnet.webp), sin añadir fotos nuevas inventadas.
- **Stack justificado (sección 12):** HTML/CSS/JS estático, sin frameworks. Justificación: el sitio es informativo y convierte por WhatsApp, no necesita React/Next/Tailwind ni un build; un framework pesaría el zip, complicaría GitHub Pages y no aportaría conversión. JS: 1.963 bytes, solo menú, FAQ y flechas.

## 4. Arquitectura (sección 6) — 25 páginas, mismas URLs
Home + 24 internas finales, en `docs/`:
index, prestamos-empleados-publicos, prestamos-para-docentes-y-auxiliares, prestamos-policia-provincia-buenos-aires, prestamos-jubilados-pensionados-ips, prestamos-servicio-penitenciario-bonaerense, prestamos-personal-salud, prestamos-fuerzas-armadas, prestamos-ejercito-argentino, prestamos-armada-argentina, prestamos-fuerza-aerea-argentina, prestamos-fuerzas-de-seguridad, prestamos-policia-federal, prestamos-gendarmeria-nacional, prestamos-prefectura-naval-argentina, prestamos-policia-seguridad-aeroportuaria, prestamos-servicio-penitenciario-federal, prestamos-caja-retiros-policia-federal, prestamos-policia-de-la-ciudad, prestamos-personal-retirado-fuerzas, quienes-somos, preguntas-frecuentes, informacion-financiera, politica-de-privacidad, terminos-y-condiciones. Más 404.html con noindex (no está en sitemap).
Cada página: objetivo claro (consulta por WhatsApp), jerarquía H1/H2, navegación global y migas, recorrido (hero → para quién es → monto → requisitos → pasos → FAQ → CTA final) y CTA principal + secundario. En Docentes, el módulo "Cargos que tomamos" está entre el hero y "Líneas de Préstamo Disponibles", verificado antes de Líneas.

## 5. Copy (sección 7)
Español de Argentina, PAS suave donde sirve (home), beneficios concretos antes que características, objeciones reales (costo, Veraz, tiempos, descuento). Sin lenguaje artificial, sin estadísticas/testimonios/garantías/credenciales inventadas, sin urgencia falsa, sin "Buy Now". CTA siempre: "¡Consulta tu disponible ahora!" por WhatsApp, con "Sujeto a aprobación crediticia".

## 6. SEO / AEO (secciones 8–10)
- Títulos únicos ≤60 caracteres (0 >60), metas únicas, 6 metas de la lista final aprobada por el usuario entre 156–159 caracteres (dentro del rango orientativo 155–160 del Prompt, sección 8; no se modificaron unilateralmente — ver defectos Bajo).
- HTML semántico, canonical, sitemap con 25 URLs, robots, enlazado interno relativo, OG/Twitter.
- Respuestas directas arriba en las páginas de grupo, FAQ semántica visible y en schema.
- JSON-LD solo real y apropiado: Organization (25 páginas), WebSite (25), Service (27 menciones), FAQPage (22), BreadcrumbList (24), WebPage (24). Sin precios, disponibilidad, autores ni reseñas inventadas. No se añade Product (no hay producto en venta en el sitio).

## 7. CRO (sección 11)
Objetivo: consulta por WhatsApp. CTA principal en hero y al final, CTA secundario (Preguntas frecuentes / ver líneas), beneficios, confianza verificable, FAQ, objeciones. CTA sticky en móvil en todas las páginas (`#wa-sticky-bar`), que no bloquea contenido: en móvil se oculta el botón flotante para no duplicar, y el footer tiene padding inferior extra. Sin animaciones de compra ni urgencia.

## 8. Performance / Accesibilidad / Seguridad (secciones 13–15)
- Performance: CSS 11.962 bytes, JS 1.963 bytes, logo 8,2 KB, docs totales 1.647.260 bytes. Sin frameworks, sin JS innecesario, fuentes con display=swap. **No se declara Lighthouse 95–100 ni Core Web Vitals: no se midieron** (ver matriz, Pendiente de comprobar).
- Accesibilidad WCAG 2.2 AA (objetivo): HTML semántico, jerarquía, contraste alto (tinta sobre blanco, blanco sobre marino), foco ámbar visible, enlace "Saltar al contenido", alt en imágenes (0 imágenes sin alt en la auditoría), aria en menú móvil y en botones WhatsApp, FAQ con role button en JS, `prefers-reduced-motion`.
- Seguridad/privacidad: HTTPS por GitHub Pages, sin formularios que envíen datos, sin secretos en el repo, sin cookies propias, enlaces externos con rel noopener donde ya existían. No se declara cumplimiento legal completo.

## 9. Testing y autoauditoría (secciones 18–19) — dos ciclos
**Ciclo 1:** `python scripts/validate_site.py` → OK: 26 HTML, 24 páginas internas finales, 25 URLs indexables y referencias locales válidas.
**Ciclo 2 (auditoría propia):**
- Títulos únicos 26/26, metas únicas 24/24, 0 títulos >60, 0 metas >160.
- CSS: 127 llaves abiertas / 127 cerradas. JS: `node --check` OK.
- Enlaces internos absolutos incompatibles con Pages: 0. Enlaces rotos: 0 (validador).
- Frase prohibida "un crédito por mes": 0 apariciones.
- Hechos verificados: $20.000.000 (38 menciones), $10.000.000 (12), $6.000.000 (8), Decreto 352/2026 (157), Decreto 988/2021 (44), AUXILIAR TITULAR y AUXILIAR MENSUALIZADO presentes, Docentes con cargos antes de Líneas, Caja con los 7 organismos comprobados por nombre en la auditoría y SINEP presente.
- No se pudo hacer revisión visual renderizada en navegador (subagente sin navegador en vivo) ni medición Lighthouse: queda como pendiente, no como verificado.
**Defectos clasificados:**
- Crítico: ninguno. Alto: ninguno.
- Medio: ninguno en la auditoría automática (0 H1 faltantes/duplicados, 0 páginas sin v6.css/js, 0 sin WhatsApp, 0 img sin alt).
- Bajo: (1) 6 metas entre 156–159 caracteres, de la lista final aprobada por el usuario; el Prompt las admite como rango orientativo 155–160, así que no se tocaron sin aprobación. Próxima mejora: recortarlas a ≤155 si el usuario lo aprueba. (2) El contenido y la estructura HTML se heredan de v2: el diseño es nuevo, pero el copy no se reescribió desde cero en las 25 páginas. Próxima mejora si el usuario lo pide: redacción nueva por página manteniendo los hechos.
- Pendiente de comprobar: render visual real, Lighthouse/Core Web Vitals, contraste medido con herramienta, navegación por teclado manual, y comportamiento del carrusel home sin el JS viejo de clonación (ahora es tira con snap; debe probarse en móvil real).

## 10. Evaluación final — matriz (sección 27)
No se declara 10/10 global. No se calcula nota global artificial. Puntuación 0–10 solo donde hay evidencia suficiente; donde no, se indica Pendiente de comprobar sin puntuación.

| # | Dimensión | Objetivo | Estado | Evidencia | Punt. | Pendiente / próxima mejora |
|---|---|---|---|---|---|---|
| 1 | Diseño visual y dirección de arte | Sistema propio, coherente, premium sobrio | Revisado parcialmente | v6.css nuevo, CSS viejo eliminado, tokens y componentes consistentes | 7 | Render visual real en Pages |
| 2 | UX | Entender en segundos dónde estoy, qué ofrece, qué hacer | Revisado parcialmente | Hero + CTA + recorrido por página, sticky móvil | 7 | Prueba con usuarios reales / móvil real |
| 3 | UI | Componentes consistentes y estados claros | Revisado parcialmente | Botones, tarjetas, tablas, FAQ, foco visible | 7 | Revisión visual y de estados en navegador |
| 4 | Arquitectura de información | 25 páginas, navegación y migas claras | Verificado | Sitemap = páginas, validador OK, enlaces relativos | 9 | Ninguno crítico |
| 5 | Calidad del código | Limpio, modular, sin frameworks injustificados | Verificado | CSS 11.962 B, JS 1.963 B, node --check OK, llaves equilibradas | 8 | Lint formal no ejecutado |
| 6 | Rendimiento y velocidad | Liviano, sin JS pesado | Revisado parcialmente | Tamaños medidos, sin frameworks | 7 | Lighthouse / Core Web Vitals no medidos |
| 7 | SEO técnico y de contenidos | Títulos/metas/canonical/sitemap/schema reales | Verificado | Títulos únicos, metas únicas, schema real, validador OK | 8 | 6 metas 156–159 (Bajo, ver arriba) |
| 8 | Visibilidad para motores de respuesta (AEO/GEO) | Respuestas directas, FAQ, entidades claras | Revisado parcialmente | Respuesta arriba, FAQ + FAQPage, entidades consistentes | 7 | No garantiza aparecer citado en IA |
| 9 | Accesibilidad | WCAG 2.2 AA | Revisado parcialmente | Contraste alto, foco, skip link, alt, aria, reduced-motion | 7 | Auditoría manual con teclado / lector, contraste medido |
| 10 | Seguridad y privacidad | Sin datos, sin secretos, HTTPS | Revisado parcialmente | Sin formularios, sin secretos, Pages HTTPS | 8 | No se declara cumplimiento legal completo |
| 11 | Adaptación responsive | Mobile-first real, no solo contenedores | Revisado parcialmente | Breakpoints 1000/800 px, grids a 1 columna, sticky móvil | 7 | Prueba en dispositivos reales |
| 12 | Copywriting y comunicación | Claro, español AR, sin inventos ni urgencia falsa | Revisado parcialmente | PAS suave, CTA WhatsApp, disclaimers | 7 | Redacción nueva desde cero si el usuario la pide |
| 13 | Optimización de conversiones | Consulta por WhatsApp medible | Revisado parcialmente | CTA hero/final/sticky, beneficios, FAQ, objeciones | 7 | Medición real de clics WhatsApp pendiente |
| 14 | Funcionalidad e integraciones | WhatsApp, teléfono, email, redes reales | Verificado | wa.me/541122845514, tel, mailto y redes presentes | 8 | Ninguno |
| 15 | Escalabilidad y mantenibilidad | Un CSS y un JS, fácil de mantener | Verificado | v6.css + v6.js únicos, sin dependencias | 8 | Documentación de componentes en este archivo |
| 16 | Calidad del contenido y confiabilidad | Hechos verificados, sin inventos | Verificado | Montos, decretos, cargos, organismos, "un crédito por mes" ausente | 9 | Ninguno crítico |
| 17 | Compatibilidad entre navegadores | CSS/JS estándar, sin APIs exóticas | Revisado parcialmente | CSS/JS estándar, sin frameworks | 7 | Prueba en Safari/Firefox/Chrome no hecha |
| 18 | Estabilidad y tolerancia a errores | Sin JS que rompa la página si falla | Revisado parcialmente | JS mínimo, contenido visible sin JS (FAQ <details> donde existe, enlaces reales) | 7 | Prueba con JS desactivado no hecha |
| 19 | Analítica y medición | Objetivos medibles definidos | Pendiente de comprobar | Objetivo = clic WhatsApp, pero sin herramienta de medición instalada | — | Instalar medición solo si el usuario lo pide y con privacidad |
| 20 | Adecuación estratégica al negocio | Vender consultas, no vender un producto | Verificado | Arquetipo híbrido aplicado, sin checkout ni "Buy Now" | 8 | Ninguno |

**Recomendación para producción: NO todavía.**
Motivo: faltan las comprobaciones que el propio Prompt exige antes de recomendar producción — revisión visual renderizada, Lighthouse/Core Web Vitals y prueba en dispositivos reales. El sitio es apto para **prueba en GitHub Pages (vista no indexable)** y, si esa prueba visual es satisfactoria, entonces sí se puede evaluar el pase a producción. No hay defectos críticos ni altos conocidos; los pendientes son de verificación, no de contenido inventado ni de enlaces rotos.

## Despliegue (solo prueba)
Subir el contenido de `credisnet-web-v6/` a la raíz de un repo nuevo, rama `main`, con GitHub Actions para Pages. No subir a producción ni a AAA114851.
