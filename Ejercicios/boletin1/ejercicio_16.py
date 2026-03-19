# ============================================================================
# BOLETÍN 1 - EJERCICIO 16
# ============================================================================
# ENUNCIADO:
# Escribir un programa que genere un número aleatorio entre el 10.000.000
# y el 50.000.000 que sea primo
#
# CONCEPTOS CLAVE:
# - Bucle while para generar hasta encontrar uno primo
# - Función que comprueba si un número es primo
# - Números aleatorios en rango grande
# ============================================================================

print("=" * 50)
print("EJERCICIO 16: Generar número primo aleatorio")
print("=" * 50)

import random

# Función para comprobar si un número es primo
def es_primo(n):
    """
    Comprueba si un número n es primo.
    Devuelve True si es primo, False si no lo es.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # Si es par y no es 2, no es primo
        return False
    
    # Solo comprobamos divisores impares hasta la raíz cuadrada
    for divisor in range(3, int(n**0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True


print("\n🔍 Buscando un número primo...")
print("   Rango: 10.000.000 a 50.000.000")
print("-" * 40)

intentos = 0
encontrado = False

while not encontrado:
    # Generar número aleatorio en el rango
    numero = random.randint(10000000, 50000000)
    intentos += 1
    
    # Comprobar si es primo
    if es_primo(numero):
        encontrado = True
        print(f"\n✓ ¡NÚMERO PRIMO ENCONTRADO!")
        print(f"  Número: {numero:,}")  # :, añade separadores de miles
        print(f"  Intentos necesarios: {intentos}")

print("-" * 40)

# NOTA IMPORTANTE:
# Los números primos son menos frecuentes en rangos grandes.
# Aproximadamente 1 de cada 20-30 números es primo en este rango.
# Por eso puede necesitar varios intentos.

# OPTIMIZACIÓN USADA:
# - Solo comprobamos divisores impares (después de verificar que no es par)
# - Solo hasta la raíz cuadrada del número (más eficiente)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
