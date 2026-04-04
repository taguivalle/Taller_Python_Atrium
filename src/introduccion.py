# ============================================
# ARCHIVO: src/introduccion.py
# AUTOR: Gustavo Vallejo
# FECHA: 04 de Abril de 2026
# ============================================

# --- VARIABLES ---
titulo = "🐍 Bienvenido a AtriumEdu - Taller Python"
autor = "Gustavo Vallejo"
fecha = "04 de Abril de 2026"

# --- CONTENIDO HTML MEJORADO ---
contenido_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <!-- Con este link se inserta el icono en el título de la pagina "Blog de Café. " 
    https://imagen.online-convert.com/es/convertir/png-a-ico. -->
    <link rel="shortcut icon" href="../output/icons/introduccionPython.ico" type="image/x-icon">
    <!-- Este es el preload del google font. -->
    <link rel="preload" href="https://fonts.googleapis.com" as="font">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <!-- Este es el preload del google font. -->
    <link rel="preload" href="https://fonts.gstatic.com" crossorigin="crossorigin" as="font">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <!-- Este es el preload del google font. -->
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=PT+Sans:wght@400;700&display=swap"
        crossorigin="crossorigin" as="font">
    <link rel="preconnect" href="https://fonts.googleapis.com/css2?family=PT+Sans:wght@400;700&display=swap">
    <!-- Los preloads nos permite recargar más rápidamente. Para este caso de los estilos. -->
    <link rel="preload" href="css/style.css" crossorigin="crossorigin" as="css">
    <link rel="stylesheet" href="css/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- El prefetch nos permite llevar la siguiente página que esperaríamos (Una especie de intuición) que el usuario 
    visite más rápidamente y/o para darle una mejor experiencia. (Google analytics) -->
    <link rel="prefetch" href="" as="document">
    <link rel="stylesheet" href="../static/css/estilo.css">
</head>
<body>
    <div class="contenedor">
        <header>
            <h1>{titulo}</h1>
            <div class="info-meta">
                <p><strong>Autor:</strong> {autor}</p>
                <p><strong>Fecha:</strong> {fecha}</p>
            </div>
        </header>
        
        <main>
            <h2>🎯 ¿Qué vas a lograr en esta sesión?</h2>
            <div class="destacado">
                <ul>
                    <li>📦 Declararás variables sin dolor de cabeza</li>
                    <li>🔢 Harás cálculos matemáticos como un pro</li>
                    <li>📝 Manipularás textos con facilidad</li>
                    <li>💬 Conversarás con el usuario usando input()</li>
                    <li>🎮 Resolverás ejercicios reales</li>
                </ul>
            </div>
            
            <h2>🤔 ¿Por qué Python es tan especial?</h2>
            <p>En muchos lenguajes, tienes que decirle al computador: <em>"Oye, esta variable va a guardar un número entero"</em>.</p>
            <p>En Python, es más relajado:</p>
            
            <div class="destacado">
                <h3>❌ Otros lenguajes (más estrictos)</h3>
                <pre>int numero = 10;
string nombre = "Ana";</pre>
                
                <h3>✅ Python (más flexible)</h3>
                <pre>numero = 10
nombre = "Ana"</pre>
            </div>
            
            <p><strong>💡 Analogía:</strong> Piensa en las variables como <strong>cajas mágicas</strong>:</p>
            <ul>
                <li>No necesitas etiquetarlas antes de usarlas</li>
                <li>Puedes cambiar lo que guardan dentro</li>
                <li>Python se encarga de saber qué hay adentro</li>
            </ul>
            
            <h2>📦 1. Declarando tu primera variable</h2>
            <pre>
# Declaración simple
a = 10
print("'a' vale:", a)

