# ============================================================================
# BOLETÍN 3 - EJERCICIO 3
# ============================================================================
# ENUNCIADO:
# Realiza un juego que consiste en acertar un numero que el ordenador
# elige de forma aleatoria entre 1 y 50. Para ello se leen por teclado
# una serie de números, para los que se indica "mayor" o "menor", según
# sea mayor o menor respecto al numero secreto. El proceso termina cuando
# se acierta o cuando se superan el número máximo de intentos establecidos
# en 3.
#
# CONCEPTOS CLAVE:
# - Juego con número aleatorio
# - Bucle con límite de intentos
# - Pistas "mayor/menor" para ayudar al jugador
# ============================================================================

print("=" * 50)
print("EJERCICIO 3: Juego - Adivina el número")
print("=" * 50)

import random

# Configuración del juego (fácil de modificar)
NUMERO_MINIMO = 1
NUMERO_MAXIMO = 50
MAXIMO_INTENTOS = 3

# Generar número secreto
numero_secreto = random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)

print(f"\n🎮 JUEGO: ADIVINA EL NÚMERO")
print("-" * 40)
print(f"Estoy pensando en un número entre {NUMERO_MINIMO} y {NUMERO_MAXIMO}")
print(f"Tienes {MAXIMO_INTENTOS} intentos.")
print("-" * 40)

intentos_realizados = 0
adivinado = False

while intentos_realizados < MAXIMO_INTENTOS and not adivinado:
    # Pedir intento al jugador
    intento = int(input(f"\nIntento {intentos_realizados + 1}/{MAXIMO_INTENTOS}: "))
    intentos_realizados += 1
    
    # Comparar con el número secreto
    if intento == numero_secreto:
        print("🎉 ¡CORRECTO! Has adivinado el número.")
        adivinado = True
    elif intento < numero_secreto:
        print("📈 El número secreto es MAYOR.")
    else:
        print("📉 El número secreto es MENOR.")
    
    # Mostrar intentos restantes
    if not adivinado and intentos_realizados < MAXIMO_INTENTOS:
        print(f"   Te quedan {MAXIMO_INTENTOS - intentos_realizados} intentos.")

# Fin del juego
print("\n" + "=" * 40)
if not adivinado:
    print(f"😢 GAME OVER. El número era: {numero_secreto}")
else:
    print(f"🏆 ¡FELICIDADES! Adivinaste en {intentos_realizados} intentos.")
print("=" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
