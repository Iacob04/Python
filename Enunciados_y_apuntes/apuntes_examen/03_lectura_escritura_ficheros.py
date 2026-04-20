# =============================================================
#  APUNTES EXAMEN — LECTURA Y ESCRITURA DE FICHEROS
# =============================================================
# ÍNDICE:
#   1. Abrir un fichero: open() y modos
#   2. Leer el fichero completo: read() y readlines()
#   3. Leer línea a línea: for línea in fichero
#   4. Escribir en un fichero: write()
#   5. Añadir al final sin borrar: modo "a"
#   6. Leer Y escribir al mismo tiempo: modo "r+"
#   7. Comprobar si existe el fichero: pathlib.Path
#   8. Parsear CSV con split(",")
#   9. Patrón seek(0) + writelines()  →  reescribir el fichero
#  10. Ejemplo completo: inventario de productos
# =============================================================


# ─────────────────────────────────────────────────────────────
# 1 · ABRIR UN FICHERO
# ─────────────────────────────────────────────────────────────
# Siempre usar  with open(...)  → cierra el fichero automáticamente
#
# MODOS:
#   "r"   → solo lectura (falla si no existe)
#   "w"   → escritura (borra el contenido anterior)
#   "a"   → añadir al final (no borra nada)
#   "r+"  → lectura Y escritura (el fichero debe existir)
#   "x"   → crear fichero nuevo (falla si ya existe)
#
# encoding="utf-8"  →  siempre ponerlo para evitar problemas con tildes

# with open("mi_fichero.txt", "r", encoding="utf-8") as f:
#     contenido = f.read()


# ─────────────────────────────────────────────────────────────
# 2 · LEER
# ─────────────────────────────────────────────────────────────

# --- read() → devuelve todo el fichero como UN string ---
# with open("fichero.txt", "r", encoding="utf-8") as f:
#     todo = f.read()
#     print(todo)

# --- readlines() → devuelve una LISTA, cada elemento es una línea ---
# with open("fichero.txt", "r", encoding="utf-8") as f:
#     lineas = f.readlines()   # ["línea1\n", "línea2\n", ...]
#     for linea in lineas:
#         print(linea.strip())  # strip() elimina el \n del final


# ─────────────────────────────────────────────────────────────
# 3 · LEER LÍNEA A LÍNEA (más eficiente con ficheros grandes)
# ─────────────────────────────────────────────────────────────
# with open("fichero.txt", "r", encoding="utf-8") as f:
#     for linea in f:              # itera directamente el fichero
#         datos = linea.strip()    # quita espacios y \n
#         print(datos)


# ─────────────────────────────────────────────────────────────
# 4 · ESCRIBIR  (modo "w" → borra y escribe desde cero)
# ─────────────────────────────────────────────────────────────
# with open("fichero.txt", "w", encoding="utf-8") as f:
#     f.write("Primera línea\n")   # \n para saltar de línea
#     f.write("Segunda línea\n")


# ─────────────────────────────────────────────────────────────
# 5 · AÑADIR AL FINAL  (modo "a" → NO borra el contenido)
# ─────────────────────────────────────────────────────────────
# with open("fichero.txt", "a", encoding="utf-8") as f:
#     f.write("Esta línea se añade al final\n")


# ─────────────────────────────────────────────────────────────
# 6 · LEER Y ESCRIBIR  (modo "r+")
# ─────────────────────────────────────────────────────────────
# Se usa cuando quieres modificar líneas concretas sin perder el resto.
# Patrón:
#   1. readlines()  → leer todas las líneas a una lista
#   2. modificar la lista en memoria
#   3. seek(0)      → volver al inicio del fichero
#   4. writelines() → reescribir todo desde el principio

# with open("fichero.txt", "r+", encoding="utf-8") as f:
#     lineas = f.readlines()
#     lineas[0] = "Línea 0 modificada\n"   # cambiamos la primera línea
#     f.seek(0)          # cursor al inicio
#     f.writelines(lineas)


# ─────────────────────────────────────────────────────────────
# 7 · COMPROBAR SI EXISTE EL FICHERO  →  pathlib.Path
# ─────────────────────────────────────────────────────────────
from pathlib import Path

