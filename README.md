# Credisnet Web — v6 (sitio nuevo, solo para prueba)

Sitio estático de Credisnet, construido con el Prompt Maestro V2.0, para probar en GitHub Pages.
NO es producción y NO sobrescribe el repo candidato AAA114851.

## Estado
- 25 páginas indexables (home + 24 internas finales) en `docs/`, URLs limpias con barra final.
- Sistema visual propio nuevo en `docs/css/v6.css` (el CSS viejo — style.css, pages.css, credis-assistant.css — fue eliminado, no tapado).
- JS mínimo en `docs/js/v6.js`: menú móvil, FAQ acordeón, flechas de tiras. Sin frameworks.
- Header, menú móvil, footer e identidad visual unificados. Solo el logo original en `docs/img/logo.png`.
- Canonical, sitemap con 25 URLs, robots, metadatos sociales y JSON-LD reales (Organization, WebSite, Service, FAQPage, BreadcrumbList).
- Página 404 con `noindex`.
- Enlaces internos relativos, para que funcione en GitHub Pages de proyecto (`usuario.github.io/repo/`) y en dominio propio.

## GitHub Pages de prueba
El workflow en `.github/workflows/pages.yml` valida, prepara una vista no indexable en `_site` con `scripts/prepare_github_pages.py` y publica con GitHub Actions. En `Settings → Pages`, usar **GitHub Actions**.

## Validación local
```bash
python scripts/validate_site.py
python -m http.server 8000 --directory docs
```

## Contacto (real, sin formularios que envíen datos)
- WhatsApp: https://wa.me/541122845514
- Teléfono: 11 6970-7265
- Email: info@credisnet.com

Ver `CAMBIOS-V6.md` para arquetipo, estrategia, diseño, pruebas, defectos y matriz de evaluación. No se declara 10/10 global sin evidencia.
