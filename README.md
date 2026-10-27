# Credisnet Web — versión final

Sitio estático de Credisnet preparado para publicarse en **Cloudflare Pages** desde GitHub.

## Estado

- Portada final en `docs/index.html`.
- 24 páginas internas finales con URLs limpias.
- Header, menú móvil, footer e identidad visual unificados.
- CSS centralizado en `docs/css/style.css` y `docs/css/pages.css`.
- Interlinking, migas de pan, canonical, metadatos sociales y datos estructurados.
- Sitemap con 25 URLs indexables.
- Página 404 con `noindex`.
- Redirecciones históricas en `docs/_redirects`.
- Dominio canónico: `https://www.credisnet.com.ar`.

## Archivos de control

- `URLS-DEFINITIVAS.md`: inventario de rutas finales.
- `PAGINAS-PENDIENTES.md`: confirma que no quedan páginas pendientes.
- `content-pages.json`: inventario estructurado de las 24 páginas internas.
- `scripts/validate_site.py`: valida páginas finales, enlaces, canonical, robots y sitemap.

## Cloudflare Pages

- Rama de producción: `main`
- Framework preset: `None`
- Build command: vacío
- Build output directory: `docs`

## GitHub Pages de prueba

El workflow crea una copia temporal no indexable en `_site`. En `Settings → Pages`, usar **GitHub Actions** si se desea mantener esa vista de prueba.

## Validación local

```bash
python scripts/validate_site.py
python -m http.server 8000 --directory docs
```

## URLs en Cloudflare Pages

Las páginas internas usan barra final (`/ruta/`), que coincide con la forma canónica en que Cloudflare Pages sirve carpetas con `index.html`. No deben agregarse redirecciones de `/ruta/` hacia `/ruta`, porque producirían un bucle.
