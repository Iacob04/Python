# ============================================================================
# BOLETÍN 1 - EJERCICIO 14
# ============================================================================
# ENUNCIADO:
# Escribe un programa que genere números aleatorios entre el 1 y el 1000
# sin parar y que sólo se detenga cuando salga el 666
#
# CONCEPTOS CLAVE:
# - Bucle while True: se ejecuta indefinidamente
# - break: sale del bucle inmediatamente
# - Bucle con condición de parada interna
# ============================================================================

print("=" * 50)
print("EJERCICIO 14: Números aleatorios hasta salir el 666")
print("=" * 50)

import random

print("\n🔢 Generando números entre 1 y 1000...")
print("   (El programa parará cuando salga el 666)")
print("-" * 40)

contador = 0

# Bucle infinito que solo se detiene con break
while True:
    # Generar número aleatorio entre 1 y 1000
    numero = random.randint(1, 1000)
    contador += 1
    
    # Mostrar el número generado
    print(f"Intento {contador}: {numero}")
    
    # Comprobar si es el número buscado
    if numero == 666:
        print()
        print("🎉 ¡Número 666 encontrado!")
        break  # Sale del bucle while

print("-" * 40)
print(f"Total de números generados: {contador}")

# EXPLICACIÓN DE while True:
# --------------------------------------------------------
# while True:
#     # Este código se ejecuta INFINITAMENTE
#     # hasta que encuentre un 'break'
#
# break: instrucción que sale del bucle inmediatamente
# --------------------------------------------------------

# VERSIÓN ALTERNATIVA (con condición en el while):
print("\n--- Versión alternativa (con bandera) ---")
contador = 0
encontrado = False

while not encontrado:
    numero = random.randint(1, 1000)
    contador += 1
    print(f"Intento {contador}: {numero}")
    
    if numero == 666:
        encontrado = True

print(f"¡Encontrado en {contador} intentos!")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