# ¡Puedes cambiar el contenido!
a = "abcd"
print("Ahora 'a' vale:", a)</pre>
            
            <p><strong>⚠️ Importante:</strong> En Python, una variable puede cambiar de tipo durante su vida útil. ¡Es como un camaleón!</p>
            
            <h2>🎨 2. Tipos de datos básicos (los "primitivos")</h2>
            
            <table style="width:100%; border-collapse: collapse; margin: 20px 0;">
                <thead>
                    <tr style="background: var(--color-primario); color: white;">
                        <th style="padding: 10px; border: 1px solid #ddd;">Tipo</th>
                        <th style="padding: 10px; border: 1px solid #ddd;">Nombre</th>
                        <th style="padding: 10px; border: 1px solid #ddd;">Ejemplo</th>
                        <th style="padding: 10px; border: 1px solid #ddd;">¿Para qué sirve?</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ddd;"><strong>int</strong></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Enteros</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>x = 10</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Números sin decimales</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px; border: 1px solid #ddd;"><strong>float</strong></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Decimales</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>pi = 3.14159</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Números con coma</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ddd;"><strong>complex</strong></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Complejos</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>z = 2 + 3j</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Matemáticas avanzadas</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px; border: 1px solid #ddd;"><strong>bool</strong></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Booleanos</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>is_active = True</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Verdadero/Falso</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ddd;"><strong>str</strong></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Texto</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>name = "Python"</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Cadenas de caracteres</td>
                    </tr>
                </tbody>
            </table>
            
            <h2>🔍 3. ¿Cómo sé qué tipo de dato tengo?</h2>
            <p>Usa la función <code>type()</code> - es como una "radiografía" de tu variable:</p>
            <pre>var_1 = 100
print(type(var_1))  # Salida: &lt;class 'int'&gt;

var_1 = "abcd"
print(type(var_1))  # Salida: &lt;class 'str'&gt;</pre>
            
            <p><strong>💡 Tip de experto:</strong> Usa <code>type()</code> cuando tengas dudas. Es mejor preguntar que asumir.</p>
            
            <h2>➕ 4. Trabajando con números (matemáticas básicas)</h2>
            
            <table style="width:100%; border-collapse: collapse; margin: 20px 0;">
                <thead>
                    <tr style="background: var(--color-primario); color: white;">
                        <th style="padding: 10px; border: 1px solid #ddd;">Operador</th>
                        <th style="padding: 10px; border: 1px solid #ddd;">Nombre</th>
                        <th style="padding: 10px; border: 1px solid #ddd;">Ejemplo</th>
                        <th style="padding: 10px; border: 1px solid #ddd;">Resultado</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>+</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Suma</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>10 + 5</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>15</code></td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>-</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Resta</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>10 - 5</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>5</code></td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>*</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Multiplicación</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>10 * 5</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>50</code></td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>/</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">División</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>10 / 5</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>2.0</code></td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>//</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">División entera</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>10 // 3</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>3</code></td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>%</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Módulo (resto)</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>10 % 3</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>1</code></td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>**</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;">Potencia</td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>10 ** 2</code></td>
                        <td style="padding: 10px; border: 1px solid #ddd;"><code>100</code></td>
                    </tr>
                </tbody>
            </table>
            
            <h2>💬 5. Leyendo datos del usuario (input)</h2>
            <pre>
# Con mensaje personalizado
nombre = input("Introduce tu nombre: ")

# El resultado SIEMPRE es un string
print(type(nombre))  # &lt;class 'str'&gt;

# Para enteros
numero = int(input("Introduce un número entero: "))

# Para decimales
numero = float(input("Introduce un número decimal: "))</pre>
            
            <div class="destacado">
                <strong>⚠️ Advertencia:</strong> Si el usuario escribe letras en lugar de números al usar <code>int()</code> o <code>float()</code>, dará error. ¡Cuidado!
            </div>
            
            <h2>🎯 6. Ejercicio práctico</h2>
<p>Intenta crear este pequeño programa:</p>
<pre>
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
estatura = float(input("Introduce tu estatura: "))

print(f"\n{{'='*40}}")
print(f"👤 Nombre completo: {{nombre}}")
print(f"🎂 Edad: {{edad}} años")
print(f"📏 Estatura: {{estatura}} metros")
print(f"{{'='*40}}")</pre>
            
            <h2>🎉 ¡Felicidades!</h2>
            <p>Si llegaste hasta aquí, ya tienes las bases para:</p>
            <ul>
                <li>✅ Crear y usar variables</li>
                <li>✅ Realizar cálculos matemáticos</li>
                <li>✅ Manipular textos</li>
                <li>✅ Interactuar con el usuario</li>
            </ul>
            
            <blockquote>
                <p><strong>"Cada experto fue alguna vez un principiante. Lo único que los separa es la práctica constante."</strong></p>
            </blockquote>
        </main>
        
        <footer>
            <p>© 2026 AtriumEdu - Taller Python | Creado con mucho respeto para los estudiantes</p>
        </footer>
    </div>
</body>
</html>
"""

# --- ESCRITURA EN CARPETA OUTPUT ---
with open("../output/introduccion.html", "w", encoding="utf-8") as archivo:
    archivo.write(contenido_html)

print("✅ Archivo 'introduccion.html' creado exitosamente en la carpeta 'output'.")
print("📄 Abre el archivo en tu navegador para ver el resultado.")
