# ============================================================================
# BOLETÍN 1 - EJERCICIO 15
# ============================================================================
# ENUNCIADO:
# Escribir un programa que pida un número al usuario y calcule si es primo o no
#
# CONCEPTOS CLAVE:
# - Número primo: solo divisible por 1 y por sí mismo
# - Algoritmo: comprobar si tiene algún divisor entre 2 y número-1
# - Si encontramos un divisor, no es primo
# ============================================================================

print("=" * 50)
print("EJERCICIO 15: ¿Es primo?")
print("=" * 50)

# Pedir número al usuario
numero = int(input("Introduce un número: "))

print("\n" + "-" * 40)

# Casos especiales
if numero <= 1:
    print(f"{numero} NO es primo (los primos son mayores que 1)")
elif numero == 2:
    print(f"{numero} SÍ es primo (el único primo par)")
else:
    # Comprobar si es primo
    es_primo = True  # Asumimos que es primo hasta demostrar lo contrario
    
    # Solo necesitamos comprobar hasta la mitad del número
    # (ningún número tiene divisores mayores que su mitad, excepto él mismo)
    for divisor in range(2, numero // 2 + 1):
        if numero % divisor == 0:
            # Si encontramos un divisor, no es primo
            es_primo = False
            print(f"{numero} es divisible por {divisor}")
            break  # No necesitamos seguir buscando
    
    # Mostrar resultado
    if es_primo:
        print(f"✓ {numero} SÍ es un número primo")
    else:
        print(f"✗ {numero} NO es un número primo")

print("-" * 40)

# EXPLICACIÓN DE NÚMEROS PRIMOS:
# --------------------------------------------------------
# | Número | Divisores      | ¿Primo? | Explicación       |
# |--------|----------------|---------|-------------------|
# | 2      | 1, 2           | SÍ      | Solo 1 y sí mismo |
# | 3      | 1, 3           | SÍ      | Solo 1 y sí mismo |
# | 4      | 1, 2, 4        | NO      | También divisible |
# |        |                |         | por 2             |
# | 5      | 1, 5           | SÍ      | Solo 1 y sí mismo |
# | 6      | 1, 2, 3, 6     | NO      | Divisible por 2 y |
# |        |                |         | 3                 |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
