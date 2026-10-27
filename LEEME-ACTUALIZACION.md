# Credisnet · actualización solicitada

Fecha: 27 de octubre de 2026.
Base: `AAA114851-main(1).zip` proporcionado en esta conversación.

## Cambios

- Tarjetas de préstamos estáticas: 4 columnas en escritorio amplio (desde 1051 px), 2 en pantallas intermedias (768–1050 px).
- Carrusel móvil hasta 767 px: desplazamiento táctil y botones anterior/siguiente. Sin clonación de tarjetas ni avance automático.
- Selector “Una opción para tu sector”: las 19 líneas existentes, con botón “Ver mi línea”.
- Buscador de organismos en la sección de líneas: admite búsquedas sin tildes, varias palabras, estado sin resultados y restauración al borrar.
- Se completaron las 19 opciones de la sección de organismos con enlaces a Fuerzas Armadas, Fuerzas de Seguridad y Caja de Retiros, ya presentes como páginas del sitio.
- Portada más compacta, logo más grande, tarjetas con montos alineados, textos secundarios de mayor tamaño y controles de testimonios más grandes.
- Testimonios con navegación manual para que no se desplacen mientras se leen; corregido el acceso a la última posición.
- Ajustes de foco y menú móvil.

## Conservado

Los archivos `style.css`, `pages.css` y `credis-assistant.css` se conservan byte por byte. La nueva capa `mejoras.css` utiliza exclusivamente las variables de color originales. No se incorporaron fondos blancos, crema ni colores de las capturas.

Se conservan textos aprobados, montos, cuotas, requisitos, testimonios, contactos, metadatos, datos estructurados y URLs. También imágenes y asistente Credis. Sólo se añadió el texto necesario para los nuevos controles solicitados.

## Verlo localmente

Con Python 3, desde la carpeta del repositorio:

```sh
python -m http.server 8000 --directory docs
```

Abrí http://localhost:8000. No requiere instalación de dependencias.

## Subirlo manualmente a GitHub

1. Descomprimí el ZIP.
2. Subí el contenido de `credisnet-actualizado/` a la raíz del repositorio; no subas sólo el ZIP ni otra carpeta envolviendo el proyecto.
3. Incluí `.github/workflows/pages.yml`, `docs/`, `scripts/`, `auditoria/` y los demás archivos.
4. Conservá GitHub Pages configurado con **GitHub Actions**.
5. Esperá que termine “Validar y publicar en GitHub Pages”.

El workflow mantiene la configuración de vista de prueba no indexable del repositorio original. No cambiamos la publicación activa durante esta entrega. Conservá un respaldo antes de reemplazar archivos.

## Archivos nuevos principales

- `docs/css/mejoras.css`: presentación y breakpoints. Se carga después de los estilos originales.
- `docs/js/mejoras.js`: selector, buscador, carrusel y ajustes de navegación.
- `scripts/verify_preservation.py`: verifica conservación del original.
- `scripts/test_features.cjs`: pruebas de lógica con DOM simulado.
- `auditoria/original.json`: referencia de contenido y firmas de archivos originales.

## Verificaciones ejecutadas

```sh
python scripts/validate_site.py
python scripts/verify_preservation.py
node --check docs/js/main.js
node --check docs/js/mejoras.js
node scripts/test_features.cjs
```

Resultados: 26 HTML, 24 páginas internas y 25 URLs de sitemap con referencias válidas; contenido original conservado; CSS y recursos originales intactos; pruebas de lógica aprobadas para búsqueda, selector, carrusel móvil, límites, modo escritorio, movimiento reducido y cierre con Escape.

La infraestructura de vista previa local no estuvo disponible. No se ejecutaron revisión visual en navegador de esta versión, Lighthouse ni pruebas en dispositivos reales. Las pruebas JavaScript usan un DOM simulado. Revisar la URL de prueba en computadora y celular antes del reemplazo definitivo.
