# ============================================================================
# BOLETÍN 7 - EJERCICIO 1
# ============================================================================
# ENUNCIADO:
# Queremos hacer una función en python que reciba un número (n), y nos
# devuelva una tupla con los n primeros números primos. Muéstrala por
# pantalla. Por ejemplo, si llamamos a nuestra función con el número 5
# nos debería de imprimir lo siguiente:
# (1, 2, 3, 5, 7)
#
# CONCEPTOS CLAVE:
# - Funciones que devuelven tuplas
# - Generación de números primos
# - Bucle while para encontrar n primos
# - Tuplas son inmutables (usamos lista y convertimos)
# ============================================================================

# Función auxiliar para comprobar si es primo
def es_primo(n):
    """Comprueba si un número es primo."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Función principal
def primeros_primos(n):
    """
    Devuelve una tupla con los n primeros números primos.
    
    Parámetros:
        n (int): Cantidad de números primos a generar
    
    Retorna:
        tuple: Tupla con los n primeros primos
    """
    primos = []  # Lista temporal para ir añadiendo primos
    numero = 2   # Empezamos buscando desde el 2
    
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    
    # Convertir lista a tupla y devolver
    return tuple(primos)


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 1: n primeros números primos")
print("=" * 50)

# Ejemplo del enunciado
print("\n📊 Ejemplo: primeros_primos(5)")
print("-" * 40)
resultado = primeros_primos(5)
print(resultado)

# Más ejemplos
print("\n📊 Más ejemplos:")
print("-" * 40)
print(f"primeros_primos(3)  = {primeros_primos(3)}")
print(f"primeros_primos(10) = {primeros_primos(10)}")
print(f"primeros_primos(1)  = {primeros_primos(1)}")

# Versión interactiva
print("\n📊 VERSIÓN INTERACTIVA:")
print("-" * 40)
n = int(input("¿Cuántos números primos quieres? "))
print(f"Resultado: {primeros_primos(n)}")

# NOTA: El enunciado muestra (1, 2, 3, 5, 7) pero 1 NO es primo
# Si se quiere exactamente eso, modificar es_primo() para que 1 sea True

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
