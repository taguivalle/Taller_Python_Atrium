#!/usr/bin/env python3
# ============================================
# ARCHIVO: src/validador_enlaces.py
# AUTOR: Gustavo Vallejo
# FECHA: 06 de Abril de 2026
# ============================================

import os
import re
from pathlib import Path
from collections import defaultdict

# Configuración
OUTPUT_DIR = Path("output")


def extract_links_from_html(filepath):
    """Extrae todos los enlaces href de un archivo HTML"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Buscar todos los href="..."
    pattern = r'href=["\']([^"\']+)["\']'
    matches = re.findall(pattern, content)

    # Filtrar enlaces externos y anclas
    links = []
    for link in matches:
        if not link.startswith(('http://', 'https://', '#', 'mailto:', 'javascript:')):
            links.append(link)

    return links


def validate_links_in_directory(directory):
    """Valida todos los enlaces en un directorio"""
    results = {
        'valid': [],
        'broken': [],
        'external': [],
        'warnings': []
    }

    if not directory.exists():
        print(f"❌ Error: La carpeta '{directory}' no existe")
        return results

    html_files = list(directory.glob("*.html"))

    print(f"\n📂 Analizando: {directory.absolute()}")
    print(f"📄 Archivos HTML: {len(html_files)}")
    print("-" * 60)

    for html_file in html_files:
        print(f"\n🔍 Analizando: {html_file.name}")
        links = extract_links_from_html(html_file)

        for link in links:
            # Verificar si es un enlace interno
            if link.endswith('.html'):
                target_path = directory / link
                if target_path.exists():
                    results['valid'].append((html_file.name, link))
                else:
                    results['broken'].append((html_file.name, link))
            else:
                # Otros enlaces internos (css, js, etc.)
                target_path = directory.parent / link
                if target_path.exists():
                    results['valid'].append((html_file.name, link))
                else:
                    results['warnings'].append((html_file.name, link))

    return results


def print_report(results):
    """Imprime el reporte de validación"""
    print("\n" + "=" * 60)
    print("📊 REPORTE DE VALIDACIÓN DE ENLACES")
    print("=" * 60)

    # Enlaces válidos
    print(f"\n✅ ENLACES VÁLIDOS: {len(results['valid'])}")
    for source, link in results['valid'][:10]:  # Mostrar primeros 10
        print(f"   {source} → {link}")
    if len(results['valid']) > 10:
        print(f"   ... y {len(results['valid']) - 10} más")

    # Enlaces rotos
    if results['broken']:
        print(f"\n❌ ENLACES ROTOS: {len(results['broken'])}")
        for source, link in results['broken']:
            print(f"   {source} → {link}")
    else:
        print(f"\n✅ NO HAY ENLACES ROTOS")

    # Advertencias
    if results['warnings']:
        print(f"\n⚠️ ADVERTENCIAS: {len(results['warnings'])}")
        for source, link in results['warnings']:
            print(f"   {source} → {link}")

    print("\n" + "=" * 60)


def main():
    """Función principal"""
    print("=" * 60)
    print("🔍 VALIDADOR DE ENLACES - AtriumEdu")
    print("=" * 60)

    results = validate_links_in_directory(OUTPUT_DIR)
    print_report(results)

    # Resumen final
    total_issues = len(results['broken']) + len(results['warnings'])
    if total_issues == 0:
        print("\n🎉 ¡FELICIDADES! Todos los enlaces están correctos")
    else:
        print(
            f"\n⚠️ Se encontraron {total_issues} problemas que requieren atención")


if __name__ == "__main__":
    main()
