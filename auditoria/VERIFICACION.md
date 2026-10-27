# Verificación de la corrección

Fecha: 27/10/2026.
Origen: AAA114851-main.zip suministrado por el usuario.

## Contenido conservado

`python scripts/verify_content.py` pasó en las 26 páginas:

- Mismos fragmentos textuales y cantidades de apariciones.
- Mismos destinos de enlaces y cantidades de apariciones.
- Mismos metadatos y URL canonical.
- Mismas imágenes y atributos.
- Mismos objetos JSON-LD.

El bloque de familia de la portada se reubicó junto al título principal. Por eso se comparan los textos independientemente del orden. Los scripts inline, el asistente y sus respuestas se conservaron. Se cambió la lógica del carrusel de portada para mostrar un catálogo en escritorio y desplazamiento manual en móvil, sin clones ni avance automático.

## Otras pruebas

`validate_site.py`: 26 HTML, 24 páginas internas, 25 URLs del sitemap y referencias locales válidas.

`node --check` pasó para `main.js`, `rediseno.js` y `credis-assistant.js`.

## No comprobado

La infraestructura de vista previa informó que el servicio no estaba disponible. No se ejecutaron pruebas visuales en navegador, pruebas reales de WhatsApp ni Lighthouse. No se atribuyen puntuaciones ni mejoras de conversión.

Esta entrega es una modificación de diseño con conservación de contenido aprobado, no una nueva auditoría ni reescritura de las afirmaciones comerciales o jurídicas del original.
