# ============================================================================
# BOLETÍN 1 - EJERCICIO 5
# ============================================================================
# ENUNCIADO:
# Escribir un programa que pida un número al usuario y diga si es par o impar
#
# CONCEPTOS CLAVE:
# - input() + int() para obtener número del usuario
# - Condicional if-else para tomar decisiones
# - Operador % (módulo) para saber si es par o impar
# ============================================================================

print("=" * 50)
print("EJERCICIO 5: ¿Par o Impar?")
print("=" * 50)

# Paso 1: Pedir el número al usuario
numero = int(input("Introduce un número: "))

print("\n" + "-" * 40)

# Paso 2: Comprobar si es par o impar
# Un número es PAR si al dividirlo por 2 el resto es 0
# Un número es IMPAR si al dividirlo por 2 el resto es 1

if numero % 2 == 0:
    # Se ejecuta si la condición es VERDADERA
    print(f"✓ El número {numero} es PAR")
else:
    # Se ejecuta si la condición es FALSA
    print(f"✓ El número {numero} es IMPAR")

# EXPLICACIÓN DETALLADA:
# -------------------------------------------------
# | Número | numero % 2 | Resultado | ¿Par/Impar? |
# |--------|------------|-----------|-------------|
# |   4    |  4 % 2 = 0 |    0      |    PAR      |
# |   7    |  7 % 2 = 1 |    1      |   IMPAR     |
# |   10   | 10 % 2 = 0 |    0      |    PAR      |
# |   15   | 15 % 2 = 1 |    1      |   IMPAR     |
# -------------------------------------------------

# FORMA ALTERNATIVA (más compacta):
# resultado = "PAR" if numero % 2 == 0 else "IMPAR"
# print(f"El número {numero} es {resultado}")

print("-" * 40)
print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
