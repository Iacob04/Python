# =============================================================================
#  FICHEROS EN PYTHON – LECTURA Y ESCRITURA
#  Apuntes y teoría con ejemplos comentados
# =============================================================================

# -----------------------------------------------------------------------------
# 1. ¿POR QUÉ USAR FICHEROS?
# -----------------------------------------------------------------------------
# Los datos en variables desaparecen al cerrar el programa.
# Los ficheros permiten PERSISTIR datos en el disco duro entre ejecuciones.
#
# Flujo básico:
#   Abrir → Leer / Escribir → Cerrar
#
# Python usa un "file object" como intermediario entre tu código y el SO.


# -----------------------------------------------------------------------------
# 2. MODOS DE APERTURA – open(ruta, modo, encoding)
# -----------------------------------------------------------------------------
#
#  Modo  | Nombre      | Descripción
# -------|-------------|--------------------------------------------------------
#  "r"   | Read        | Lectura (por defecto). ERROR si el fichero no existe.
#  "w"   | Write       | Escritura. Crea el fichero O LO SOBREESCRIBE si ya existe.
#  "a"   | Append      | Añade al final. No destruye el contenido previo.
#  "x"   | Create      | Crea el fichero. ERROR si ya existe.
#  "r+"  | Read+Write  | Lectura Y escritura. El fichero DEBE existir.
#  "b"   | Binary      | Se combina con otro modo: "rb", "wb". Para imágenes, PDFs…
#
# IMPORTANTE: Incluye siempre encoding="utf-8" para evitar problemas
#             con acentos y caracteres especiales (ñ, á, é…)


# -----------------------------------------------------------------------------
# 3. GESTOR DE CONTEXTO – with open(...)
# -----------------------------------------------------------------------------
# ✅ FORMA RECOMENDADA: el fichero se cierra solo al salir del bloque,
#    aunque ocurra un error (excepción).

# with open("ejemplo.txt", "r", encoding="utf-8") as f:
#     contenido = f.read()
# Aquí el fichero YA ESTÁ CERRADO, pero la variable sigue disponible.
# print(contenido)

# ❌ FORMA NO RECOMENDADA: hay que recordar cerrar manualmente.
# f = open("ejemplo.txt", "r")
# contenido = f.read()
# f.close()   ← fácil de olvidar; si hay error antes, no se cierra


# -----------------------------------------------------------------------------
# 4. MÉTODOS DE LECTURA
# -----------------------------------------------------------------------------

# ── 4.1  .read() ──────────────────────────────────────────────────────────────
# Lee TODO el fichero de una vez y lo devuelve como una sola cadena (str).
# Adecuado para ficheros pequeños.

# with open("notas.txt", "r", encoding="utf-8") as f:
#     todo = f.read()          # "línea1\nlínea2\nlínea3\n"
#     print(todo)

# ── 4.2  .readlines() ─────────────────────────────────────────────────────────
# Devuelve una lista donde cada elemento es una línea del fichero (incluye \n).
# Útil cuando quieres trabajar línea a línea de golpe.

# with open("notas.txt", "r", encoding="utf-8") as f:
#     lineas = f.readlines()   # ['línea1\n', 'línea2\n', 'línea3\n']
#     print(lineas[0])         # 'línea1\n'

# ── 4.3  .readline() ──────────────────────────────────────────────────────────
# Lee UNA SOLA línea cada vez que se llama. El cursor avanza al principio
# de la siguiente línea. Devuelve "" (cadena vacía) al llegar al final.

# with open("notas.txt", "r", encoding="utf-8") as f:
#     primera = f.readline()   # 'línea1\n'
#     segunda  = f.readline()  # 'línea2\n'

# ── 4.4  Iteración directa (la más eficiente) ─────────────────────────────────
# Recorre el fichero línea a línea SIN cargarlo entero en memoria.
# Ideal para ficheros grandes.

# with open("notas.txt", "r", encoding="utf-8") as f:
#     for linea in f:
#         print(linea.strip())   # strip() elimina \n y espacios al inicio/final

# ── ⚠️  Advertencia sobre el cursor ───────────────────────────────────────────
# Cada vez que lees, el cursor avanza. Si llamas a .read() y luego a
# .readlines(), el segundo devolverá [] porque el cursor llegó al final.
# Usa f.seek(0) para volver al principio:

# with open("notas.txt", "r", encoding="utf-8") as f:
#     todo   = f.read()
#     f.seek(0)                  # ← vuelve el cursor al inicio
#     lineas = f.readlines()     # ahora sí funciona


