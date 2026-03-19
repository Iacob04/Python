# ============================================================================
# BOLETÍN 1 - EJERCICIO 1
# ============================================================================
# ENUNCIADO:
# Escribir un programa donde se muestren los 10 primeros números enteros
#
# CONCEPTOS CLAVE:
# - Bucle for: permite repetir código un número determinado de veces
# - range(): genera una secuencia de números
# - La función range(10) genera números del 0 al 9 (10 números en total)
# ============================================================================

print("=" * 50)
print("EJERCICIO 1: Los 10 primeros números enteros")
print("=" * 50)

# FORMA 1: Usando range() con un solo argumento
# range(10) genera: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print("\n--- Forma 1: range(10) ---")
for numero in range(10):
    print(f"Número: {numero}")

# FORMA 2: Si queremos que empiece en 1 y termine en 10
# range(1, 11) genera: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print("\n--- Forma 2: range(1, 11) ---")
for numero in range(1, 11):
    print(f"Número: {numero}")

# EXPLICACIÓN DE range():
# range(inicio, fin, paso)
# - inicio: número donde empieza (incluido) - por defecto es 0
# - fin: número donde termina (NO incluido) - OBLIGATORIO
# - paso: incremento entre números - por defecto es 1

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
