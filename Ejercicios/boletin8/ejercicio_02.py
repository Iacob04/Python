# ============================================================================
# BOLETÍN 8 - EJERCICIO 2
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que guarde en un diccionario las notas
# de las asignaturas de un alumno. El diccionario no debe crearse
# interactivamente desde el teclado, sino que debe estar ya creado en el
# código. El programa debe mostrar un listado con aquellos módulos que el
# alumno debe de recuperar y la nota que tiene en esos módulos. El programa
# debería de funcionar siempre y no sólo con las notas que aparecen aquí.
# Además, el programa debería de mostrar la nota media con dos decimales.
#
# Tabla de notas:
#   Redes: 4.35
#   Python: 5.15
#   Marcas: 6.30
#   FOL: 8.80
#   Sistemas: 2.25
#   Bases de Datos: 7.00
#
# CONCEPTOS CLAVE:
# - Iterar sobre diccionario con items()
# - Filtrar elementos según condición
# - Calcular media de valores
# ============================================================================

print("=" * 50)
print("EJERCICIO 2: Notas de asignaturas")
print("=" * 50)

# Diccionario con las notas (predefinido)
notas = {
    "Redes": 4.35,
    "Python": 5.15,
    "Marcas": 6.30,
    "FOL": 8.80,
    "Sistemas": 2.25,
    "Bases de Datos": 7.00
}

# NOTA: Para probar el segundo ejemplo del enunciado,
# descomenta la siguiente línea:
# notas = {"Redes": 7.5, "Python": 8.0, "Marcas": 6.5, "FOL": 7.0, "Sistemas": 8.0, "Bases de Datos": 6.0}

print("\n📚 TODAS LAS NOTAS:")
print("-" * 40)
for asignatura, nota in notas.items():
    estado = "✓" if nota >= 5 else "✗"
    print(f"  {estado} {asignatura}: {nota}")

print("\n" + "-" * 40)

# Encontrar asignaturas suspensas (nota < 5)
asignaturas_suspensas = []
for asignatura, nota in notas.items():
    if nota < 5:
        asignaturas_suspensas.append((asignatura, nota))

# Mostrar resultado
if len(asignaturas_suspensas) > 0:
    print("\n⚠ El alumno tiene que recuperar los siguientes módulos:")
    for asignatura, nota in asignaturas_suspensas:
        print(f"    {asignatura} con un {nota}")
else:
    print("\n✓ El alumno no tiene que recuperar ningún módulo")

# Calcular nota media
# sum() suma todos los valores, len() cuenta las asignaturas
nota_media = sum(notas.values()) / len(notas)

print(f"\n📊 La nota media obtenida es de {nota_media:.2f}")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
