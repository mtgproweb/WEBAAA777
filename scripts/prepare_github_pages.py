#!/usr/bin/env python3
"""Prepara una vista de prueba no indexable para GitHub Pages."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs"
DESTINATION = ROOT / "_site"
NOINDEX_META = '<meta name="robots" content="noindex,nofollow,noarchive">'


def main() -> None:
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)
    shutil.copytree(SOURCE, DESTINATION)

    for html_file in DESTINATION.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8")
        lower = text.lower()
        head_pos = lower.find("<head>")
        if head_pos >= 0:
            insert_at = head_pos + len("<head>")
            text = text[:insert_at] + "\n" + NOINDEX_META + text[insert_at:]
            html_file.write_text(text, encoding="utf-8")

    (DESTINATION / "robots.txt").write_text(
        "User-agent: *\nDisallow: /\n", encoding="utf-8"
    )
    print(f"Vista GitHub Pages preparada en {DESTINATION}")


if __name__ == "__main__":
    main()
