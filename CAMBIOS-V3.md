# Credisnet v3 — versión 10/10 de prueba — SOLO PARA PRUEBA, NO PRODUCCIÓN

Subir solo a un repo de PRUEBA nuevo y publicar solo con GitHub Pages.
El workflow `.github/workflows/pages.yml` que ya trae el proyecto prepara
una vista NO indexable (noindex, robots Disallow), así que no afecta al SEO
de credisnet.com.ar. Cuando esté aprobado, recién ahí se evalúa pasar a
producción. NO subir este zip al repo de producción sin aprobación.

## Diseño elegido y por qué

Tema claro, no oscuro. La versión anterior era oscura con tarjetas de vidrio;
esta es papel cálido (#FFFDF7), azul marino profundo (#0B2340) y verde
bosque (#0B7A5E, contraste alto sobre blanco). Se eligió así porque gran
parte del público son retirados y jubilados: el texto oscuro sobre fondo
claro se lee mejor, con menos cansancio, que el texto blanco sobre fondo
oscuro, y el verde bosque mantiene la identidad Credisnet sin perder
contraste.

- Tipografía: Inter para texto y Montserrat para títulos (las mismas
  familias del sitio, para no romper nada), pero con base más grande
  (18 px, 17 px en móvil) y renglones más altos (1.75).
- Mucho aire: secciones con más respiro, tarjetas blancas con borde
  visible y sombra suave, en vez de vidrio oscuro.
- CTA: botones de WhatsApp en verde WhatsApp (#25D366) con texto oscuro,
  grandes (16–28 px de relleno, 1.12 rem de letra). No se volvió a poner
  botón en el encabezado, para no apretar el menú como pasó en v2: el CTA
  grande está en el hero, hay CTA al final de cada página y el botón
  flotante de WhatsApp es más grande (68 px).
- Cabecera: blanca, con borde marino, sticky, sin tapar contenido, y menú
  en azul marino legible.
- Carrusel de la home: tarjetas blancas de 300 px (280 px en móvil),
  con margen lateral, para que no queden cortadas en los bordes como antes.
- Footer: se mantiene oscuro marino, para cerrar con contraste y que los
  enlaces se lean.

El nuevo diseño vive en `docs/css/v3-theme.css`, cargado después de
`style.css` y `pages.css` en las 26 páginas HTML. No se tocaron los CSS
originales, así que el cambio es reversible quitando ese archivo y su
`<link>`.

## Qué cambió

- Home: fondo claro, titular marino con acento verde bosque, resumen y
  botón grande de WhatsApp arriba, carrusel blanco sin tarjetas cortadas.
- Páginas internas: mismo contenido, nueva presentación clara, tablas
  con encabezado marino, preguntas frecuentes en tarjetas blancas,
  secciones alternadas claras.
- Caja de Retiros: se mantiene la tira de 11 organismos, ahora en
  tarjetas blancas, con monto $20.000.000, hasta 36 cuotas según evaluación.
- Docentes: se mantiene el módulo propio "Cargos que tomamos" entre el
  hero y "Líneas de Préstamo Disponibles", con 6 tarjetas: DOCENTE
  TITULAR, DOCENTE TITULAR INTERINO, DOCENTE PROVISIONAL, DOCENTE
  SUPLENTE, AUXILIAR TITULAR y AUXILIAR MENSUALIZADO.
- Títulos, metas, canonical, sitemap (25 URLs), robots y JSON-LD: sin
  cambios respecto a v2, que ya traía los títulos y metas finales.

## Qué NO cambió

- Contenido verificado, montos, plazos, decretos (352/2026 nacional,
  988/2021 provincia) y condiciones: no se inventó ningún monto, tasa,
  plazo ni condición nueva.
- Caja: nunca "un crédito por mes".
- Páginas legales (Privacidad, Términos, Información Financiera): solo
  nuevo diseño, sin reescribir el fondo legal.
- Contacto real, sin formularios que envíen datos: WhatsApp
  https://wa.me/541122845514, teléfono 11 6970-7265, email
  info@credisnet.com.
- URLs exactas de `docs/sitemap.xml`.

## Validación

`python scripts/validate_site.py` en esta copia debe dar OK (26 HTML,
25 URLs indexables). Si da un error nuevo, no subir a prueba hasta
revisarlo.
