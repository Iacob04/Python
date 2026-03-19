# ============================================================================
# BOLETÍN 1 - EJERCICIO 6
# ============================================================================
# ENUNCIADO:
# Escribir un programa que pida un número al usuario y diga si es
# divisible por 3 o no.
#
# CONCEPTOS CLAVE:
# - input() para entrada de datos
# - Condicional if-else
# - Operador % para comprobar divisibilidad
# ============================================================================

print("=" * 50)
print("EJERCICIO 6: ¿Divisible por 3?")
print("=" * 50)

# Pedir el número al usuario
numero = int(input("Introduce un número: "))

print("\n" + "-" * 40)

# Comprobar si es divisible por 3
# Un número es divisible por 3 cuando numero % 3 == 0
if numero % 3 == 0:
    print(f"✓ El número {numero} SÍ es divisible por 3")
    # Opcional: mostrar el resultado de la división
    print(f"  {numero} ÷ 3 = {numero // 3}")
else:
    print(f"✗ El número {numero} NO es divisible por 3")
    # Opcional: mostrar el resto
    print(f"  Resto de dividir {numero} entre 3: {numero % 3}")

print("-" * 40)

# EJEMPLOS:
# Si introduces 9:  9 % 3 = 0  → SÍ es divisible
# Si introduces 10: 10 % 3 = 1 → NO es divisible
# Si introduces 15: 15 % 3 = 0 → SÍ es divisible
# Si introduces 20: 20 % 3 = 2 → NO es divisible

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
