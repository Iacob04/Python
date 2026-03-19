# ============================================================================
# BOLETÍN 2 - EJERCICIO 5
# ============================================================================
# ENUNCIADO:
# Modifica el ejercicio anterior para que cuando la media salga como
# aprobado pero el alumno tenga menos de un 4,5 en cualquiera de los
# apartados la nota resultante será un 4
#
# CONCEPTOS CLAVE:
# - Condiciones compuestas con and/or
# - Validación de requisitos mínimos
# - Reglas de negocio (lógica específica del problema)
# ============================================================================

print("=" * 50)
print("EJERCICIO 5: Media ponderada con requisitos mínimos")
print("=" * 50)

# Pesos de cada apartado
PESO_TRABAJO_CLASE = 0.10
PESO_PRACTICAS = 0.20
PESO_EXAMEN = 0.70

# Nota mínima requerida en cada apartado
NOTA_MINIMA = 4.5

# Pedir las notas
print("\nIntroduce las notas:")
nota_trabajo = float(input("  Trabajo en clase (10%): "))
nota_practicas = float(input("  Ejercicios prácticos (20%): "))
nota_examen = float(input("  Examen (70%): "))

print("\n" + "-" * 40)

# Calcular media ponderada
media = (
    nota_trabajo * PESO_TRABAJO_CLASE +
    nota_practicas * PESO_PRACTICAS +
    nota_examen * PESO_EXAMEN
)

print(f"Media calculada: {media:.2f}")

# Comprobar si cumple los requisitos mínimos
# El alumno debe tener al menos NOTA_MINIMA en TODOS los apartados

# FORMA 1: Usando and (más clara)
cumple_requisitos = (
    nota_trabajo >= NOTA_MINIMA and
    nota_practicas >= NOTA_MINIMA and
    nota_examen >= NOTA_MINIMA
)

# FORMA 2: Usando min() (más compacta)
# cumple_requisitos = min(nota_trabajo, nota_practicas, nota_examen) >= NOTA_MINIMA

print("-" * 40)
print("VERIFICACIÓN DE REQUISITOS MÍNIMOS:")
print(f"  Trabajo clase: {nota_trabajo} >= {NOTA_MINIMA}? {'✓' if nota_trabajo >= NOTA_MINIMA else '✗'}")
print(f"  Prácticas:     {nota_practicas} >= {NOTA_MINIMA}? {'✓' if nota_practicas >= NOTA_MINIMA else '✗'}")
print(f"  Examen:        {nota_examen} >= {NOTA_MINIMA}? {'✓' if nota_examen >= NOTA_MINIMA else '✗'}")

# Aplicar regla de la nota 4
if media >= 5 and not cumple_requisitos:
    print("-" * 40)
    print("⚠ La media es >= 5 pero no cumple requisitos mínimos")
    nota_final = 4.0
else:
    nota_final = media

print("=" * 40)
print(f"NOTA FINAL: {nota_final:.2f}")
print("=" * 40)

# EJEMPLOS:
# --------------------------------------------------------
# | Notas (T,P,E) | Media | Cumple min? | Nota final |
# |---------------|-------|-------------|------------|
# | 5, 5, 6       | 5.6   | SÍ          | 5.6        |
# | 3, 7, 8       | 6.9   | NO (T<4.5)  | 4.0        |
# | 5, 4, 7       | 6.1   | NO (P<4.5)  | 4.0        |
# | 4, 4, 4       | 4.0   | NO          | 4.0        |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
