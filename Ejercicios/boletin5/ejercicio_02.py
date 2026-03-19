# ============================================================================
# BOLETÍN 5 - EJERCICIO 2
# ============================================================================
# ENUNCIADO:
# Escribir un programa que nos pida el nombre, el nombre de la asignatura
# y las notas de un alumno de cada uno de los tres trimestres y lo almacene
# todo en una lista. Luego lo debería de mostrar todo en pantalla junto con
# la media que correspondería a la nota final.
#
# CONCEPTOS CLAVE:
# - Lista con datos de diferentes tipos (string, float)
# - Cálculo de media
# - Formateo de salida
# ============================================================================

print("=" * 50)
print("EJERCICIO 2: Datos del alumno en lista")
print("=" * 50)

# Crear lista vacía para almacenar los datos
datos_alumno = []

print("\n📚 INTRODUCCIÓN DE DATOS DEL ALUMNO")
print("-" * 40)

# Pedir datos y añadirlos a la lista
nombre = input("Nombre del alumno: ")
datos_alumno.append(nombre)

asignatura = input("Nombre de la asignatura: ")
datos_alumno.append(asignatura)

nota1 = float(input("Nota del primer trimestre: "))
datos_alumno.append(nota1)

nota2 = float(input("Nota del segundo trimestre: "))
datos_alumno.append(nota2)

nota3 = float(input("Nota del tercer trimestre: "))
datos_alumno.append(nota3)

# Calcular la media
media = (nota1 + nota2 + nota3) / 3

print("\n" + "=" * 40)
print("BOLETÍN DE NOTAS")
print("=" * 40)

# Mostrar datos desde la lista
print(f"Nombre: {datos_alumno[0]}")
print(f"Asignatura: {datos_alumno[1]}")
print(f"Nota del primer trimestre: {datos_alumno[2]}")
print(f"Nota del segundo trimestre: {datos_alumno[3]}")
print(f"Nota del tercer trimestre: {datos_alumno[4]}")
print("-" * 40)
print(f"Nota media final: {media:.1f}")
print("=" * 40)

# ESTRUCTURA DE LA LISTA:
# --------------------------------------------------------
# | Posición | Contenido              | Tipo             |
# |----------|------------------------|------------------|
# |    0     | Nombre del alumno      | str              |
# |    1     | Nombre de asignatura   | str              |
# |    2     | Nota 1er trimestre     | float            |
# |    3     | Nota 2º trimestre      | float            |
# |    4     | Nota 3er trimestre     | float            |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
