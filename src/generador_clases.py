# ============================================
# GENERADOR DE TODAS LAS CLASES + ÍNDICE
# ============================================

from pathlib import Path
from datos_clases import clases

# --- VARIABLES COMUNES ---
autor = "Gustavo Vallejo"
curso = "AtriumEdu - Taller Python"

# --- FUNCIÓN PARA GENERAR HTML DE UNA CLASE ---


def generar_html_clase(clase):
    numero = clase['numero']
    return f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clase {numero}: {clase['titulo']}</title>
    <link rel="stylesheet" href="../static/css/estilo.css">
</head>
<body class="clase-{numero}">
    <div class="contenedor">
        <header>
            <h1>🐍 Clase {numero}: {clase['titulo']}</h1>
            <div class="info-meta">
                <p><strong>Fecha:</strong> {clase['fecha']}</p>
                <p><strong>Autor:</strong> {autor}</p>
            </div>
        </header>
        
        <main>
            <h2>Temas de la sesión</h2>
            <ul>
                {''.join([f"<li>{tema}</li>" for tema in clase['temas']])}
            </ul>
            
            <div class="destacado">
                {clase['contenido']}
            </div>
            
            <h3>Próximos pasos</h3>
            <p>Continúa practicando los ejercicios y prepara las preguntas para la siguiente clase.</p>
        </main>
        
        <footer>
            <p>© 2026 {curso} | Creado con ❤️ para estudiantes</p>
            <p><a href="index.html">⬅ Volver al Índice</a></p>
        </footer>
    </div>
</body>
</html>
"""

# --- FUNCIÓN PARA GENERAR EL ÍNDICE ---


def generar_html_index():
    tarjetas = ""
    for clase in clases:
        numero = clase['numero']
        titulo = clase['titulo']
        fecha = clase['fecha']
        tarjetas += f"""
        <div class="card">
            <div class="card-header clase-{numero}">
                <h3>Clase {numero}</h3>
                <span>{fecha}</span>
            </div>
            <div class="card-body">
                <h4>{titulo}</h4>
                <p>Temas: {', '.join(clase['temas'][:2])}...</p>
                <a href="clase_{numero}.html" class="btn btn-clase-{numero}">Ver Clase ➜</a>
            </div>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índice - {curso}</title>
    <link rel="stylesheet" href="../static/css/estilo.css">
</head>
<body class="clase-index">
    <div class="contenedor">
        <header>
            <h1>🐍 {curso}</h1>
            <div class="info-meta">
                <p><strong>Alumno:</strong> {autor}</p>
                <p><strong>Estado:</strong> En progreso</p>
            </div>
        </header>
        
        <main>
            <h2>Selecciona una clase para comenzar</h2>
            <div class="grid-clases">
                {tarjetas}
            </div>
        </main>
        
        <footer>
            <p>© 2026 {curso} | Creado con mucho respeto para los estudiantes</p>
        </footer>
    </div>
</body>
</html>
"""
# --- PROCESO PRINCIPAL ---


def main():
    base_dir = Path(__file__).resolve().parent.parent
    output_dir = base_dir / "output"

    # Crear carpeta output si no existe
    output_dir.mkdir(exist_ok=True)

    print("🚀 Generando páginas de clases e índice...")

    # 1. Generar clases individuales
    for clase in clases:
        archivo_salida = output_dir / f"clase_{clase['numero']}.html"
        contenido = generar_html_clase(clase)

        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(contenido)

        print(f"✅ Clase {clase['numero']}: {archivo_salida.name}")

    # 2. Generar el Índice
    archivo_index = output_dir / "index.html"
    contenido_index = generar_html_index()

    with open(archivo_index, "w", encoding="utf-8") as f:
        f.write(contenido_index)

    print(f"✅ Índice: {archivo_index.name}")

    print("\n🎉 ¡Todo generado exitosamente!")
    print(f"📂 Carpeta de salida: {output_dir}")
    print("🌐 Abre: http://localhost/Taller_Python_Atrium/output/index.html")


if __name__ == "__main__":
    main()
