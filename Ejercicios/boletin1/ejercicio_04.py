# ============================================================================
# BOLETÍN 1 - EJERCICIO 4
# ============================================================================
# ENUNCIADO:
# Escribir un programa donde se muestren todos los números divisibles
# por 7 menores a 10000
#
# CONCEPTOS CLAVE:
# - Número divisible por N: el resto de la división por N es 0
# - Bucle con condición: recorremos todos los números y filtramos
# - range() con límite alto para recorrer muchos valores
# ============================================================================

print("=" * 50)
print("EJERCICIO 4: Números divisibles por 7 menores a 10000")
print("=" * 50)

# FORMA 1: Recorrer todos los números y comprobar divisibilidad
print("\n--- Forma 1: Comprobando cada número ---")
contador = 0

for numero in range(1, 10000):
    if numero % 7 == 0:  # Si el resto de dividir por 7 es 0
        contador += 1
        # Solo mostramos algunos para no llenar la pantalla
        if contador <= 10:
            print(f"{numero} es divisible por 7")
        elif contador == 11:
            print("... (mostrando solo los 10 primeros)")

print(f"\nTotal de números divisibles por 7 menores a 10000: {contador}")

# FORMA 2: Más eficiente - empezar en 7 e ir de 7 en 7
print("\n--- Forma 2: range(7, 10000, 7) - MÁS EFICIENTE ---")
contador = 0
for numero in range(7, 10000, 7):
    contador += 1

print(f"Total de números divisibles por 7 menores a 10000: {contador}")

# CÁLCULO MATEMÁTICO:
# 9999 ÷ 7 = 1428.42...
# Por tanto, hay 1428 números divisibles por 7 menores a 10000

# EXPLICACIÓN:
# Un número es divisible por 7 cuando: número % 7 == 0
# En lugar de comprobar todos los números, podemos:
# - Empezar en el primer múltiplo: 7
# - Ir saltando de 7 en 7: 7, 14, 21, 28, 35...
# - Parar antes de llegar a 10000

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
