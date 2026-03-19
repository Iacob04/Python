# ============================================================================
# BOLETÍN 1 - EJERCICIO 13
# ============================================================================
# ENUNCIADO:
# Escribir un programa que nos permita generar una quiniela. Para ello nos
# debe generar quince números aleatorios entre el 1 y el 3. Recuerda que
# los resultados válidos son 1, X o 2, así que si te sale un 3 lo que tienes
# que imprimir es una X
#
# CONCEPTOS CLAVE:
# - Generar números 1, 2 o 3
# - Convertir el 3 en "X" (condicional if)
# - La quiniela tiene 15 resultados
# ============================================================================

print("=" * 50)
print("EJERCICIO 13: Generador de Quiniela")
print("=" * 50)

import random

print("\n⚽ RESULTADOS DE LA QUINIELA ⚽")
print("=" * 40)
print()

# Generar 15 resultados (uno por cada partido)
for partido in range(1, 16):
    # Generar número aleatorio entre 1 y 3
    resultado = random.randint(1, 3)
    
    # Convertir el resultado a formato quiniela
    if resultado == 1:
        signo = "1"  # Victoria local
    elif resultado == 2:
        signo = "2"  # Victoria visitante
    else:  # resultado == 3
        signo = "X"  # Empate
    
    # Mostrar el resultado formateado
    print(f"Partido {partido:2d}:  {signo}")

print()
print("=" * 40)

# EXPLICACIÓN DE LA QUINIELA:
# --------------------------------------------------------
# | Signo | Significado                              |
# |-------|------------------------------------------|
# |   1   | Gana el equipo que juega en casa         |
# |   X   | Empate                                   |
# |   2   | Gana el equipo visitante                 |
# --------------------------------------------------------

# VERSIÓN ALTERNATIVA (más compacta):
print("\n--- Versión compacta en una línea ---")
resultados = []
for i in range(15):
    num = random.randint(1, 3)
    resultados.append("1" if num == 1 else "2" if num == 2 else "X")
print(" ".join(resultados))

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