ruta = Path("inventario.txt")

if not ruta.exists():
    ruta.touch()            # crea el fichero vacío
    print("Fichero creado.")
else:
    print("El fichero ya existe.")

# Path también sirve para:
#   ruta.name          → "inventario.txt"
#   ruta.suffix        → ".txt"
#   ruta.parent        → carpeta que lo contiene


# ─────────────────────────────────────────────────────────────
# 8 · PARSEAR CSV CON split(",")
# ─────────────────────────────────────────────────────────────
# Si el fichero guarda datos separados por comas:
#   sal,50,2
#   jamon,110,2
#
# línea.strip().split(",")  →  ["sal", "50", "2"]
#
# datos[0] = "sal"     → nombre
# datos[1] = "50"      → cantidad   (¡es string! convertir con int())
# datos[2] = "2"       → precio     (¡es string! convertir con float())

# Ejemplo:
# with open("inventario.txt", "r", encoding="utf-8") as f:
#     for linea in f:
#         datos = linea.strip().split(",")
#         nombre   = datos[0]
#         cantidad = int(datos[1])
#         precio   = float(datos[2])
#         print(f"{nombre}: {cantidad} uds. a {precio}€")


# ─────────────────────────────────────────────────────────────
# 9 · PATRÓN seek(0) + writelines()  →  reescribir líneas concretas
# ─────────────────────────────────────────────────────────────
# Úsalo cuando quieras modificar solo UNA línea del fichero.
# Pasos:
#   1. Abrir en modo "r+"
#   2. readlines() → lista de líneas
#   3. for i, linea in enumerate(lineas) → recorrer con índice
#   4. Cuando encuentres la línea a cambiar → lineas[i] = nueva_linea
#   5. seek(0) → volver al principio
#   6. writelines(lineas) → reescribir todo

# with open("inventario.txt", "r+", encoding="utf-8") as f:
#     lineas = f.readlines()
#     for i, linea in enumerate(lineas):
#         datos = linea.strip().split(",")
#         if datos[0] == "sal":
#             lineas[i] = f"sal,999,{datos[2]}\n"  # cambiamos la cantidad
#     f.seek(0)
#     f.writelines(lineas)


# ─────────────────────────────────────────────────────────────
# 10 · EJEMPLO COMPLETO: inventario de productos
# ─────────────────────────────────────────────────────────────

FICHERO = "inventario_demo.txt"

def crear_fichero_demo():
    with open(FICHERO, "w", encoding="utf-8") as f:
        f.write("sal,50,2\n")
        f.write("jamon,110,5\n")
        f.write("aceite,30,8\n")
    print("Fichero demo creado.")


def mostrar_inventario():
    print("--- INVENTARIO ---")
    with open(FICHERO, "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(",")
            nombre   = datos[0]
            cantidad = int(datos[1])
            precio   = float(datos[2])
            print(f"  {nombre:10} | {cantidad:5} uds. | {precio:.2f}€/ud | total: {cantidad*precio:.2f}€")


def añadir_producto(nombre, cantidad, precio):
    with open(FICHERO, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{cantidad},{precio}\n")
    print(f"'{nombre}' añadido al inventario.")


def actualizar_cantidad(nombre_buscado, nueva_cantidad):
    encontrado = False
    with open(FICHERO, "r+", encoding="utf-8") as f:
        lineas = f.readlines()                         # 1. leer todo
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[0].lower() == nombre_buscado.lower():
                lineas[i] = f"{datos[0]},{nueva_cantidad},{datos[2]}\n"  # 2. modificar
                encontrado = True
        if encontrado:
            f.seek(0)              # 3. volver al inicio
            f.writelines(lineas)   # 4. reescribir
            print(f"Cantidad de '{nombre_buscado}' actualizada a {nueva_cantidad}.")
        else:
            print(f"'{nombre_buscado}' no encontrado.")


# --- Ejecución de prueba ---
crear_fichero_demo()
mostrar_inventario()

añadir_producto("arroz", 75, 1.5)
mostrar_inventario()

actualizar_cantidad("sal", 999)
mostrar_inventario()
