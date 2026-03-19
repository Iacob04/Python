# ============================================================================
# BOLETÍN 4 - EJERCICIO 10
# ============================================================================
# ENUNCIADO:
# Haz un programa en Python que te calcule la letra del NIF.
# La forma de hacerlo es la siguiente:
# 1. Se divide el número entre 23
# 2. El resto de esa división indica la letra según esta tabla:
#    0=T, 1=R, 2=W, 3=A, 4=G, 5=M, 6=Y, 7=F, 8=P, 9=D, 10=X, 11=B,
#    12=N, 13=J, 14=Z, 15=S, 16=Q, 17=V, 18=H, 19=L, 20=C, 21=K, 22=E
#
# NOTA: cuando aprendamos a manejarnos con colecciones y listas será
# mucho más fácil hacer esto. Por el momento puedes hacerlo con un
# match enooooorme!
#
# CONCEPTOS CLAVE:
# - Operador módulo % para obtener resto
# - match-case con muchos casos
# - Cálculo de letra NIF
# ============================================================================

print("=" * 50)
print("EJERCICIO 10: Cálculo de letra del NIF")
print("=" * 50)

# Pedir número del NIF (sin letra)
numero = input("Introduce los 8 dígitos del NIF: ")

# Validar que son 8 dígitos
if len(numero) != 8 or not numero.isdigit():
    print("✗ Error: Debes introducir exactamente 8 números")
else:
    # Calcular el resto de dividir entre 23
    resto = int(numero) % 23
    
    print("\n" + "-" * 40)
    print(f"Número introducido: {numero}")
    print(f"Resto de {numero} ÷ 23 = {resto}")
    
    # Determinar la letra según el resto
    match resto:
        case 0: letra = "T"
        case 1: letra = "R"
        case 2: letra = "W"
        case 3: letra = "A"
        case 4: letra = "G"
        case 5: letra = "M"
        case 6: letra = "Y"
        case 7: letra = "F"
        case 8: letra = "P"
        case 9: letra = "D"
        case 10: letra = "X"
        case 11: letra = "B"
        case 12: letra = "N"
        case 13: letra = "J"
        case 14: letra = "Z"
        case 15: letra = "S"
        case 16: letra = "Q"
        case 17: letra = "V"
        case 18: letra = "H"
        case 19: letra = "L"
        case 20: letra = "C"
        case 21: letra = "K"
        case 22: letra = "E"
        case _: letra = "?"
    
    print(f"Letra correspondiente: {letra}")
    print("=" * 40)
    print(f"✓ Tu NIF completo es: {numero}{letra}")
    print("=" * 40)

# FORMA ALTERNATIVA (con lista - más eficiente):
print("\n--- Forma alternativa (con lista) ---")

letras_nif = [
    "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
    "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"
]

# La letra es letras_nif[resto]
print(f"Con lista: La letra sería {letras_nif[int(numero) % 23]}")

# TABLA DE LETRAS:
# --------------------------------------------------------
# | Resto | Letra | Resto | Letra | Resto | Letra |
# |-------|-------|-------|-------|-------|-------|
# |   0   |   T   |   8   |   P   |  16   |   Q   |
# |   1   |   R   |   9   |   D   |  17   |   V   |
# |   2   |   W   |  10   |   X   |  18   |   H   |
# |   3   |   A   |  11   |   B   |  19   |   L   |
# |   4   |   G   |  12   |   N   |  20   |   C   |
# |   5   |   M   |  13   |   J   |  21   |   K   |
# |   6   |   Y   |  14   |   Z   |  22   |   E   |
# |   7   |   F   |  15   |   S   |       |       |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
