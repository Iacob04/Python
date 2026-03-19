# ============================================================================
# BOLETÍN 1 - EJERCICIO 8
# ============================================================================
# ENUNCIADO:
# Escribir un programa que genere un número aleatorio entre el 0 y el 50
# y lo muestre
#
# CONCEPTOS CLAVE:
# - import random: importa el módulo para números aleatorios
# - random.randint(a, b): genera número entero aleatorio entre a y b (incluidos)
# - random.randrange(a, b): genera número entre a y b-1
# ============================================================================

print("=" * 50)
print("EJERCICIO 8: Número aleatorio entre 0 y 50")
print("=" * 50)

# Importar el módulo random
# Este módulo contiene funciones para generar números aleatorios
import random

print("\n--- Usando random.randint() ---")
# random.randint(inicio, fin) incluye AMBOS extremos
# Genera un número entre 0 y 50 (ambos incluidos)
numero_aleatorio = random.randint(0, 50)
print(f"Número aleatorio generado: {numero_aleatorio}")

print("\n--- Usando random.randrange() ---")
# random.randrange(inicio, fin) NO incluye el fin
# Genera un número entre 0 y 49 (el 50 no está incluido)
# Por eso ponemos 51 como límite superior
numero_aleatorio2 = random.randrange(0, 51)
print(f"Número aleatorio generado: {numero_aleatorio2}")

# GENERAR VARIOS NÚMEROS PARA VER LA VARIABILIDAD
print("\n--- Generando 10 números aleatorios ---")
for i in range(10):
    num = random.randint(0, 50)
    print(f"Número {i+1}: {num}")

# EXPLICACIÓN DE LAS FUNCIONES:
# --------------------------------------------------------
# | Función              | Rango         | Incluye fin?  |
# |----------------------|---------------|---------------|
# | randint(0, 50)       | 0 a 50        | SÍ            |
# | randrange(0, 51)     | 0 a 50        | NO            |
# | randrange(0, 50)     | 0 a 49        | NO            |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
