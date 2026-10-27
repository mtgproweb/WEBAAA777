#!/usr/bin/env python3
"""Valida el sitio final de Credisnet antes de publicarlo."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "docs"
MANIFEST = REPO / "content-pages.json"
SITEMAP = ROOT / "sitemap.xml"
EXPECTED_INTERNAL_PAGES = 24
FINAL_DOMAIN = "https://www.credisnet.com.ar"
URL_ATTRS = {"href", "src", "action", "poster", "data-src"}


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if not value:
                continue
            if name in URL_ATTRS:
                self.references.append(value)
            elif name == "srcset":
                for item in value.split(","):
                    candidate = item.strip().split()[0] if item.strip() else ""
                    if candidate:
                        self.references.append(candidate)

    handle_startendtag = handle_starttag


def validate_reference(file: Path, value: str, errors: list[str]) -> None:
    if value.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return

    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc:
        return

    # El sitio también se publica como vista de prueba en un subdirectorio de
    # GitHub Pages; por eso los recursos internos deben ser relativos.
    if value.startswith("/"):
        errors.append(
            f"{file.relative_to(ROOT)}: referencia absoluta incompatible con "
            f"la vista de GitHub Pages: {value}"
        )
        return

    target_path = unquote(parsed.path)
    if not target_path:
        return

    target = (file.parent / target_path).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        errors.append(f"{file.relative_to(ROOT)}: referencia fuera de docs/: {value}")
        return

    candidates = [target]
    if target_path.endswith("/") or target.is_dir():
        candidates.append(target / "index.html")
    if not any(candidate.exists() for candidate in candidates):
        errors.append(f"{file.relative_to(ROOT)}: no existe {value}")


def robots_content(text: str) -> str:
    match = re.search(
        r'<meta\b[^>]*\bname=["\']robots["\'][^>]*\bcontent=["\']([^"\']+)["\']',
        text,
        flags=re.IGNORECASE,
    )
    if not match:
        # Admite el orden inverso de atributos.
        match = re.search(
            r'<meta\b[^>]*\bcontent=["\']([^"\']+)["\'][^>]*\bname=["\']robots["\']',
            text,
            flags=re.IGNORECASE,
        )
    return match.group(1).lower().replace(" ", "") if match else ""


def canonical_href(text: str) -> str:
    patterns = (
        r'<link\b[^>]*\brel=["\']canonical["\'][^>]*\bhref=["\']([^"\']+)["\']',
        r'<link\b[^>]*\bhref=["\']([^"\']+)["\'][^>]*\brel=["\']canonical["\']',
    )
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(1)
    return ""


def read_sitemap(errors: list[str]) -> set[str]:
    if not SITEMAP.is_file():
        errors.append("Falta docs/sitemap.xml")
        return set()
    try:
        root = ET.parse(SITEMAP).getroot()
    except Exception as exc:
        errors.append(f"No se pudo leer sitemap.xml: {exc}")
        return set()
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return {
        loc.text.strip()
        for loc in root.findall("sm:url/sm:loc", namespace)
        if loc.text and loc.text.strip()
    }


def main() -> int:
    errors: list[str] = []
    html_files = sorted(ROOT.rglob("*.html"))

    if not (ROOT / "index.html").is_file():
        errors.append("Falta docs/index.html")

    for file in html_files:
        text = file.read_text(encoding="utf-8")
        parser = ReferenceParser()
        parser.feed(text)
        for reference in parser.references:
            validate_reference(file, reference, errors)

    try:
        pages = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        pages = []
        errors.append(f"No se pudo leer content-pages.json: {exc}")

    if not isinstance(pages, list):
        errors.append("content-pages.json debe contener una lista")
        pages = []

    if len(pages) != EXPECTED_INTERNAL_PAGES:
        errors.append(
            f"content-pages.json debe contener {EXPECTED_INTERNAL_PAGES} páginas; "
            f"contiene {len(pages)}"
        )

    sitemap_urls = read_sitemap(errors)
    expected_sitemap_urls = {f"{FINAL_DOMAIN}/"}
    seen: set[str] = set()

    for page in pages:
        if not isinstance(page, dict):
            errors.append(f"Entrada inválida en content-pages.json: {page!r}")
            continue

        slug = str(page.get("slug", ""))
        status = str(page.get("status", "final")).lower()
        relative_file = str(page.get("file", ""))

        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            errors.append(f"Slug inválido: {slug!r}")
        if slug in seen:
            errors.append(f"Slug duplicado: {slug}")
        seen.add(slug)

        file = REPO / relative_file
        if not file.is_file():
            errors.append(f"Falta página declarada: {relative_file}")
            continue

        text = file.read_text(encoding="utf-8")
        robots = robots_content(text)
        expected_url = f"{FINAL_DOMAIN}/{slug}/"
        canonical = canonical_href(text)

        if status == "final":
            if not robots:
                errors.append(f"La página final no tiene meta robots: {relative_file}")
            elif "noindex" in robots:
                errors.append(f"La página final conserva noindex: {relative_file}")
            elif "index" not in robots or "follow" not in robots:
                errors.append(f"Meta robots incompleta en página final: {relative_file}")
            expected_sitemap_urls.add(expected_url)
        elif status == "pending":
            if "noindex" not in robots:
                errors.append(f"La página pendiente no tiene noindex: {relative_file}")
        else:
            errors.append(f"Estado desconocido {status!r} en {relative_file}")

        if canonical != expected_url:
            errors.append(
                f"Canonical incorrecta en {relative_file}: "
                f"se esperaba {expected_url!r} y se encontró {canonical!r}"
            )
        if expected_url not in text:
            errors.append(f"Falta la URL final en metadatos de {relative_file}")

    missing_sitemap = sorted(expected_sitemap_urls - sitemap_urls)
    extra_sitemap = sorted(sitemap_urls - expected_sitemap_urls)
    for url in missing_sitemap:
        errors.append(f"Falta URL final en sitemap.xml: {url}")
    for url in extra_sitemap:
        errors.append(f"URL no declarada o no indexable en sitemap.xml: {url}")

    index_text = (ROOT / "index.html").read_text(encoding="utf-8")
    if re.search(r'href=["\'][^"\']*(?:/p/|\.html(?:[?#]|["\']))', index_text):
        errors.append("La portada contiene enlaces públicos con /p/ o .html")

    homepage_canonical = canonical_href(index_text)
    if homepage_canonical != f"{FINAL_DOMAIN}/":
        errors.append(
            "Canonical incorrecta en docs/index.html: "
            f"se encontró {homepage_canonical!r}"
        )
    if "noindex" in robots_content(index_text):
        errors.append("La portada conserva noindex")

    not_found = ROOT / "404.html"
    if not_found.is_file() and "noindex" not in robots_content(
        not_found.read_text(encoding="utf-8")
    ):
        errors.append("docs/404.html debe conservar noindex")

    if errors:
        print("Errores encontrados:")
        for error in errors:
            print(f"- {error}")
        return 1

    final_count = sum(
        1 for page in pages if isinstance(page, dict) and page.get("status", "final") == "final"
    )
    print(
        f"OK: {len(html_files)} HTML, {final_count} páginas internas finales, "
        f"{len(sitemap_urls)} URLs indexables y referencias locales válidas."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
