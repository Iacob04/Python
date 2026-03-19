# ============================================================================
# BOLETÍN 6 - EJERCICIO 3
# ============================================================================
# ENUNCIADO:
# Escribir una función en python que reciba una cadena de texto y un
# carácter y la escriba al revés y suprimiendo las apariciones de ese
# caracter.
#
# EJEMPLO DE EJECUCIÓN:
#   volteayelmimina("Hola mundo cruel", "o")
#   La cadena al revés y sin el carácter 'o' es: leurc odnum alH
#   He eliminado 2 caracteres
#
# CONCEPTOS CLAVE:
# - Manipulación de strings
# - Slicing con paso negativo para invertir [::-1]
# - replace() para eliminar caracteres
# - Contar ocurrencias con count()
# ============================================================================

# Definición de la función
def volteayelmimina(cadena, caracter):
    """
    Invierte una cadena y elimina todas las apariciones de un carácter.
    
    Parámetros:
        cadena (str): Texto a procesar
        caracter (str): Carácter a eliminar
    
    Muestra:
        La cadena procesada y cuántos caracteres se eliminaron
    """
    # Contar cuántas veces aparece el carácter (antes de eliminar)
    eliminados = cadena.count(caracter)
    
    # Eliminar el carácter de la cadena
    sin_caracter = cadena.replace(caracter, "")
    
    # Invertir la cadena (slicing con paso -1)
    invertida = sin_caracter[::-1]
    
    # Mostrar resultados
    print(f"La cadena al revés y sin el carácter '{caracter}' es: {invertida}")
    print(f"He eliminado {eliminados} caracteres")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 3: Voltear y eliminar carácter")
print("=" * 50)

# Ejemplo del enunciado
print("\n📝 Ejemplo del enunciado:")
print("-" * 40)
volteayelmimina("Hola mundo cruel", "o")

# Más ejemplos
print("\n📝 Más ejemplos:")
print("-" * 40)
volteayelmimina("Python es genial", "e")

print()
volteayelmimina("Anita lava la tina", "a")

print()
volteayelmimina("Programación", "n")

# Versión interactiva
print("\n📊 VERSIÓN INTERACTIVA:")
print("-" * 40)
texto = input("Introduce una frase: ")
car = input("Introduce el carácter a eliminar: ")
print()
volteayelmimina(texto, car)

# EXPLICACIÓN DEL SLICING [::-1]:
# --------------------------------------------------------
# | Sintaxis | Significado                              |
# |----------|------------------------------------------|
# | [::-1]   | Toda la cadena, al revés                 |
# | [2:5]    | Caracteres del índice 2 al 4             |
# | [:5]     | Primeros 5 caracteres                    |
# | [5:]     | Desde el índice 5 hasta el final         |
# | [::2]    | Cada 2 caracteres (saltando uno)         |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
