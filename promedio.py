import os

# Definición de rutas absolutas dentro del Sistema de Archivos
ARCHIVO_NOTAS = "/var/www/html/notas.txt"
ARCHIVO_HTML = "/var/www/html/index.html"

# 1. ESTRUCTURA DE DATOS: Aplicamos listas para el almacenamiento dinámico
lista_notas = []

print("Iniciando proceso de lectura y cálculo del sistema...")

try:
    # 2. GESTIÓN DE ARCHIVOS (Lectura): Verificación e ingreso de datos
    # Si el archivo de texto no existe en el almacenamiento, lo creamos con datos por defecto
    if not os.path.exists(ARCHIVO_NOTAS):
        with open(ARCHIVO_NOTAS, "w") as f:
            f.write("8\n9\n7\n10\n6")
        print("Archivo 'notas.txt' creado con datos iniciales de control.")

    # Apertura y lectura del descriptor de archivo
    with open(ARCHIVO_NOTAS, "r") as f:
        for linea in f:
            # Eliminamos espacios en blanco y convertimos la cadena de texto a entero
            nota = int(linea.strip())
            lista_notas.append(nota)  # Almacenamos en la lista

    # Validación lógica de los datos procesados
    if len(lista_notas) == 0:
        raise ValueError("La lista de notas en memoria se encuentra vacía.")

    # Algoritmo de cálculo aritmético sobre la lista
    promedio = sum(lista_notas) / len(lista_notas)

    # 3. GESTIÓN DE ARCHIVOS (Escritura): Generación de la salida HTML para el servidor web
    contenido_html = f"""<html>
<head><title>TFI - Arquitectura y S.O.</title></head>
<body style='background-color: #0F3D3E; color: #F3EFEA; font-family: sans-serif; text-align: center; padding-top: 50px;'>
    <h1>TFI: Sistema de Gestion de Promedios en la Nube</h1>
    <h3>[Estructura de Datos] Listas procesadas en memoria: {lista_notas}</h3>
    <h2 style='background-color: #f47321; display: inline-block; padding: 10px 20px; border-radius: 5px;'>
        El promedio final calculado es: {promedio:.2f}
    </h2>
    <p>Validacion exitosa: Lectura de archivos, Manejo de excepciones y Despliegue en Servidor Apache2.</p>
</body>
</html>"""

    with open(ARCHIVO_HTML, "w") as f:
        f.write(contenido_html)
    
    print("Transacción exitosa. Interfaz index.html actualizada en el servidor web.")

# 4. MANEJO DE ERRORES: Control estricto de excepciones del sistema operativo y datos
except FileNotFoundError:
    print("Error Crítico de Entrada/Salida: No se encontró el archivo descriptor 'notas.txt'.")
except ValueError as e:
    print(f"Error de Datos: Se detectó una entrada incorrecta. Detalle: {e}")
except Exception as e:
    print(f"Error Inesperado del Sistema Operativo: {e}")
