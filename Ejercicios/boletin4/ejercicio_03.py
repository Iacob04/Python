# ============================================================================
# BOLETÍN 4 - EJERCICIO 3
# ============================================================================
# ENUNCIADO:
# Escribir un programa que pida al usuario que escriba una cadena y la
# separe en dos distintas. En la primera de ellas estarían las letras que
# ocupan una posición par y en la segunda las que ocupan una posición impar.
# Por ejemplo, si el usuario escribe Hola Mundo:
# - Primera cadena (posiciones pares): Hl ud
# - Segunda cadena (posiciones impares): oaMno
#
# CONCEPTOS CLAVE:
# - Índices de strings (empiezan en 0)
# - Slicing con paso [::2] para pares
# - Slicing con paso [1::2] para impares
# ============================================================================

print("=" * 50)
print("EJERCICIO 3: Separar cadena en posiciones par/impar")
print("=" * 50)

# Pedir cadena
cadena = input("Introduce una cadena de texto: ")

print("\n" + "-" * 40)

# Posiciones PARES (índices 0, 2, 4, 6...)
# [::2] = desde inicio hasta fin, paso 2
pares = cadena[::2]

# Posiciones IMPARES (índices 1, 3, 5, 7...)
# [1::2] = desde índice 1 hasta fin, paso 2
impares = cadena[1::2]

print(f"Cadena original: '{cadena}'")
print(f"\nPosiciones PARES (0, 2, 4...): '{pares}'")
print(f"Posiciones IMPARES (1, 3, 5...): '{impares}'")

print("-" * 40)

# EXPLICACIÓN VISUAL:
# --------------------------------------------------------
# | Cadena:    H  o  l  a     M  u  n  d  o             |
# | Índice:    0  1  2  3  4  5  6  7  8  9             |
# | Par/Impar: P  I  P  I  P  I  P  I  P  I             |
# |                                                      |
# | Pares:     H  l     M  n  o  →  "Hl Mno"            |
# | Impares:   o  a     u  d     →  "oa ud"             |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
