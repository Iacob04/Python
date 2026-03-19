# ============================================================================
# BOLETÍN 3 - EJERCICIO 8
# ============================================================================
# ENUNCIADO:
# Modifica el programa anterior para que sea el usuario quién introduzca
# dos números y se nos muestre los primos que hay entre ambos
#
# CONCEPTOS CLAVE:
# - Reutilización de funciones
# - Rango definido por el usuario
# - Uso de min() y max() para asegurar orden correcto
# ============================================================================

print("=" * 50)
print("EJERCICIO 8: Números primos en un rango personalizado")
print("=" * 50)

# Función para comprobar si es primo
def es_primo(n):
    """Devuelve True si n es primo, False en caso contrario."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for divisor in range(3, int(n**0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True


# Pedir rango al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Asegurar que el rango es correcto (inicio < fin)
inicio = min(num1, num2)
fin = max(num1, num2)

print("\n" + "-" * 40)
print(f"🔢 NÚMEROS PRIMOS ENTRE {inicio} Y {fin}:")
print("-" * 40)

# Buscar primos en el rango
primos = []
for numero in range(inicio, fin + 1):
    if es_primo(numero):
        primos.append(numero)

# Mostrar resultados
if len(primos) > 0:
    print("Primos encontrados:")
    print(", ".join(str(p) for p in primos))
    print(f"\nTotal: {len(primos)} números primos")
else:
    print("No se encontraron números primos en este rango.")

# Información adicional
print("-" * 40)
print(f"Rango analizado: {inicio} a {fin}")
print(f"Total de números en el rango: {fin - inicio + 1}")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
