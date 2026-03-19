# ============================================================================
# BOLETÍN 3 - EJERCICIO 1
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que pida al usuario un número y escriba
# todos sus divisores
#
# CONCEPTOS CLAVE:
# - Divisor: número que divide exactamente a otro (resto = 0)
# - Bucle para encontrar todos los divisores
# - Operador módulo % para comprobar divisibilidad
# ============================================================================

print("=" * 50)
print("EJERCICIO 1: Divisores de un número")
print("=" * 50)

# Pedir número al usuario
numero = int(input("Introduce un número: "))

print("\n" + "-" * 40)
print(f"Divisores de {numero}:")
print("-" * 40)

# Un número siempre es divisible por 1 y por sí mismo
# Los divisores están entre 1 y el número (incluido)

contador_divisores = 0

for posible_divisor in range(1, numero + 1):
    if numero % posible_divisor == 0:
        # Si el resto es 0, es un divisor
        contador_divisores += 1
        print(f"  {posible_divisor} es divisor de {numero}")
        # Opcional: mostrar la división
        print(f"     {numero} ÷ {posible_divisor} = {numero // posible_divisor}")

print("-" * 40)
print(f"Total de divisores: {contador_divisores}")

# EXPLICACIÓN:
# Si numero = 12:
#   12 ÷ 1 = 12  → resto 0 ✓ divisor
#   12 ÷ 2 = 6   → resto 0 ✓ divisor
#   12 ÷ 3 = 4   → resto 0 ✓ divisor
#   12 ÷ 4 = 3   → resto 0 ✓ divisor
#   12 ÷ 5 = 2.4 → resto 2 ✗ no es divisor
#   12 ÷ 6 = 2   → resto 0 ✓ divisor
#   ...

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
