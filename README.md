# Credisnet — nuevo sitio

Rediseño completo en HTML, CSS y JavaScript. Incluye portada, 24 páginas internas y página 404. Se mantiene la estructura `docs/`, las URLs públicas y los dos canales de WhatsApp del repositorio original.

## Ver en tu computadora

Requiere Python 3. Desde la carpeta del repositorio:

```sh
python -m http.server 8000 --directory docs
```

Abrí http://localhost:8000. Detené el servidor con Ctrl+C. No requiere npm, instalación de paquetes ni claves.

## Subir a un repositorio NUEVO de GitHub

1. Descomprimí el ZIP.
2. Creá un repositorio nuevo (por ejemplo `credisnet-nuevo`).
3. Subí el **contenido** de la carpeta `credisnet-nuevo`, con `docs`, `scripts`, `data`, `content-pages.json` y los demás archivos en la raíz. No subas el ZIP ni una carpeta adicional envolviendo el proyecto.
4. Incluí la carpeta oculta `.github/workflows/pages.yml`. En Settings → Pages seleccioná **GitHub Actions**.
5. Ejecutá “Validar y publicar en GitHub Pages” desde Actions si no comenzó al subir a `main`.
6. Abrí la URL indicada por el despliegue. La copia publicada mediante este flujo lleva `noindex` para evitar duplicar el sitio actual. Esto no es un control de acceso: cualquiera con la URL puede verla.

Para subir sólo con el navegador y sin workflow: ejecutá `python scripts/prepare_github_pages.py`, copiá el contenido generado de `_site/` en `docs/` de una copia separada y publicá desde main /docs. No alteres los fuentes originales con esa copia de prueba.

## Reemplazar el sitio actual, después de revisarlo

Conservá un respaldo. `docs/` es la versión indexable para el dominio `https://www.credisnet.com.ar/`; el workflow genera una copia de prueba no indexable en `_site/`. No uses `_site/` en producción. No se cambió ningún repositorio remoto, dominio ni sitio activo durante esta entrega.

Antes de reemplazar: confirmar canales de contacto, condiciones comerciales y textos legales; revisar escritorio y móvil y completar las pruebas de accesibilidad, Lighthouse y flujos reales. Ver `AUDITORIA.md`.

## Editar y regenerar

- `scripts/build_site.py`: componentes, portada y páginas de líneas de crédito.
- `content-pages.json`: nombres y rutas de las 24 páginas internas.
- `data/*.html`: textos de privacidad, términos e información financiera.
- `docs/css/site.css`: diseño responsive y estados de foco.
- `docs/js/site.js`: menú, búsqueda y selector de sector.
- `docs/img/`: imágenes del proyecto original.

```sh
python scripts/build_site.py
python scripts/validate_site.py
python scripts/prepare_github_pages.py
python scripts/check_quality.py
node --check docs/js/site.js
node scripts/test_interactions.cjs
```

Node sólo es necesario para comprobar JavaScript; no para servir el sitio. Los cambios manuales en HTML generado se sobrescriben al regenerar.

## Alcance funcional

Buscador local de 19 líneas, selector de organismo, preguntas desplegables y consulta contextual por WhatsApp. No se recopilan datos en el sitio, no hay cookies ni analítica. No hay simulador de cuotas ni aprobación automática: no se proporcionaron tasas verificadas ni una API de entidad financiera.

Los WhatsApp se conservan por función: consultas `+54 11 2284-5514`; contacto general `+54 11 6970-7265`. Email: `info@credisnet.com`.

Las imágenes proceden del ZIP proporcionado; el titular debe confirmar sus derechos de uso. Los contenidos de cada línea se han simplificado para no presentar montos, plazos, tasas o disponibilidad como garantizados. Los términos originales se conservaron como base; requieren revisión jurídica antes del reemplazo.
