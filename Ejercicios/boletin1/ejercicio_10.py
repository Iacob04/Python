# ============================================================================
# BOLETÍN 1 - EJERCICIO 10
# ============================================================================
# ENUNCIADO:
# Escribir un programa que nos pida dos números y genere un número aleatorio
# comprendido entre ambos. Por el momento no te preocupes de que el primer
# número siempre debería de ser menor que el segundo.
#
# CONCEPTOS CLAVE:
# - random.randint() con límites variables
# - Los límites se toman tal cual se introducen
# ============================================================================

print("=" * 50)
print("EJERCICIO 10: Número aleatorio entre dos números")
print("=" * 50)

import random

# Pedir los dos números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print("\n" + "-" * 40)

# Generar número aleatorio entre los dos números
# NOTA: Si num1 > num2, esto dará ERROR
# (se arregla en el ejercicio 11)
numero_aleatorio = random.randint(num1, num2)

print(f"Números introducidos: {num1} y {num2}")
print(f"Número aleatorio entre ellos: {numero_aleatorio}")

print("-" * 40)

# EXPLICACIÓN DE LA LIMITACIÓN:
# --------------------------------------------------------
# random.randint(a, b) REQUIERE que a <= b
# Si a > b, se produce un error: ValueError
#
# Ejemplo que FUNCIONA:
#   num1 = 10, num2 = 50 → random.randint(10, 50) ✓
#
# Ejemplo que FALLA:
#   num1 = 50, num2 = 10 → random.randint(50, 10) ✗ ERROR
#
# SOLUCIÓN (en ejercicio 11):
#   Comprobar cuál es mayor y ajustar los límites

print("\n" + "=" * 50)
print("NOTA: Este programa falla si el primer número")
print("      es mayor que el segundo. Se arregla en el")
print("      ejercicio 11.")
print("=" * 50)
