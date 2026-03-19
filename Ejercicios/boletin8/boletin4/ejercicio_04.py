# ============================================================================
# BOLETÍN 4 - EJERCICIO 4
# ============================================================================
# ENUNCIADO:
# Escribir un programa que pida al usuario una cadena de texto y la escriba
# con el alfabeto típico de los hackers sustituyendo:
# - a → 4
# - e → 3
# - i → 1
# - o → 0
# Considera que las vocales pueden estar en mayúsculas o minúsculas.
# PISTA: se hace más fácilmente con un switch (match-case en Python 3.10+)
#
# CONCEPTOS CLAVE:
# - match-case (switch en Python)
# - Recorrer caracteres de una cadena
# - Construir nueva cadena
# ============================================================================

print("=" * 50)
print("EJERCICIO 4: Alfabeto hacker (leet speak)")
print("=" * 50)

# Pedir cadena
cadena = input("Introduce una cadena de texto: ")

print("\n" + "-" * 40)

# Convertir a alfabeto hacker
resultado = ""

for caracter in cadena:
    # match-case (switch de Python 3.10+)
    match caracter.lower():  # .lower() para manejar mayúsculas y minúsculas
        case "a":
            resultado += "4"
        case "e":
            resultado += "3"
        case "i":
            resultado += "1"
        case "o":
            resultado += "0"
        case _:
            # El guión bajo (_) es el "default" del switch
            resultado += caracter

print(f"Cadena original: '{cadena}'")
print(f"Cadena hacker: '{resultado}'")

print("-" * 40)

# FORMA ALTERNATIVA (sin match-case, compatible con versiones antiguas):
print("\n--- Forma alternativa (con diccionario) ---")

traduccion = {"a": "4", "e": "3", "i": "1", "o": "0",
              "A": "4", "E": "3", "I": "1", "O": "0"}

resultado2 = ""
for caracter in cadena:
    resultado2 += traduccion.get(caracter, caracter)

print(f"Resultado: '{resultado2}'")

# TABLA DE CONVERSIÓN:
# --------------------------------------------------------
# | Letra | Sustitución | Ejemplo                    |
# |-------|-------------|----------------------------|
# | a, A  | 4           | "Hola" → "H0l4"            |
# | e, E  | 3           | "Mundo" → "Mund0"          |
# | i, I  | 1           | "Python" → "Pyth0n"        |
# | o, O  | 0           | "Hola Mundo" → "H0l4 Mund0"|
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
