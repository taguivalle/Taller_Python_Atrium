# ============================================
# ARCHIVO: src/introduccion.py
# AUTOR: Gustavo Vallejo
# FECHA: 03 de Abril de 2026
# ============================================

# --- IMPORTAR LIBRERÍA NECESARIA ---
from pathlib import Path

# --- VARIABLES ---
titulo = "Bienvenido a AtriumEdu - Taller Python"
autor = "Gustavo Vallejo"
fecha = "03 de Abril de 2026"

# --- CONTENIDO HTML MEJORADO ---
contenido_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <link rel="stylesheet" href="../static/css/estilo.css">
</head>
<body>
    <div class="contenedor">
        <header>
            <h1>🐍 {titulo}</h1>
            <div class="info-meta">
                <p><strong>Autor:</strong> {autor}</p>
                <p><strong>Fecha:</strong> {fecha}</p>
            </div>
        </header>
        
        <main>
            <h2>¿Qué es Python?</h2>
            <p>Python es un lenguaje de programación <strong>interpretado</strong>, <strong>multiparadigma</strong> y de <strong>alto nivel</strong>. Se caracteriza por su sintaxis clara y legible, lo que lo hace ideal para estudiantes.</p>
            
            <div class="destacado">
                <strong>💡 Sabías que...</strong> Python fue creado por Guido van Rossum y lanzado oficialmente en 1991. Su nombre viene de "Monty Python", un grupo de comedia británico.
            </div>
            
            <h3>Características principales:</h3>
            <ul>
                <li>Facilidad de aprendizaje y uso</li>
                <li>Gran cantidad de bibliotecas y frameworks</li>
                <li>Soporte para múltiples paradigmas de programación</li>
                <li>Sintaxis elegante y fácil de leer</li>
                <li><strong>Lenguaje de alto nivel:</strong> Se abstrae de los detalles de la máquina</li>
                <li><strong>Lenguaje interpretado:</strong> No necesitas compilar antes de ejecutar</li>
                <li><strong>Propósito general:</strong> Desarrollo web, análisis de datos, IA, automatización, etc.</li>
                <li><strong>Código abierto:</strong> Puedes usarlo, modificarlo y distribuirlo libremente</li>
                <li><strong>Fácil de usar:</strong> Ideal para prototipos sin comprometer mantenibilidad</li>
                <li>Biblioteca estándar amplia para tareas comunes</li>
                <li>Modo interactivo para pruebas rápidas de código</li>
                <li>Se amplía con módulos en C o C++</li>
                <li>Se integra en aplicaciones como interfaz programable</li>
                <li>Multiplataforma: Mac OS X, Windows, Linux, Unix, Android, iOS</li>
                <li><strong>Software libre:</strong> Sin costo y con licencia de código abierto</li>
            </ul>
            
            <h3>Información técnica adicional:</h3>
            <p>Tipos de datos básicos: números (enteros, flotantes, complejos), cadenas (ASCII y Unicode), listas y diccionarios.</p>
            <p>Soporta programación orientada a objetos con clases y herencia múltiple.</p>
            <p>Manejo de excepciones para errores más limpios.</p>
            <p>Gestión automática de memoria.</p>
        </main>
        
        <footer>
            <p>© 2026 AtriumEdu - Taller Python | Creado con ❤️ para estudiantes</p>
        </footer>
    </div>
</body>
</html>
"""

# --- ESCRITURA EN CARPETA OUTPUT (CORREGIDO) ---
# Obtener la ruta base del proyecto (subir 2 niveles desde src/)
base_dir = Path(__file__).resolve().parent.parent
output_file = base_dir / "output" / "introduccion.html"

# Crear la carpeta output si no existe
output_file.parent.mkdir(exist_ok=True)

# Escribir el archivo
with open(output_file, "w", encoding="utf-8") as archivo:
    archivo.write(contenido_html)

print("✅ ¡Archivo HTML generado exitosamente!")
print(f"📄 Archivo creado en: {output_file}")
