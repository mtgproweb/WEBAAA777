# Credisnet — Nuevo sitio web V2.0

Rediseño independiente creado desde cero para el nicho de préstamos con descuento de haberes del sector público argentino. Es una **entrega nueva**, no un commit ni una modificación directa sobre `mtgproweb/AAA114851`.

## Qué incluye

- 25 URLs indexables y una página 404 (`noindex`), con arquitectura de carpetas y barras finales.
- Portada completamente nueva, selector funcional de sector, 18 páginas especializadas de línea de crédito, preguntas frecuentes, guía explicativa, quiénes somos, contacto y textos legales de revisión.
- Responsive real, navegación móvil accesible, preguntas desplegables sin dependencias, diseño editorial original en verdes naturales y lima.
- SEO básico preparado: títulos y descripciones por página, canonical, Open Graph, imagen para compartir, `robots.txt`, `sitemap.xml`, datos estructurados WebSite, Organization y Service únicamente en páginas correspondientes.
- Medidas de seguridad estáticas en `docs/_headers`, sin rastreadores ni formularios de captura de datos personales.
- Generador con fuente centralizada de contenido, scripts de validación y pruebas visuales aisladas.

## Estructura

```text
credisnet-nueva-v2/
├─ config/site.json          # Marca, dominio y único número comercial
├─ scripts/build.py          # Genera las 25 páginas HTML
├─ scripts/check.py          # Integridad de enlaces, SEO, JSON-LD, sitemap
├─ scripts/browser_check.py  # Pruebas UI con Chromium, render aislado
├─ docs/                    # Directorio listo para Cloudflare Pages
│  ├─ index.html
│  ├─ css/site.css
│  ├─ js/site.js
│  ├─ assets/favicon.svg
│  ├─ assets/og-card.png
│  ├─ <ruta>/index.html
│  ├─ robots.txt
│  ├─ sitemap.xml
│  ├─ _headers
│  ├─ _redirects
│  └─ 404.html
└─ QA-REPORT.md
```

## Revisar antes de publicar

1. **WhatsApp:** el sitio público de referencia mostraba dos teléfonos distintos. El CTA principal usaba `541122845514` y la cabecera `541169707265`. Este rediseño centraliza `541122845514` en `config/site.json` **provisionalmente**. Confirmá el número comercial real y regenerá el sitio antes de publicar. No se modificó ningún número de la web activa.
2. **Páginas legales:** las páginas de términos y privacidad son bases de trabajo y requieren revisión por responsable legal, identificación formal del responsable de datos, canales de contacto y revisión de normativa aplicable.
3. **Créditos:** validar para cada organismo los convenios, normas citadas, disponibilidad, entidades otorgantes, requisitos y términos financieros. Por seguridad, esta versión no presume montos, tasas, plazos ni tiempos de aprobación garantizados.
4. **Redirecciones históricas:** el README público del repositorio original señala `docs/_redirects`. No se pudo obtener el archivo completo. Copiar y comparar las redirecciones originales **antes de sustituir** el sitio, para preservar SEO.
5. **Contenido y marca:** validar copy, marca, uso de símbolos e identidad institucional, la cobertura geográfica y la inclusión de cada línea.
6. **Pruebas de despliegue:** realizar en una URL de staging verificando cabeceras, HTTP 404, enlaces, OG, Search Console, Lighthouse y pruebas reales con teclado y lector de pantalla. Evitar indexar el staging.

## Editar contacto o dominio

Modificar `config/site.json`:

```json
{
  "brand": "Credisnet",
  "canonical_domain": "https://www.credisnet.com.ar",
  "whatsapp": "541122845514"
}
```

El teléfono debe tener solo dígitos, con código de país, sin signo `+` ni espacios. El archivo incluye una nota de revisión adicional. Luego ejecutar:

```bash
python scripts/build.py
python scripts/check.py
```

Los cambios de textos por sector se realizan en la lista `LINES` de `scripts/build.py`. Los estilos están en `docs/css/site.css`.

## Publicar en Cloudflare Pages

Esta entrega sigue la arquitectura estática del README público del repositorio de referencia. **No necesita npm ni compilación para desplegar `docs`**.

1. Crear un **repositorio nuevo** en GitHub (recomendado), importar este proyecto y confirmar el contenido completo de `docs/`.
2. En Cloudflare Pages: crear un proyecto conectado al nuevo repositorio; rama `main`; Framework preset `None`; Build command vacío; Build output directory `docs`.
3. Publicar primero en staging, sin conectar todavía el dominio definitivo. Revisar los puntos pendientes.
4. Cuando la versión esté aprobada, conservar las URLs actuales, agregar redirecciones históricas y recién entonces migrar el dominio.

También puede probarse localmente desde la raíz del proyecto:

```bash
python -m http.server 8000 --directory docs
```

Abrir `http://localhost:8000/`. Algunas rutas `/carpeta/` funcionan de forma nativa mediante `index.html`.

## Verificaciones incluidas

```bash
python scripts/check.py
node --check docs/js/site.js
python scripts/browser_check.py
```

`browser_check.py` usa Playwright y Chromium del entorno de prueba, carga el HTML con estilos y script embebidos porque el navegador del entorno bloquea conexiones HTTP locales por política. No prueba navegación real a rutas del servidor ni resultados en Cloudflare. Para pruebas locales de routing, usar servidor y navegador sin esa restricción.

## Procedencia y límites

Se verificó públicamente el README de `https://github.com/mtgproweb/AAA114851` y contenido accesible de `https://www.credisnet.com.ar`. No se pudo clonar ni inspeccionar la totalidad de los archivos fuente originales; esta reconstrucción no debe presentarse como una migración 1:1 o un refactor verificado contra cada archivo. Las rutas del catálogo se preservaron a partir de las rutas públicas verificadas; las rutas nuevas de información se incluyeron como contenido adicional.

**No se efectuó despliegue, publicación, commit o push a GitHub.**
