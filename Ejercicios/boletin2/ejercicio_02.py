# ============================================================================
# BOLETÍN 2 - EJERCICIO 2
# ============================================================================
# ENUNCIADO:
# Idem al anterior pero pidiéndonos apellidos de personas
#
# CONCEPTOS CLAVE:
# - Ordenación alfabética de strings
# - input() para texto (no necesita conversión)
# - Las cadenas se comparan alfabéticamente con < y >
# ============================================================================

print("=" * 50)
print("EJERCICIO 2: Ordenar 3 apellidos alfabéticamente")
print("=" * 50)

# Pedir los tres apellidos
# input() sin int() porque son textos
apellido1 = input("Introduce el primer apellido: ")
apellido2 = input("Introduce el segundo apellido: ")
apellido3 = input("Introduce el tercer apellido: ")

print("\n" + "-" * 40)
print(f"Apellidos introducidos: {apellido1}, {apellido2}, {apellido3}")
print("-" * 40)

# FORMA 1: Usando lista y sort()
print("\n--- Forma 1: Usando sort() ---")

apellidos = [apellido1, apellido2, apellido3]
apellidos.sort()  # Ordena alfabéticamente

print("Apellidos ordenados alfabéticamente:")
for i, apellido in enumerate(apellidos, 1):
    print(f"  {i}. {apellido}")

# FORMA 2: Usando sorted() con key para ignorar mayúsculas/minúsculas
print("\n--- Forma 2: Ordenación case-insensitive ---")

apellidos_ci = sorted([apellido1, apellido2, apellido3], 
                       key=str.lower)  # Ignora mayúsculas

print("Apellidos ordenados (ignorando mayúsculas):")
for i, apellido in enumerate(apellidos_ci, 1):
    print(f"  {i}. {apellido}")

# NOTA IMPORTANTE:
# En ordenación alfabética:
# - Las MAYÚSCULAS van antes que las minúsculas
# - "Zapata" < "alba" (porque Z < a en ASCII)
# - Para ordenar correctamente usar key=str.lower

print("-" * 40)

# EJEMPLOS DE COMPARACIÓN DE STRINGS:
# --------------------------------------------------------
# | Comparación      | Resultado | Explicación           |
# |------------------|-----------|-----------------------|
# | "Alba" < "Pérez" | True      | A va antes que P      |
# | "Zapata" < "alba"| True      | Z(90) < a(97) ASCII   |
# | "García" == "garcía" | False | Diferentes (G ≠ g)    |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
