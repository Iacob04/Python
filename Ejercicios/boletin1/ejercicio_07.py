# ============================================================================
# BOLETÍN 1 - EJERCICIO 7
# ============================================================================
# ENUNCIADO:
# Escribir un programa que pida un número al usuario que simule ser
# el precio de un artículo y escriba el resultado de aplicarle el IVA del 21%
#
# CONCEPTOS CLAVE:
# - Cálculo de porcentajes
# - IVA = precio × (porcentaje / 100)
# - Precio final = precio + IVA
# - Formateo de decimales con :.2f
# ============================================================================

print("=" * 50)
print("EJERCICIO 7: Cálculo de IVA (21%)")
print("=" * 50)

# Constantes (valores que no cambian)
PORCENTAJE_IVA = 21  # 21%

# Paso 1: Pedir el precio al usuario
# Usamos float() porque el precio puede tener decimales
precio = float(input("Introduce el precio del artículo (€): "))

print("\n" + "-" * 40)
print("TICKET DE COMPRA")
print("-" * 40)

# Paso 2: Calcular el IVA
# Fórmula: IVA = precio × (21 / 100) = precio × 0.21
iva = precio * (PORCENTAJE_IVA / 100)

# Paso 3: Calcular el precio final
precio_final = precio + iva

# Paso 4: Mostrar resultados formateados
# :.2f muestra el número con 2 decimales
print(f"Precio sin IVA:    {precio:>10.2f} €")
print(f"IVA ({PORCENTAJE_IVA}%):       {iva:>10.2f} €")
print("-" * 40)
print(f"PRECIO FINAL:      {precio_final:>10.2f} €")

# EXPLICACIÓN DEL CÁLCULO:
# Si el precio es 100€:
#   IVA = 100 × 0.21 = 21€
#   Precio final = 100 + 21 = 121€
#
# FÓRMULA DIRECTA (sin paso intermedio):
#   precio_final = precio × 1.21

# Versión alternativa más corta:
# precio_final = precio * 1.21
# print(f"El precio con IVA es: {precio_final:.2f} €")

print("-" * 40)
print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
