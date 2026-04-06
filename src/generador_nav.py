#!/usr/bin/env python3
# ============================================
# ARCHIVO: src/generador_nav.py
# AUTOR: Gustavo Vallejo
# FECHA: 06 de Abril de 2026
# ============================================

import os
import re
from pathlib import Path

# Configuración
OUTPUT_DIR = Path("output")
NAV_HTML = '''
    <nav class="menu-principal">
        <ul>
            <li><a href="index.html" class="{inicio_class}">🏠 Inicio</a></li>
            <li class="dropdown">
                <a href="#">📚 Clases ▾</a>
                <div class="dropdown-content">
                    <a href="introduccion.html">🐍 Introducción</a>
                    <a href="variables.html">🔢 Variables</a>
                    <a href="estruCondicio.html">🔀 Condicionales</a>
                    <a href="colecciones.html">📚 Colecciones</a>
                    <a href="listas.html">📋 Listas</a>
                    <a href="tuplas.html">🔗 Tuplas</a>
                    <a href="conjuntos.html">🧩 Conjuntos</a>
                    <a href="diccionarios.html">📖 Diccionarios</a>
                    <a href="bucles.html">🔁 Bucles</a>
                    <a href="patroMental.html">🧠 Patrones Mentales</a>
                    <a href="ejercicios.html">📝 Ejercicios</a>
                </div>
            </li>
            <li><a href="https://campusatrium.com" target="_blank">🎓 Campus</a></li>
        </ul>
    </nav>
'''

def get_files_with_extension(directory, extension):
    """Obtiene todos los archivos con una extensión específica"""
    files = []
    for file in directory.iterdir():
        if file.suffix == extension:
            files.append(file.name)
    return sorted(files)

def insert_nav_in_file(filepath, current_page):
    """Inserta el nav en un archivo HTML"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determinar clase activa para "Inicio"
    inicio_class = "activo" if "index.html" in current_page else ""
    
    # Insertar nav después de <header>
    nav_html = NAV_HTML.format(inicio_class=inicio_class)
    
    # Buscar la posición después de </header>
    header_end = content.find('</header>')
    if header_end != -1:
        # Insertar después del cierre de header
        insert_pos = header_end + len('</header>')
        new_content = content[:insert_pos] + '\n' + nav_html + '\n' + content[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Nav agregado a: {current_page}")
        return True
    else:
        print(f"⚠️ No se encontró </header> en: {current_page}")
        return False

def main():
    """Función principal"""
    print("=" * 50)
    print("🔧 GENERADOR DE NAV PARA TODAS LAS PÁGINAS")
    print("=" * 50)
    
    if not OUTPUT_DIR.exists():
        print(f"❌ Error: La carpeta '{OUTPUT_DIR}' no existe")
        return
    
    html_files = get_files_with_extension(OUTPUT_DIR, '.html')
    
    print(f"\n📂 Carpeta: {OUTPUT_DIR.absolute()}")
    print(f"📄 Archivos HTML encontrados: {len(html_files)}")
    print("-" * 50)
    
    success_count = 0
    for html_file in html_files:
        filepath = OUTPUT_DIR / html_file
        if insert_nav_in_file(filepath, html_file):
            success_count += 1
    
    print("-" * 50)
    print(f"\n✅ Proceso completado!")
    print(f"📊 Archivos modificados: {success_count}/{len(html_files)}")
    print("=" * 50)

if __name__ == "__main__":
    main()