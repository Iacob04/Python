# ============================================================================
# BOLETÍN 1 - EJERCICIO 3
# ============================================================================
# ENUNCIADO:
# Escribir un programa donde se muestren los 5 primeros números múltiplos
# de uno dado por el usuario
#
# CONCEPTOS CLAVE:
# - input(): captura datos del teclado (siempre devuelve string)
# - int(): convierte string a número entero
# - Múltiplo de N: cualquier número que se obtiene multiplicando N por un entero
# ============================================================================

print("=" * 50)
print("EJERCICIO 3: 5 primeros múltiplos de un número")
print("=" * 50)

# Paso 1: Pedir el número al usuario
# input() muestra el mensaje y espera que el usuario escriba algo
# int() convierte el texto introducido a número entero
numero_base = int(input("Introduce un número para ver sus múltiplos: "))

print(f"\nLos 5 primeros múltiplos de {numero_base} son:")
print("-" * 40)

# Paso 2: Calcular y mostrar los 5 primeros múltiplos
# Un múltiplo de N se calcula como: N × 1, N × 2, N × 3, etc.
for i in range(1, 6):  # Del 1 al 5 (5 iteraciones)
    multiplo = numero_base * i
    print(f"{numero_base} × {i} = {multiplo}")

# EXPLICACIÓN:
# Si el usuario introduce 7:
#   - Iteración 1: 7 × 1 = 7
#   - Iteración 2: 7 × 2 = 14
#   - Iteración 3: 7 × 3 = 21
#   - Iteración 4: 7 × 4 = 28
#   - Iteración 5: 7 × 5 = 35

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
