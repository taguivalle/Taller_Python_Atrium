#!/usr/bin/env python3
# ============================================
# ARCHIVO: src/diagnostico_css.py
# AUTOR: Gustavo Vallejo
# FECHA: 06 de Abril de 2026
# ============================================

from pathlib import Path

CSS_FILE = Path("../static/css/estilo.css")


def check_dropdown_css():
    """Verifica si el CSS del dropdown está correcto"""
    print("=" * 60)
    print("🔍 DIAGNÓSTICO CSS DEL DROPDOWN")
    print("=" * 60)

    if not CSS_FILE.exists():
        print(f"❌ Archivo no encontrado: {CSS_FILE}")
        return

    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = [
        ('.dropdown-content', "Clase .dropdown-content"),
        ('z-index: 100000', "z-index alto"),
        ('display: none', "display: none inicial"),
        ('display: block', "display: block en hover"),
        ('overflow-y: auto', "Scroll vertical"),
        ('max-height: 400px', "Altura máxima"),
        ('position: absolute', "Posición absoluta"),
    ]

    print("\n📋 VERIFICACIÓN DE CSS:")
    print("-" * 60)

    for pattern, name in checks:
        status = "✅" if pattern in content else "❌"
        print(f"{status} {name}")

    print("-" * 60)

    if all(pattern in content for pattern, _ in checks):
        print("\n✅ CSS del dropdown parece correcto")
    else:
        print("\n⚠️ Algunos patrones faltan en el CSS")

    print("=" * 60)


if __name__ == "__main__":
    check_dropdown_css()
