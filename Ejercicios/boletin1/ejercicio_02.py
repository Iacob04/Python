# ============================================================================
# BOLETÍN 1 - EJERCICIO 2
# ============================================================================
# ENUNCIADO:
# Escribir un programa donde se muestren los 50 primeros números pares
#
# CONCEPTOS CLAVE:
# - Número par: divisible por 2 (resto de la división = 0)
# - Operador módulo %: devuelve el resto de una división
# - range(inicio, fin, paso): podemos saltar de 2 en 2 para obtener pares
# ============================================================================

print("=" * 50)
print("EJERCICIO 2: Los 50 primeros números pares")
print("=" * 50)

# FORMA 1: Usando range() con paso 2 (más eficiente)
# Empezamos en 0 (primer par) y vamos de 2 en 2 hasta tener 50 números
# El 100 es el límite (no incluido), así que genera: 0, 2, 4, ..., 98
print("\n--- Forma 1: range(0, 100, 2) ---")
contador = 0
for numero in range(0, 100, 2):
    contador += 1
    print(f"Par #{contador}: {numero}")

# FORMA 2: Usando el operador módulo % para filtrar pares
# Comprobamos si el resto de dividir por 2 es 0
print("\n--- Forma 2: Usando operador % (módulo) ---")
contador = 0
for numero in range(100):  # Del 0 al 99
    if numero % 2 == 0:    # Si el resto de dividir por 2 es 0, es par
        contador += 1
        print(f"Par #{contador}: {numero}")
        if contador == 50:  # Paramos cuando tengamos 50 pares
            break

# EXPLICACIÓN DEL OPERADOR MÓDULO %:
# a % b devuelve el resto de dividir a entre b
# Ejemplos:
#   10 % 2 = 0  (10 es divisible por 2, es PAR)
#   11 % 2 = 1  (11 no es divisible por 2, es IMPAR)
#   15 % 3 = 0  (15 es divisible por 3)
#   17 % 5 = 2  (17 dividido por 5 da resto 2)

print("\n" + "=" * 50)
print(f"Total de números pares mostrados: {contador}")
print("=" * 50)
