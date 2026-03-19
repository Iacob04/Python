# ============================================================================
# BOLETÍN 1 - EJERCICIO 12
# ============================================================================
# ENUNCIADO:
# Escribir un programa que genere seis números aleatorios entre el 1 y el 49
# (simulando una primitiva). Por el momento no te preocupes de que algunos
# números puedan salir repetidos.
#
# CONCEPTOS CLAVE:
# - Bucle for para repetir 6 veces
# - random.randint(1, 49) para números de la primitiva
# - En la primitiva real, los números no se repiten (se verá más adelante)
# ============================================================================

print("=" * 50)
print("EJERCICIO 12: Simulador de Primitiva (con repeticiones)")
print("=" * 50)

import random

print("\n🎰 COMBINACIÓN DE LA PRIMITIVA 🎰")
print("-" * 40)

# Generar 6 números aleatorios entre 1 y 49
print("Tus números de la suerte son:")
print()

for i in range(6):
    numero = random.randint(1, 49)
    print(f"  Número {i+1}: {numero}")

print()
print("-" * 40)

# NOTA IMPORTANTE:
# En este ejercicio los números PUEDEN REPETIRSE
# Por ejemplo, podría salir: 7, 15, 7, 23, 41, 7
# En la primitiva real esto NO es válido (todos diferentes)
# Más adelante aprenderemos a evitar repeticiones

# VERSIÓN EN UNA LÍNEA (para mostrar todos juntos):
print("\n--- Versión compacta ---")
numeros = []
for i in range(6):
    numeros.append(random.randint(1, 49))

print("Combinación:", " - ".join(str(n) for n in numeros))

print("\n" + "=" * 50)
print("NOTA: En este ejercicio los números pueden repetirse.")
print("      En la primitiva real todos los números deben ser")
print("      diferentes.")
print("=" * 50)
