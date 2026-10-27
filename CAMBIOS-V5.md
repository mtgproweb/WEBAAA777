# Credisnet v5 — Premium, nivel Apple/Stripe, con las 25 páginas completas

SOLO PARA PRUEBA. No subir a producción ni al repo principal sin aprobación.

## Por qué no es amateur ni otro rediseño plano
- El CSS viejo oscuro/glass (style.css, pages.css, credis-assistant.css) fue ELIMINADO
  del sitio, no tapado con un theme encima. Todo el diseño vive en un único sistema
  nuevo: docs/css/premium.css.
- Sistema de diseño con tokens consistentes: azul marino #0F2A44, verde Credisnet
  #0EA47A / #0B7A5E, ámbar #FFC53D solo para montos y foco, fondo blanco y
  #F6F8FB, tinta #12233A, línea #E2E8F0, radios 16/20 px, sombras suaves en dos
  niveles, nunca sombras duras ni brillos de vidrio.
- Tipografía refinada: Montserrat 800 para títulos con tracking -0.02em e
  Inter para texto, 17.5 px, interlineado 1.65, jerarquía H1 clamp 2.1-3.6rem,
  H2 clamp 1.55-2.25rem. Nada de tamaños al azar.
- Ritmo profesional: secciones a 56 px, tarjetas a 16 px de gap, grids alineados
  a 3 columnas en escritorio y 1 en móvil, micro-interacciones de 200 ms
  (hover sube 3 px, foco ámbar visible, sin rebotes).
- Hero premium en home y en cada página interna: titular fuerte, subtítulo corto,
  CTA grande de WhatsApp, señales de confianza reales junto al CTA
  ("Asesoramiento gratuito · Sin costos ocultos · Sujeto a aprobación crediticia")
  y tarjeta de monto orientativo en azul marino con el monto en ámbar.
- Header premium: blanco, sticky, con blur suave, que no tapa contenido y no
  aprieta el menú. En móvil: hamburguesa + barra fija de WhatsApp abajo
  ("¡Consulta tu disponible ahora!"), que reemplaza al flotante en móvil para
  no duplicar. Sin botón de encabezado que apriete el menú (decisión ya tomada en v2).
- Componentes tipo Stripe: grid de líneas con monto, tarjetas de beneficios,
  pasos numerados, tabla de condiciones con encabezado marino, FAQ en tarjetas
  blancas accesibles, cierre con CTA grande en degradado marino. Nada de
  carrusel infinito que corte tarjetas: el carrusel de la home ahora es una
  tira con snap, tarjetas blancas de 308 px, con padding lateral para que no
  queden cortadas en los bordes.
- Solo el logo original (docs/img/logo.png), sin fotos con uniformes ni
  insignias oficiales. Se mantienen las imágenes existentes del sitio
  (familia.webp, fuerzas.webp, prestamos-credisnet.webp) solo donde ya estaban.

## Las 25 páginas (mismas URLs, títulos y metas finales de v2)
index, prestamos-empleados-publicos, prestamos-para-docentes-y-auxiliares,
prestamos-policia-provincia-buenos-aires, prestamos-jubilados-pensionados-ips,
prestamos-servicio-penitenciario-bonaerense, prestamos-personal-salud,
prestamos-fuerzas-armadas, prestamos-ejercito-argentino, prestamos-armada-argentina,
prestamos-fuerza-aerea-argentina, prestamos-fuerzas-de-seguridad,
prestamos-policia-federal, prestamos-gendarmeria-nacional,
prestamos-prefectura-naval-argentina, prestamos-policia-seguridad-aeroportuaria,
prestamos-servicio-penitenciario-federal, prestamos-caja-retiros-policia-federal,
prestamos-policia-de-la-ciudad, prestamos-personal-retirado-fuerzas,
quienes-somos, preguntas-frecuentes, informacion-financiera,
politica-de-privacidad, terminos-y-condiciones.

## Contenido mantenido, sin inventar
- Montos orientativos hasta 36 cuotas, sujeto a aprobación: $20.000.000
  Ejército, Armada, Fuerza Aérea, PFA, Fuerzas Armadas, Fuerzas de Seguridad,
  Gendarmería, Prefectura, PSA, SPF, Retirados, Caja; $10.000.000 Docentes,
  SP Bonaerense, IPS, Policía Ciudad; $6.000.000 Policía Provincia, Salud.
- Decretos 352/2026 nacional, 988/2021 provincia.
- Docentes: módulo "Cargos que tomamos" entre hero y Líneas, con DOCENTE
  TITULAR, DOCENTE TITULAR INTERINO, DOCENTE PROVISIONAL, DOCENTE SUPLENTE,
  AUXILIAR TITULAR, AUXILIAR MENSUALIZADO, en tarjetas del mismo estilo.
- Caja: 11 organismos (PFA, PNA, Gendarmería, PSA civil y seguridad, SPF,
  Personal Civil de Inteligencia FFAA, Personal Militar FFAA, Policía de
  Establecimientos Navales según anexos, AFI, SIDE, SINEP), $20.000.000.
  NUNCA "un crédito por mes" (verificado ausente).
- Contacto: WhatsApp https://wa.me/541122845514, 11 6970-7265,
  info@credisnet.com. Sin formularios que envíen datos.
- Legales: fondo legal serio sin reescribir de fondo, solo nuevo diseño.
- SEO/CRO Sales: respuesta directa arriba, FAQ con schema, schema
  Service/FAQPage/Organization heredados de v2, CTA "¡Consulta tu disponible
  ahora!" por WhatsApp, sin "Buy Now" ni garantías inventadas.
- Enlaces RELATIVOS en todo el sitio, para GitHub Pages de proyecto
  (usuario.github.io/repo/) y dominio propio. Sitemap con las 25 URLs de
  producción, robots, workflow Pages no indexable.

## Validación
- scripts/validate_site.py: OK, 26 HTML, 24 páginas internas finales,
  25 URLs indexables y referencias locales válidas.
- Títulos únicos (0 duplicados), metas finales de v2 sin cambios.
- premium.css: llaves equilibradas.
- Caveat: validación de estructura y contenido, no revisión visual renderizada
  en navegador; abrir la prueba en Pages y confirmar visualmente home,
  Docentes y Caja antes de cualquier paso a producción.
