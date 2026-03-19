# ============================================================================
# BOLETÍN 5 - EJERCICIO 1
# ============================================================================
# ENUNCIADO:
# Escribir un programa que genere una lista con 10 números aleatorios
# comprendidos entre el 1 y el 500 y la muestre por pantalla ordenada.
# A continuación nos debería de pedir un número por teclado y decirnos
# si está o no en la lista y cuantos de los números son menores al que
# le hemos dado
#
# CONCEPTOS CLAVE:
# - Listas y métodos (append, sort)
# - random.randint() para generar números
# - Operador in para buscar en lista
# - Bucle para contar elementos que cumplen condición
# ============================================================================

print("=" * 50)
print("EJERCICIO 1: Lista de números aleatorios")
print("=" * 50)

import random

# Generar lista con 10 números aleatorios entre 1 y 500
numeros = []
for i in range(10):
    numeros.append(random.randint(1, 500))

# Ordenar la lista
numeros.sort()

print("\n📋 Lista generada (ordenada):")
print(numeros)

print("\n" + "-" * 40)

# Pedir número al usuario
numero_buscar = int(input("Introduce un número para buscar: "))

print("-" * 40)

# Comprobar si está en la lista
if numero_buscar in numeros:
    print(f"✓ El número {numero_buscar} SÍ está en la lista.")
    print(f"  Posición: {numeros.index(numero_buscar) + 1}")
else:
    print(f"✗ El número {numero_buscar} NO está en la lista.")

# Contar cuántos números son menores
contador_menores = 0
for num in numeros:
    if num < numero_buscar:
        contador_menores += 1

print(f"\n📊 Números menores que {numero_buscar}: {contador_menores}")

# Versión compacta con sum() y comprensión de listas
# contador_menores = sum(1 for num in numeros if num < numero_buscar)

print("-" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
