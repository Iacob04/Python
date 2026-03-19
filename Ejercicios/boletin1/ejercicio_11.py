# ============================================================================
# BOLETÍN 1 - EJERCICIO 11
# ============================================================================
# ENUNCIADO:
# Modificar el programa del punto anterior para que si el primer número
# que metemos es mayor que el segundo funcione correctamente.
# Es decir, si metemos 50 y 10, nos genere un número entre 10 y 50.
#
# CONCEPTOS CLAVE:
# - if para intercambiar valores si es necesario
# - Uso de variable auxiliar para intercambio
# - También se puede usar min() y max()
# ============================================================================

print("=" * 50)
print("EJERCICIO 11: Número aleatorio (versión mejorada)")
print("=" * 50)

import random

# Pedir los dos números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print("\n" + "-" * 40)

# FORMA 1: Usando if para intercambiar si es necesario
print("--- Forma 1: Intercambio con if ---")

# Guardamos los valores originales para mostrarlos
original1 = num1
original2 = num2

# Si num1 es mayor que num2, los intercambiamos
if num1 > num2:
    # Intercambio usando variable auxiliar
    auxiliar = num1
    num1 = num2
    num2 = auxiliar
    print(f"(Se han intercambiado: {original1} y {original2})")

# Ahora num1 siempre es menor o igual que num2
numero_aleatorio = random.randint(num1, num2)
print(f"Número aleatorio entre {num1} y {num2}: {numero_aleatorio}")

# FORMA 2: Usando min() y max() (más elegante)
print("\n--- Forma 2: Usando min() y max() ---")

# min() devuelve el menor de los dos
# max() devuelve el mayor de los dos
limite_inferior = min(original1, original2)
limite_superior = max(original1, original2)

numero_aleatorio2 = random.randint(limite_inferior, limite_superior)
print(f"Número aleatorio entre {limite_inferior} y {limite_superior}: {numero_aleatorio2}")

print("-" * 40)

# EXPLICACIÓN DE LAS FUNCIONES:
# --------------------------------------------------------
# | Función      | Descripción                          | Ejemplo          |
# |--------------|--------------------------------------|------------------|
# | min(a, b)    | Devuelve el valor menor              | min(50, 10) = 10 |
# | max(a, b)    | Devuelve el valor mayor              | max(50, 10) = 50 |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
