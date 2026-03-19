# ============================================================================
# BOLETÍN 2 - EJERCICIO 10
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que nos pida elegir entre cuatro destinos
# turísticos (Francia, Italia, Chile o Japón) y dependiendo de nuestra
# respuesta nos diga cual es la capital de nuestro destino
# (París, Roma, Santiago de Chile o Tokio)
#
# CONCEPTOS CLAVE:
# - Estructura if-elif-else para múltiples opciones
# - Comparación de strings
# - Diccionario como alternativa a múltiples if
# ============================================================================

print("=" * 50)
print("EJERCICIO 10: Destinos turísticos")
print("=" * 50)

# Mostrar opciones disponibles
print("\n🌍 DESTINOS TURÍSTICOS DISPONIBLES:")
print("-" * 40)
print("  1. Francia")
print("  2. Italia")
print("  3. Chile")
print("  4. Japón")
print("-" * 40)

# Pedir destino
destino = input("\nElige tu destino: ")

print("\n" + "-" * 40)

# FORMA 1: Usando if-elif-else
print("--- Resultado (con if-elif) ---")

# Normalizar entrada (quitar espacios y poner primera letra mayúscula)
destino = destino.strip().title()

if destino == "Francia":
    capital = "París"
    print(f"✓ Has elegido {destino}")
    print(f"  La capital es: {capital}")
elif destino == "Italia":
    capital = "Roma"
    print(f"✓ Has elegido {destino}")
    print(f"  La capital es: {capital}")
elif destino == "Chile":
    capital = "Santiago de Chile"
    print(f"✓ Has elegido {destino}")
    print(f"  La capital es: {capital}")
elif destino == "Japon" or destino == "Japón":
    capital = "Tokio"
    print(f"✓ Has elegido Japón")
    print(f"  La capital es: {capital}")
else:
    print(f"✗ '{destino}' no es un destino válido.")
    print("  Opciones: Francia, Italia, Chile, Japón")

# FORMA 2: Usando diccionario (más elegante y escalable)
print("\n--- Forma 2: Usando diccionario ---")

# Diccionario con país: capital
capitales = {
    "Francia": "París",
    "Italia": "Roma",
    "Chile": "Santiago de Chile",
    "Japon": "Tokio",
    "Japón": "Tokio"
}

# Buscar en el diccionario
if destino in capitales:
    print(f"✓ La capital de {destino} es {capitales[destino]}")
else:
    print(f"✗ Destino no encontrado")

print("-" * 40)

# VENTAJAS DEL DICCIONARIO:
# --------------------------------------------------------
# | Aspecto        | if-elif          | Diccionario      |
# |----------------|------------------|------------------|
# | Legibilidad    | Peor (más largo) | Mejor            |
# | Escalabilidad  | Añadir más if    | Añadir entrada   |
# | Mantenimiento  | Más difícil      | Más fácil        |
# | Velocidad      | O(n)             | O(1)             |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
