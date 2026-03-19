# ============================================================================
# BOLETÍN 1 - EJERCICIO 9
# ============================================================================
# ENUNCIADO:
# Escribir un programa que genere dos números aleatorios simultáneamente
# entre el 1 y el 6 (simulando una tirada de dos dados)
#
# CONCEPTOS CLAVE:
# - random.randint() para generar números aleatorios
# - Simulación de dados: números del 1 al 6
# - Generar múltiples números aleatorios
# ============================================================================

print("=" * 50)
print("EJERCICIO 9: Simulador de dados")
print("=" * 50)

import random

print("\n🎲 LANZAMIENTO DE DOS DADOS 🎲")
print("-" * 40)

# Generar dos números aleatorios entre 1 y 6
# Cada uno representa un dado
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

# Mostrar resultados
print(f"  Dado 1: {dado1}")
print(f"  Dado 2: {dado2}")
print("-" * 40)

# Calcular la suma de ambos dados
suma = dado1 + dado2
print(f"  SUMA TOTAL: {suma}")

# SIMULAR VARIAS TIRADAS
print("\n" + "=" * 50)
print("SIMULACIÓN DE 5 TIRADAS:")
print("=" * 50)

for tirada in range(1, 6):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    print(f"Tirada {tirada}: [{d1}] + [{d2}] = {total}")

# CONCEPTOS ADICIONALES:
# - Un dado estándar tiene 6 caras numeradas del 1 al 6
# - La suma mínima es 2 (1+1)
# - La suma máxima es 12 (6+6)
# - La suma más probable es 7 (se puede obtener de 6 formas diferentes)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
