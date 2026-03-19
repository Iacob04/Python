# ============================================================================
# BOLETÍN 2 - EJERCICIO 4
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que nos pida las notas obtenidas en un
# trimestre y nos muestre la media ponderada sabiendo que:
# - La primera nota corresponde al trabajo en clase y cuenta como un 10%
# - La segunda corresponde a los ejercicios prácticos: 20%
# - La tercera la nota del examen: 70%
#
# CONCEPTOS CLAVE:
# - Media ponderada: cada valor tiene un "peso" diferente
# - Fórmula: (nota1×peso1 + nota2×peso2 + nota3×peso3) / (peso1+peso2+peso3)
# - Los pesos deben sumar 100 (o 1.0 si usamos decimales)
# ============================================================================

print("=" * 50)
print("EJERCICIO 4: Media ponderada")
print("=" * 50)

# Definir los pesos como constantes (mejor práctica)
PESO_TRABAJO_CLASE = 0.10    # 10%
PESO_PRACTICAS = 0.20        # 20%
PESO_EXAMEN = 0.70           # 70%

# Verificación: los pesos deben sumar 1.0 (100%)
# 0.10 + 0.20 + 0.70 = 1.00 ✓

# Pedir las tres notas
print("\nIntroduce las notas:")
nota_trabajo = float(input("  Trabajo en clase (10%): "))
nota_practicas = float(input("  Ejercicios prácticos (20%): "))
nota_examen = float(input("  Examen (70%): "))

print("\n" + "-" * 40)

# Calcular la media ponderada
# Fórmula: suma de (nota × peso)
media_ponderada = (
    nota_trabajo * PESO_TRABAJO_CLASE +
    nota_practicas * PESO_PRACTICAS +
    nota_examen * PESO_EXAMEN
)

# Mostrar desglose del cálculo
print("DESGLOSE DEL CÁLCULO:")
print(f"  Trabajo clase:  {nota_trabajo} × {PESO_TRABAJO_CLASE*100:.0f}% = {nota_trabajo * PESO_TRABAJO_CLASE:.2f}")
print(f"  Prácticas:      {nota_practicas} × {PESO_PRACTICAS*100:.0f}% = {nota_practicas * PESO_PRACTICAS:.2f}")
print(f"  Examen:         {nota_examen} × {PESO_EXAMEN*100:.0f}% = {nota_examen * PESO_EXAMEN:.2f}")
print("-" * 40)
print(f"  MEDIA PONDERADA: {media_ponderada:.2f}")

# EXPLICACIÓN MEDIA PONDERADA vs ARITMÉTICA:
# --------------------------------------------------------
# | Tipo        | Fórmula                    | Uso              |
# |-------------|----------------------------|------------------|
# | Aritmética  | (a+b+c)/3                  | Todo igual       |
# | Ponderada   | (a×p1+b×p2+c×p3)/(p1+p2+p3)| Importancia dif. |
# --------------------------------------------------------
#
# En este caso, el examen vale 7 veces más que el trabajo en clase!

print("-" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
