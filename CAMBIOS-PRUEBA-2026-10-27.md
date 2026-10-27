# Versión de prueba — NO es producción

Subir este repo completo a un repo de PRUEBA en GitHub y publicar solo con GitHub Pages.
El workflow de GitHub Pages que ya trae el repo prepara una vista NO indexable (noindex, robots Disallow),
así que no afecta al SEO de credisnet.com.ar. Cuando esté aprobado, recién ahí se pasa a Cloudflare / producción.
NO subir este zip al repo de producción sin aprobación.

## Cambios incluidos
- Títulos y meta descripciones finales de las 25 páginas (guardadas el 2026-10-27), con principales en mayúscula y CTA "¡Consulta tu disponible ahora!" en todas las metas.
- Página principal: nombre del sitio "Credisnet | Préstamos", título "Credisnet | Préstamos por Descuento de Haberes".
- Página principal: botón "¡Consulta tu disponible ahora!" en el encabezado (desktop) y en el hero, con resumen directo arriba del carrusel. Botón flotante y resto de la página sin cambios.
- Botón "¡Consulta tu disponible ahora!" en el encabezado: ELIMINADO el 2026-10-27 por decisión del usuario, porque apretaba el menú en la principal. Queda solo el botón grande del hero.
- Página principal: schema FAQPage con las 10 preguntas visibles en la página.
- Página Caja de Retiros Policía Federal: lista de retirados nacionales que pueden consultar (PFA, PNA, Gendarmería, PSA, SPF, Personal Civil de Inteligencia FFAA, Personal Militar FFAA, Policía de Establecimientos Navales según anexos, AFI, SIDE, SINEP) y monto máximo orientativo $20.000.000, como ya estaba en la página.- Página Caja de Retiros Policía Federal: slide deslizable con 11 tarjetas de organismos (PFA, PNA, Gendarmería, PSA, SPF, Civil de Inteligencia FFAA, Militar FFAA, Policía de Establecimientos Navales, AFI, SIDE, SINEP), con flechas y texto corto para entenderlo rápido.
- NO se incluyó "un crédito por mes" (confirmado como no válido).
- Páginas legales (Privacidad, Términos, Información Financiera): solo título y meta, sin cambiar el fondo legal.
- No se agregaron fotos al carrusel; se mantiene el diseño actual con montos en verde.
- Validación: python scripts/validate_site.py = OK (26 HTML, 25 URLs indexables).

## Pendiente de confirmar antes de producción
- Monto de Caja: en este zip se mantiene $20.000.000, que ya estaba en la página y que el usuario mencionó como 20M. Si el máximo correcto fuera $2.000.000, avisar antes de pasar a producción.
