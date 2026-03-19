# ============================================================================
# BOLETÍN 8 - EJERCICIO 8
# ============================================================================
# ENUNCIADO:
# Haz ahora la función que realiza el descifrado del mensaje.
# - Piensa que si has tenido que introducir caracteres aleatorios puede
#   que aparezca alguna letra sin sentido.
# - También puede que al final del mensaje quede un excedente de una
#   única cifra. En ese caso se desecha.
#
# CONCEPTOS CLAVE:
# - Invertir diccionario (número→letra)
# - Procesar mensaje cifrado
# - Manejo de caracteres inválidos
# ============================================================================

import random
import string


def generar_clave_cifrado():
    """Genera un diccionario con la asignación letra→número."""
    clave = {}
    numeros = list(range(10, 100))
    random.shuffle(numeros)
    
    alfabeto = string.ascii_uppercase + "Ñ"
    for i, letra in enumerate(alfabeto):
        if i < len(numeros):
            clave[letra] = numeros[i]
    
    return clave


def cifrar_mensaje(mensaje, clave):
    """Cifra un mensaje usando la clave de sustitución."""
    mensaje_limpio = mensaje.replace(" ", "").upper()
    
    mensaje_cifrado = ""
    for letra in mensaje_limpio:
        if letra in clave:
            mensaje_cifrado += str(clave[letra])
    
    grupos = []
    for i in range(0, len(mensaje_cifrado), 3):
        grupo = mensaje_cifrado[i:i+3]
        while len(grupo) < 3:
            grupo += str(random.randint(0, 9))
        grupos.append(grupo)
    
    return " ".join(grupos)


def descifrar_mensaje(mensaje_cifrado, clave):
    """
    Descifra un mensaje usando la clave de sustitución.
    
    Parámetros:
        mensaje_cifrado (str): Mensaje en formato "XXX XXX XXX"
        clave (dict): Diccionario con letra→número (se invertirá)
    
    Retorna:
        str: Mensaje descifrado
    """
    # Invertir la clave (número→letra)
    clave_invertida = {str(v): k for k, v in clave.items()}
    
    # Quitar espacios del mensaje cifrado
    numeros = mensaje_cifrado.replace(" ", "")
    
    # Descifrar de dos en dos (cada número es de 2 cifras)
    mensaje_descifrado = ""
    
    for i in range(0, len(numeros) - 1, 2):  # -1 para evitar índice fuera de rango
        par = numeros[i:i+2]
        
        if par in clave_invertida:
            mensaje_descifrado += clave_invertida[par]
        else:
            # Carácter sin sentido (aleatorio añadido)
            mensaje_descifrado += "?"
    
    return mensaje_descifrado


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 8: Descifrado de mensajes")
print("=" * 50)

# Generar clave
clave = generar_clave_cifrado()

# Ejemplo: cifrar y descifrar
mensaje_original = "AMOR"
print(f"\n📝 Mensaje original: '{mensaje_original}'")

# Cifrar
mensaje_cifrado = cifrar_mensaje(mensaje_original, clave)
print(f"🔒 Mensaje cifrado: {mensaje_cifrado}")

# Descifrar
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave)
print(f"🔓 Mensaje descifrado: '{mensaje_descifrado}'")

print("\n" + "-" * 40)

# Ejemplo más largo
mensaje2 = "DOS ABRIL"
print(f"\n📝 Mensaje original: '{mensaje2}'")
mensaje_cifrado2 = cifrar_mensaje(mensaje2, clave)
print(f"🔒 Mensaje cifrado: {mensaje_cifrado2}")
mensaje_descifrado2 = descifrar_mensaje(mensaje_cifrado2, clave)
print(f"🔓 Mensaje descifrado: '{mensaje_descifrado2}'")

# Nota: pueden aparecer "?" por los números aleatorios añadidos

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
