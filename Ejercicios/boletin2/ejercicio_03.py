# ============================================================================
# BOLETÍN 2 - EJERCICIO 3
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que nos pida las notas de los dos
# trimestres y nos muestre la media aritmética resultante
#
# CONCEPTOS CLAVE:
# - Media aritmética = (suma de valores) / (número de valores)
# - float() para notas con decimales
# - Formateo de decimales
# ============================================================================

print("=" * 50)
print("EJERCICIO 3: Media aritmética de dos trimestres")
print("=" * 50)

# Pedir las notas de los dos trimestres
# Usamos float porque las notas pueden tener decimales
nota1 = float(input("Nota del primer trimestre: "))
nota2 = float(input("Nota del segundo trimestre: "))

print("\n" + "-" * 40)

# Calcular la media aritmética
# Fórmula: media = (nota1 + nota2) / 2
media = (nota1 + nota2) / 2

# Mostrar resultado
print("CALCULO DE LA MEDIA")
print(f"  Nota 1º trimestre: {nota1}")
print(f"  Nota 2º trimestre: {nota2}")
print("-" * 40)
print(f"  MEDIA: {media:.2f}")

# EXPLICACIÓN DE LA MEDIA ARITMÉTICA:
# --------------------------------------------------------
# | Nota 1 | Nota 2 | Cálculo         | Media  |
# |--------|--------|-----------------|--------|
# | 7.5    | 8.0    | (7.5+8.0)/2     | 7.75   |
# | 5.0    | 7.0    | (5.0+7.0)/2     | 6.00   |
# | 10.0   | 4.0    | (10.0+4.0)/2    | 7.00   |
# --------------------------------------------------------

# Verificar si está aprobado
print("-" * 40)
if media >= 5:
    print("✓ ¡APROBADO!")
else:
    print("✗ SUSPENSO - Necesitas recuperar")

print("-" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
