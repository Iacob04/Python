# ============================================================================
# BOLETÍN 7 - EJERCICIO 4
# ============================================================================
# ENUNCIADO:
# Haz una función en python que reciba un número y calcule si es capicúa o no.
#
# CONCEPTOS CLAVE:
# - Número capicúa: se lee igual de izquierda a derecha que de derecha a izquierda
# - Convertir número a string para manipularlo
# - Comparar string con su reverso
# ============================================================================

def es_capicua(numero):
    """
    Determina si un número es capicúa.
    
    Un número es capicúa si se lee igual de izquierda a derecha
    que de derecha a izquierda.
    
    Parámetros:
        numero (int): Número a comprobar
    
    Retorna:
        bool: True si es capicúa, False en caso contrario
    """
    # Convertir a string
    num_str = str(numero)
    
    # Comparar con su reverso
    # [::-1] invierte el string
    return num_str == num_str[::-1]


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 4: Número capicúa")
print("=" * 50)

# Ejemplos
print("\n📊 Ejemplos:")
print("-" * 40)

# Capicúas
capicua1 = 12321
capicua2 = 555
capicua3 = 7

# No capicúas
nocapicua1 = 12345
nocapicua2 = 100

print(f"¿{capicua1} es capicúa? {es_capicua(capicua1)}")
print(f"¿{capicua2} es capicúa? {es_capicua(capicua2)}")
print(f"¿{capicua3} es capicúa? {es_capicua(capicua3)}")
print(f"¿{nocapicua1} es capicúa? {es_capicua(nocapicua1)}")
print(f"¿{nocapicua2} es capicúa? {es_capicua(nocapicua2)}")

# Versión interactiva
print("\n📊 VERSIÓN INTERACTIVA:")
print("-" * 40)
num = int(input("Introduce un número: "))

if es_capicua(num):
    print(f"✓ {num} SÍ es capicúa")
else:
    print(f"✗ {num} NO es capicúa")

# EXPLICACIÓN:
# --------------------------------------------------------
# | Número | Como string | Reverso | ¿Capicúa? |
# |--------|-------------|---------|-----------|
# | 12321  | "12321"     | "12321" | SÍ        |
# | 12345  | "12345"     | "54321" | NO        |
# | 555    | "555"       | "555"   | SÍ        |
# | 100    | "100"       | "001"   | NO        |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
