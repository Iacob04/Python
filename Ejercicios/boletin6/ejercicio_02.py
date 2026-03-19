# ============================================================================
# BOLETÍN 6 - EJERCICIO 2
# ============================================================================
# ENUNCIADO:
# Escribir una función en python que genere de forma consecutiva tiradas
# de dados aleatorios entre el 1 y el 6 ambos incluidos y los muestre en
# pantalla finalizando la ejecución cuando el valor de todos los dados es
# el mismo. Al finalizar debe de decir cuantas veces ha tenido que lanzar
# los dados para alcanzar ese valor.
#
# EJEMPLO DE EJECUCIÓN:
#   tiradadosmultiple(3)
#   2 – 5 - 1
#   4 – 1 - 4
#   4 – 6 - 6
#   3 – 3 - 3
#   He tenido que lanzar los dados 4 veces para que todos sean iguales
#
# CONCEPTOS CLAVE:
# - Función con parámetro (número de dados)
# - Bucle while con condición de salida
# - Generación de múltiples números aleatorios
# - set() para comprobar si todos los elementos son iguales
# ============================================================================

import random

# Definición de la función
def tiradadosmultiple(cantidad_dados):
    """
    Lanza varios dados hasta que todos muestran el mismo valor.
    
    Parámetros:
        cantidad_dados (int): Número de dados a lanzar
    
    Muestra:
        Cada tirada y el número total de intentos al final
    """
    intentos = 0
    
    while True:
        intentos += 1
        
        # Generar tirada de dados
        dados = []
        for _ in range(cantidad_dados):
            dados.append(random.randint(1, 6))
        
        # Mostrar la tirada
        print(" - ".join(str(d) for d in dados))
        
        # Comprobar si todos son iguales
        # set() elimina duplicados, si solo queda 1 elemento, todos eran iguales
        if len(set(dados)) == 1:
            print(f"He tenido que lanzar los dados {intentos} veces para que todos sean iguales")
            break


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 2: Tirada múltiple de dados")
print("=" * 50)

# Ejemplo del enunciado
print("\n🎲 tiradadosmultiple(3):")
print("-" * 40)
tiradadosmultiple(3)

# Más ejemplos
print("\n🎲 tiradadosmultiple(2):")
print("-" * 40)
tiradadosmultiple(2)

print("\n🎲 tiradadosmultiple(4):")
print("-" * 40)
tiradadosmultiple(4)

# Versión interactiva
print("\n📊 VERSIÓN INTERACTIVA:")
print("-" * 40)
n = int(input("¿Cuántos dados quieres lanzar? "))
print()
tiradadosmultiple(n)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
