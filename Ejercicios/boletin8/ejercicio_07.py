# ============================================================================
# BOLETÍN 8 - EJERCICIO 7
# ============================================================================
# ENUNCIADO:
# La agencia de espionaje donde trabajas ha desarrollado un nuevo sistema
# de cifrado de sustitución que funciona de la siguiente forma:
# - Asignamos a cada letra del alfabeto un número de dos cifras elegido
#   de forma aleatoria entre el 10 y el 99. Dos letras no pueden tener
#   el mismo número.
# - Cogemos el mensaje, suprimimos los espacios, lo pasamos todo a
#   mayúsculas y sustituimos cada carácter por su cifra asociada.
# - Por último presentamos el mensaje final separando las cifras de tres
#   en tres. Si hace falta completamos con números aleatorios lo que reste.
#
# Realiza una función que realice este cifrado.
#
# CONCEPTOS CLAVE:
# - Diccionario para mapeo letra→número
# - Generación de clave aleatoria
# - Procesamiento de strings
# - Formateo de salida
# ============================================================================

import random
import string


def generar_clave_cifrado():
    """
    Genera un diccionario con la asignación letra→número para el cifrado.
    Cada letra tiene un número único entre 10 y 99.
    """
    clave = {}
    # Generar números del 10 al 99 y mezclarlos
    numeros = list(range(10, 100))
    random.shuffle(numeros)
    
    # Asignar a cada letra del alfabeto
    alfabeto = string.ascii_uppercase + "Ñ"
    for i, letra in enumerate(alfabeto):
        if i < len(numeros):
            clave[letra] = numeros[i]
    
    return clave


def cifrar_mensaje(mensaje, clave):
    """
    Cifra un mensaje usando la clave de sustitución.
    
    Parámetros:
        mensaje (str): Mensaje a cifrar
        clave (dict): Diccionario con letra→número
    
    Retorna:
        str: Mensaje cifrado
    """
    # Procesar mensaje: quitar espacios y pasar a mayúsculas
    mensaje_limpio = mensaje.replace(" ", "").upper()
    
    # Sustituir cada letra por su número
    mensaje_cifrado = ""
    for letra in mensaje_limpio:
        if letra in clave:
            mensaje_cifrado += str(clave[letra])
    
    # Separar de tres en tres
    grupos = []
    for i in range(0, len(mensaje_cifrado), 3):
        grupo = mensaje_cifrado[i:i+3]
        # Completar con números aleatorios si es necesario
        while len(grupo) < 3:
            grupo += str(random.randint(0, 9))
        grupos.append(grupo)
    
    return " ".join(grupos)


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 7: Sistema de cifrado")
print("=" * 50)

# Generar clave de cifrado
clave = generar_clave_cifrado()

print("\n🔐 CLAVE DE CIFRADO GENERADA:")
print("-" * 40)
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
for letra in alfabeto:
    if letra in clave:
        print(f"  {letra} → {clave[letra]}", end="  ")
        if (alfabeto.index(letra) + 1) % 5 == 0:
            print()

print("\n" + "=" * 40)

# Ejemplo del enunciado
mensaje = "Dos Abril"
print(f"\n📝 Mensaje original: '{mensaje}'")

# Proceso paso a paso
mensaje_limpio = mensaje.replace(" ", "").upper()
print(f"   Sin espacios y mayúsculas: '{mensaje_limpio}'")

# Cifrar
mensaje_cifrado = cifrar_mensaje(mensaje, clave)
print(f"\n🔒 Mensaje cifrado: {mensaje_cifrado}")

# Versión interactiva
print("\n" + "=" * 40)
mensaje_usuario = input("\nIntroduce un mensaje para cifrar: ")
resultado = cifrar_mensaje(mensaje_usuario, clave)
print(f"\n🔒 Resultado: {resultado}")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
