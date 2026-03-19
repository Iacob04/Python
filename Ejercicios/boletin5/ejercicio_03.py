# ============================================================================
# BOLETÍN 5 - EJERCICIO 3
# ============================================================================
# ENUNCIADO:
# Escribir un programa que vaya llenando una lista con números hasta que
# introduzcamos uno negativo. En ese momento debe de parar y mostrarnos
# la lista ordenada ascendente y descendentemente.
# NOTA: Si introducimos algo que no sea un número debería de advertirnos,
# no introducirlo en la lista pero continuar la introducción de datos
#
# CONCEPTOS CLAVE:
# - Bucle while con condición de salida
# - try-except para manejar errores de conversión
# - Métodos sort() y sorted() con reverse
# ============================================================================

print("=" * 50)
print("EJERCICIO 3: Lista ordenada ascendente y descendente")
print("=" * 50)

# Lista para almacenar los números
numeros = []

print("\nIntroduce números (negativo para terminar):")
print("-" * 40)

while True:
    entrada = input(f"Número #{len(numeros) + 1}: ")
    
    try:
        numero = float(entrada)
        
        # Si es negativo, salir del bucle
        if numero < 0:
            print("-" * 40)
            print("Número negativo introducido. Finalizando...")
            break
        
        # Añadir a la lista
        numeros.append(numero)
        print(f"  ✓ Añadido. Total en lista: {len(numeros)}")
        
    except ValueError:
        print(f"  ⚠ '{entrada}' no es un número válido. Ignorado.")
        continue  # Continuar con la siguiente iteración

print("\n" + "=" * 40)
print("RESULTADOS:")
print("=" * 40)

if len(numeros) > 0:
    # Orden ascendente
    ascendente = sorted(numeros)
    print(f"\n📈 Orden ASCENDENTE:")
    print(ascendente)
    
    # Orden descendente
    descendente = sorted(numeros, reverse=True)
    print(f"\n📉 Orden DESCENDENTE:")
    print(descendente)
    
    print(f"\nTotal de números: {len(numeros)}")
else:
    print("No se introdujo ningún número válido.")

print("=" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
