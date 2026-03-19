# ============================================================================
# BOLETÍN 3 - EJERCICIO 7
# ============================================================================
# ENUNCIADO:
# Escribir un programa en Python que te escriba todos los números primos
# que hay entre el 1 y el 100
#
# CONCEPTOS CLAVE:
# - Función para comprobar si un número es primo
# - Bucle para recorrer el rango
# - Bucle anidado para comprobar divisibilidad
# ============================================================================

print("=" * 50)
print("EJERCICIO 7: Números primos entre 1 y 100")
print("=" * 50)

# Función que comprueba si un número es primo
def es_primo(n):
    """
    Devuelve True si n es primo, False en caso contrario.
    Un número es primo si solo es divisible por 1 y por sí mismo.
    """
    if n <= 1:
        return False  # 0 y 1 no son primos
    if n == 2:
        return True   # 2 es el único primo par
    if n % 2 == 0:
        return False  # Los pares mayores que 2 no son primos
    
    # Comprobar divisores impares hasta la raíz cuadrada
    for divisor in range(3, int(n**0.5) + 1, 2):
        if n % divisor == 0:
            return False
    
    return True


print("\n🔢 NÚMEROS PRIMOS ENTRE 1 Y 100:")
print("-" * 40)

# Lista para guardar los primos encontrados
primos = []

# Recorrer del 1 al 100
for numero in range(1, 101):
    if es_primo(numero):
        primos.append(numero)

# Mostrar resultados
print("Primos encontrados:")
print(", ".join(str(p) for p in primos))

print("\n" + "-" * 40)
print(f"Total de números primos entre 1 y 100: {len(primos)}")

# Mostrar en formato tabla (10 por fila)
print("\n--- Formato tabla (10 por fila) ---")
for i, primo in enumerate(primos):
    print(f"{primo:3d}", end=" ")
    if (i + 1) % 10 == 0:  # Salto de línea cada 10 números
        print()

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
