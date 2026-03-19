# ============================================================================
# BOLETÍN 7 - EJERCICIO 2
# ============================================================================
# ENUNCIADO:
# Escribir una función en python que reciba una tupla y nos diga por
# pantalla si todos los elementos de la misma son únicos o hay alguno
# repetido. En el segundo caso nos debería de decir todos los elementos
# repetidos y cuantas veces lo están.
#
# Ejemplo:
#   (20, "Elefante", 7, True, "Pantera", "Elefante", False, 7, 7)
# Debería responder:
#   El elemento "Elefante" está repetido 2 veces
#   El elemento 7 está repetido 3 veces
#
# CONCEPTOS CLAVE:
# - Contar ocurrencias con count()
# - set() para obtener elementos únicos
# - Diccionario para contar repeticiones
# ============================================================================

def analizar_repeticiones(tupla):
    """
    Analiza una tupla y muestra qué elementos están repetidos.
    
    Parámetros:
        tupla (tuple): Tupla a analizar
    """
    # Obtener elementos únicos
    elementos_unicos = set(tupla)
    
    # Comprobar si hay repeticiones
    if len(elementos_unicos) == len(tupla):
        print("✓ Todos los elementos son únicos. No hay repeticiones.")
        return
    
    # Hay repeticiones, analizar cuáles
    print("✗ Se encontraron repeticiones:")
    print("-" * 40)
    
    # Para cada elemento único, contar cuántas veces aparece
    for elemento in elementos_unicos:
        conteo = tupla.count(elemento)
        if conteo > 1:
            print(f'El elemento "{elemento}" está repetido {conteo} veces')


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 2: Repeticiones en tupla")
print("=" * 50)

# Ejemplo del enunciado
print("\n📊 Ejemplo del enunciado:")
print("-" * 40)
ejemplo = (20, "Elefante", 7, True, "Pantera", "Elefante", False, 7, 7)
print(f"Tupla: {ejemplo}")
print()
analizar_repeticiones(ejemplo)

# Más ejemplos
print("\n📊 Tupla sin repeticiones:")
print("-" * 40)
ejemplo2 = (1, 2, 3, 4, 5)
print(f"Tupla: {ejemplo2}")
print()
analizar_repeticiones(ejemplo2)

print("\n📊 Otra tupla con repeticiones:")
print("-" * 40)
ejemplo3 = ("a", "b", "a", "c", "b", "a")
print(f"Tupla: {ejemplo3}")
print()
analizar_repeticiones(ejemplo3)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
