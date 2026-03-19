# ============================================================================
# BOLETÍN 4 - EJERCICIO 5
# ============================================================================
# ENUNCIADO:
# Escribir un programa python que reciba una cadena de texto y la muestre
# sin vocales. Por ejemplo, si recibe la cadena "Hola Mundo" debería de
# devolver "Hl Mnd".
#
# CONCEPTOS CLAVE:
# - Recorrer cadena carácter por carácter
# - Condicional para filtrar vocales
# - Construir nueva cadena
# ============================================================================

print("=" * 50)
print("EJERCICIO 5: Eliminar vocales de una cadena")
print("=" * 50)

# Pedir cadena
cadena = input("Introduce una cadena de texto: ")

print("\n" + "-" * 40)

# Definir vocales (mayúsculas y minúsculas)
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"

# FORMA 1: Bucle con condicional
resultado = ""
for caracter in cadena:
    if caracter not in vocales:
        resultado += caracter

print(f"Cadena original: '{cadena}'")
print(f"Sin vocales: '{resultado}'")

# FORMA 2: Usando replace() para cada vocal
print("\n--- Forma 2: Usando replace() ---")
resultado2 = cadena
for vocal in "aeiouAEIOU":
    resultado2 = resultado2.replace(vocal, "")

print(f"Sin vocales: '{resultado2}'")

# FORMA 3: Comprensión de listas (avanzado)
print("\n--- Forma 3: Comprensión de listas ---")
resultado3 = "".join([c for c in cadena if c not in vocales])
print(f"Sin vocales: '{resultado3}'")

print("-" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
