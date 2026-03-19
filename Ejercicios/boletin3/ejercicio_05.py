# ============================================================================
# BOLETÍN 3 - EJERCICIO 5
# ============================================================================
# ENUNCIADO:
# Escribir un programa que pida números enteros por teclado. La ejecución
# terminará cuando el usuario introduzca la palabra EXIT. En ese momento
# debería de mostrar un mensaje diciendo el número de números introducidos,
# la suma de todos y su media aritmética.
#
# CONCEPTOS CLAVE:
# - Bucle while con condición de salida
# - Acumulador de suma
# - Contador de elementos
# - try-except para manejar entrada no numérica
# ============================================================================

print("=" * 50)
print("EJERCICIO 5: Estadísticas de números introducidos")
print("=" * 50)

# Inicializar variables
contador = 0      # Cuenta cuántos números se han introducido
suma_total = 0    # Acumula la suma de todos los números

print("\nIntroduce números (escribe EXIT para terminar):")
print("-" * 40)

while True:
    entrada = input(f"Número #{contador + 1}: ")
    
    # Comprobar si quiere salir
    if entrada.upper() == "EXIT":
        break
    
    # Intentar convertir a número
    try:
        numero = int(entrada)
        suma_total += numero
        contador += 1
        print(f"  ✓ Añadido. Suma actual: {suma_total}")
    except ValueError:
        print(f"  ✗ '{entrada}' no es un número válido. Inténtalo de nuevo.")

# Mostrar resultados
print("\n" + "=" * 40)
print("RESULTADOS:")
print("-" * 40)

if contador > 0:
    media = suma_total / contador
    print(f"  Números introducidos: {contador}")
    print(f"  Suma total:           {suma_total}")
    print(f"  Media aritmética:     {media:.2f}")
else:
    print("  No se introdujo ningún número.")

print("=" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