# -----------------------------------------------------------------------------
# 5. MÉTODOS DE ESCRITURA
# -----------------------------------------------------------------------------

# ── 5.1  .write(cadena) ───────────────────────────────────────────────────────
# Escribe una cadena en el fichero. NO añade salto de línea automáticamente:
# tienes que incluir \n manualmente si lo necesitas.

# with open("salida.txt", "w", encoding="utf-8") as f:
#     f.write("Primera línea\n")
#     f.write("Segunda línea\n")

# ── 5.2  .writelines(lista) ───────────────────────────────────────────────────
# Escribe todos los elementos de una lista. Tampoco añade \n automáticamente:
# cada elemento de la lista debe incluir su propio \n si lo quieres.

# with open("salida.txt", "w", encoding="utf-8") as f:
#     datos = ["alpha\n", "beta\n", "gamma\n"]
#     f.writelines(datos)

# ── 5.3  Añadir al final con modo "a" ─────────────────────────────────────────
# No destruye el contenido existente, solo agrega al final del fichero.

# with open("salida.txt", "a", encoding="utf-8") as f:
#     f.write("Esta línea se añade al final\n")

# ── 5.4  Lectura y escritura a la vez con "r+" ────────────────────────────────
# El fichero debe existir. El cursor empieza al principio.
# Si escribes antes de leer, sobreescribes desde el inicio.
# Patrón habitual: leer primero con seek(0), modificar y escribir.

# with open("notas.txt", "r+", encoding="utf-8") as f:
#     contenido = f.read()          # lee todo
#     f.seek(0)                     # vuelve al inicio
#     f.write("Nueva primera línea\n" + contenido)


# -----------------------------------------------------------------------------
# 6. TABLA RESUMEN – MÉTODOS DE LECTURA
# -----------------------------------------------------------------------------
#
#  Método          | Devuelve         | Carga todo en memoria | Ideal para
# -----------------|------------------|-----------------------|---------------
#  .read()         | str completo     | Sí                    | Ficheros pequeños
#  .readlines()    | list de líneas   | Sí                    | Procesar lista
#  .readline()     | str (una línea)  | No                    | Leer bajo demanda
#  for linea in f  | str (una línea)  | No                    | Ficheros grandes


# -----------------------------------------------------------------------------
# 7. EJEMPLOS PRÁCTICOS
# -----------------------------------------------------------------------------

# ── Ejemplo A: Contar líneas ───────────────────────────────────────────────────
# contador_lineas = 0
# with open("notas.txt", "r", encoding="utf-8") as f:
#     for linea in f:
#         contador_lineas += 1
# print("Número de líneas:", contador_lineas)


# ── Ejemplo B: Contar palabras ────────────────────────────────────────────────
# contador_palabras = 0
# with open("notas.txt", "r", encoding="utf-8") as f:
#     for linea in f:
#         # strip()  → elimina \n y espacios al inicio/final
#         # split()  → divide la línea en palabras (separador: espacio)
#         # len(...) → cuenta cuántas palabras hay en esa línea
#         contador_palabras += len(linea.strip().split())
# print("Número de palabras:", contador_palabras)


# ── Ejemplo C: Filtrar líneas que contienen una palabra ───────────────────────
# resultados = []
# with open("notas.txt", "r", encoding="utf-8") as f:
#     for linea in f:
#         if "Python" in linea:
#             resultados.append(linea.strip())
# print(resultados)


# ── Ejemplo D: Copiar un fichero ──────────────────────────────────────────────
# with open("original.txt", "r", encoding="utf-8") as origen:
#     with open("copia.txt", "w", encoding="utf-8") as destino:
#         for linea in origen:
#             destino.write(linea)


# -----------------------------------------------------------------------------
# 8. BUENAS PRÁCTICAS – RESUMEN
# -----------------------------------------------------------------------------
#
#  ✅ Usa siempre  with open(...)  para garantizar el cierre del fichero.
#  ✅ Incluye siempre  encoding="utf-8"  para evitar errores con acentos.
#  ✅ Usa la iteración directa (for linea in f) para ficheros grandes.
#  ✅ Recuerda que .write() y .writelines() NO añaden \n automáticamente.
#  ✅ Usa f.seek(0) si necesitas releer el fichero sin cerrarlo.
#  ⚠️  El modo "w" SOBREESCRIBE el fichero. Usa "a" para no perder datos.
#  ⚠️  El modo "r+" requiere que el fichero exista previamente.
