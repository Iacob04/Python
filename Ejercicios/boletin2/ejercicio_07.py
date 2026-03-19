# ============================================================================
# BOLETÍN 2 - EJERCICIO 7
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que pida un número por teclado y nos
# imprima la tabla de multiplicar de dicho número del 1 al 10.
# Por ejemplo, si introducimos el 74 el resultado será:
# 74 x 1 = 74
# 74 x 2 = 148
# ...
# 74 x 10 = 740
#
# CONCEPTOS CLAVE:
# - Bucle for con range()
# - Operación de multiplicación
# - Formateo de strings para mostrar resultados
# ============================================================================

print("=" * 50)
print("EJERCICIO 7: Tabla de multiplicar")
print("=" * 50)

# Pedir el número
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

print("\n" + "=" * 40)
print(f"TABLA DE MULTIPLICAR DEL {numero}")
print("=" * 40)

# Generar tabla del 1 al 10
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    
    # Mostrar con formato alineado
    # :3d = número entero con 3 espacios (alineación)
    # :4d = número entero con 4 espacios
    print(f"  {numero:3d} x {multiplicador:2d} = {resultado:4d}")

print("=" * 40)

# EXPLICACIÓN DEL FORMATEO:
# --------------------------------------------------------
# | Código | Significado                    | Ejemplo    |
# |--------|--------------------------------|------------|
# | :3d    | Entero con ancho 3             | "  5"      |
# | :2d    | Entero con ancho 2             | " 7"       |
# | :4d    | Entero con ancho 4             | "  42"     |
# | :>10   | Alineado a la derecha (10)     | "       5" |
# --------------------------------------------------------

# VERSIÓN CON F-STRING AVANZADO:
print("\n--- Versión con formato más detallado ---")
for i in range(1, 11):
    print(f"{numero} × {i} = {numero * i}")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
