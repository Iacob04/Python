# ============================================================================
# BOLETÍN 6 - EJERCICIO 4
# ============================================================================
# ENUNCIADO:
# Escribir una función en python que reciba una cadena de texto que
# representa una fracción y nos devuelva su valor en decimal. La fracción
# tiene que ser introducida con el formato: numerador/denominador, siendo
# numerador y denominador dos números enteros. Si introducimos algo que
# no corresponda con esto debería de devolver un cero.
#
# EJEMPLOS DE EJECUCIÓN:
#   print(fraccion("25/10"))   → 2.5
#   print(fraccion("a/10"))    → 0
#   print(fraccion("//10"))    → 0
#   print(fraccion("10"))      → 0
#
# CONCEPTOS CLAVE:
# - split() para dividir strings
# - try-except para manejar errores
# - Validación de formato
# - División de enteros
# ============================================================================

# Definición de la función
def fraccion(cadena):
    """
    Convierte una fracción en formato "numerador/denominador" a decimal.
    
    Parámetros:
        cadena (str): Fracción en formato "a/b"
    
    Retorna:
        float: Valor decimal de la fracción, o 0 si el formato es inválido
    """
    try:
        # Dividir la cadena por el carácter "/"
        partes = cadena.split("/")
        
        # Debe haber exactamente 2 partes (numerador y denominador)
        if len(partes) != 2:
            return 0
        
        # Convertir a enteros
        numerador = int(partes[0])
        denominador = int(partes[1])
        
        # El denominador no puede ser cero
        if denominador == 0:
            return 0
        
        # Calcular y devolver el valor decimal
        return numerador / denominador
        
    except (ValueError, IndexError):
        # ValueError: si no se pueden convertir a enteros
        # IndexError: si hay problemas con los índices
        return 0


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 4: Conversor de fracciones a decimal")
print("=" * 50)

# Ejemplos del enunciado
print("\n📊 EJEMPLOS DEL ENUNCIADO:")
print("-" * 40)

print(f'fraccion("25/10")  = {fraccion("25/10")}')
print(f'fraccion("a/10")   = {fraccion("a/10")}')
print(f'fraccion("//10")   = {fraccion("//10")}')
print(f'fraccion("10")     = {fraccion("10")}')

# Más ejemplos
print("\n📊 MÁS EJEMPLOS:")
print("-" * 40)
print(f'fraccion("1/2")    = {fraccion("1/2")}')
print(f'fraccion("3/4")    = {fraccion("3/4")}')
print(f'fraccion("7/0")    = {fraccion("7/0")}  (división por cero)')
print(f'fraccion("abc")    = {fraccion("abc")}')

# Versión interactiva
print("\n📊 VERSIÓN INTERACTIVA:")
print("-" * 40)
entrada = input('Introduce una fracción (formato "a/b"): ')
resultado = fraccion(entrada)
print(f"Resultado: {resultado}")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
