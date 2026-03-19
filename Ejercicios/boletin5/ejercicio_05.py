# ============================================================================
# BOLETÍN 5 - EJERCICIO 5
# ============================================================================
# ENUNCIADO:
# Una lotería primitiva está formada por seis números y otro adicional
# para el reintegro. Los seis primeros números están comprendidos entre
# el 1 y el 49 (ambos inclusive) que no pueden estar repetidos. El
# reintegro es un número entre el 0 y el 9. Haced un programa en python
# que calcule una combinación de números de forma aleatoria para la
# primitiva cumpliendo las normas y que luego la muestre por pantalla
# ordenada de menor a mayor. Lógicamente, también debería de mostrar
# el complementario.
#
# CONCEPTOS CLAVE:
# - random.sample() para números sin repetición
# - sorted() para ordenar
# - random.randint() para el reintegro
# ============================================================================

print("=" * 50)
print("EJERCICIO 5: Generador de Primitiva (sin repeticiones)")
print("=" * 50)

import random

print("\n🎰 GENERANDO COMBINACIÓN DE PRIMITIVA 🎰")
print("-" * 40)

# Generar 6 números únicos entre 1 y 49
# random.sample() elige elementos sin repetición
numeros = random.sample(range(1, 50), 6)

# Ordenar los números
numeros_ordenados = sorted(numeros)

# Generar reintegro (0-9)
reintegro = random.randint(0, 9)

# Mostrar resultados
print("\n📋 Tu combinación de la Primitiva:")
print("-" * 40)
print("Números principales:")
print("  ", end="")
for i, num in enumerate(numeros_ordenados):
    if i < len(numeros_ordenados) - 1:
        print(f"{num:2d} - ", end="")
    else:
        print(f"{num:2d}")

print("-" * 40)
print(f"Reintegro: {reintegro}")
print("=" * 40)

# EXPLICACIÓN DE random.sample():
# --------------------------------------------------------
# | Función                    | Uso                      |
# |----------------------------|--------------------------|
# | random.sample(lista, n)    | Elige n elementos únicos |
# | range(1, 50)               | Números del 1 al 49      |
# --------------------------------------------------------
#
# Diferencia con random.randint():
# - randint() puede repetir números
# - sample() garantiza que no se repiten

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
