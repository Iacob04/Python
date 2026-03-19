# ============================================================================
# BOLETÍN 4 - EJERCICIO 2
# ============================================================================
# ENUNCIADO:
# Escribir un programa que pida al usuario que escriba una cadena de texto
# y la imprima escrita al revés (es decir, si el usuario escribe Hola Mundo
# el programa debería de escribir odnuM aloH)
#
# CONCEPTOS CLAVE:
# - Slicing con paso negativo [::-1]
# - Invertir strings en Python
# ============================================================================

print("=" * 50)
print("EJERCICIO 2: Invertir una cadena")
print("=" * 50)

# Pedir cadena
cadena = input("Introduce una cadena de texto: ")

print("\n" + "-" * 40)

# Invertir usando slicing [::-1]
# [inicio:fin:paso] - ::-1 significa: todo, al revés
cadena_invertida = cadena[::-1]

print(f"Cadena original: '{cadena}'")
print(f"Cadena invertida: '{cadena_invertida}'")

print("-" * 40)

# EXPLICACIÓN DEL SLICING:
# --------------------------------------------------------
# | Sintaxis    | Significado                          | Resultado        |
# |-------------|--------------------------------------|------------------|
# | [::-1]      | Toda la cadena, paso -1 (al revés)   | "abc" → "cba"    |
# | [::2]       | Toda la cadena, paso 2 (cada 2)      | "abcdef" → "ace" |
# | [2:5]       | Desde índice 2 hasta 4               | "abcdef" → "cde" |
# | [:3]        | Desde inicio hasta índice 2          | "abcdef" → "abc" |
# | [3:]        | Desde índice 3 hasta final           | "abcdef" → "def" |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
