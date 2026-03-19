# ============================================================================
# BOLETÍN 3 - EJERCICIO 4
# ============================================================================
# ENUNCIADO:
# Modifica el programa anterior para que el programa te de todos los
# intentos que necesites pero que cuando aciertes te informe de cuantas
# veces has fallado antes de lograrlo
#
# CONCEPTOS CLAVE:
# - Bucle while sin límite de intentos
# - Contador de fallos
# - break para salir cuando se acierta
# ============================================================================

print("=" * 50)
print("EJERCICIO 4: Juego - Adivina el número (sin límite)")
print("=" * 50)

import random

# Configuración
NUMERO_MINIMO = 1
NUMERO_MAXIMO = 50

# Generar número secreto
numero_secreto = random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)

print(f"\n🎮 JUEGO: ADIVINA EL NÚMERO")
print("-" * 40)
print(f"Estoy pensando en un número entre {NUMERO_MINIMO} y {NUMERO_MAXIMO}")
print("¡Tienes intentos ilimitados!")
print("-" * 40)

fallos = 0  # Contador de fallos

while True:
    # Pedir intento
    intento = int(input("\nTu intento: "))
    
    # Comprobar resultado
    if intento == numero_secreto:
        print("\n🎉 ¡CORRECTO! ¡Has acertado!")
        break  # Salir del bucle
    elif intento < numero_secreto:
        print("📈 El número secreto es MAYOR.")
        fallos += 1
    else:
        print("📉 El número secreto es MENOR.")
        fallos += 1

# Mostrar estadísticas finales
print("\n" + "=" * 40)
print(f"🏆 ESTADÍSTICAS FINALES:")
print(f"   Número secreto: {numero_secreto}")
print(f"   Fallos cometidos: {fallos}")
print(f"   Intentos totales: {fallos + 1}")

# Mensaje según número de fallos
if fallos == 0:
    print("   🌟 ¡IMPRESIONANTE! A la primera.")
elif fallos <= 3:
    print("   👍 ¡Muy bien! Pocos intentos.")
elif fallos <= 6:
    print("   😊 ¡Bien hecho!")
else:
    print("   😅 Por fin... ¡pero lo lograste!")

print("=" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
