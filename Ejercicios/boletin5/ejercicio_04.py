# ============================================================================
# BOLETÍN 5 - EJERCICIO 4
# ============================================================================
# ENUNCIADO:
# Crea un programa que pida un número de mes (por ejemplo, el 4) y un año
# (por ejemplo 2022) y diga cuántos días tiene (por ejemplo, 30) y el
# nombre del mes. Hazlo usando listas. Recuerda que febrero tiene 29 días
# cuando el año es divisible por 4 y 28 el resto de los años
#
# CONCEPTOS CLAVE:
# - Listas para almacenar datos relacionados
# - Índices de lista (mes 1 = índice 0)
# - Año bisiesto: divisible por 4
# ============================================================================

print("=" * 50)
print("EJERCICIO 4: Días del mes usando listas")
print("=" * 50)

# Listas con los datos de los meses
# Índice 0 no se usa (para que mes 1 = índice 1)
nombres_meses = [
    "",           # Índice 0 (no usado)
    "Enero",      # 1
    "Febrero",    # 2
    "Marzo",      # 3
    "Abril",      # 4
    "Mayo",       # 5
    "Junio",      # 6
    "Julio",      # 7
    "Agosto",     # 8
    "Septiembre", # 9
    "Octubre",    # 10
    "Noviembre",  # 11
    "Diciembre"   # 12
]

dias_meses = [
    0,   # Índice 0 (no usado)
    31,  # Enero
    28,  # Febrero (por defecto, se ajusta si es bisiesto)
    31,  # Marzo
    30,  # Abril
    31,  # Mayo
    30,  # Junio
    31,  # Julio
    31,  # Agosto
    30,  # Septiembre
    31,  # Octubre
    30,  # Noviembre
    31   # Diciembre
]

# Pedir datos al usuario
mes = int(input("Introduce el número de mes (1-12): "))
anio = int(input("Introduce el año: "))

print("\n" + "-" * 40)

# Validar mes
if mes < 1 or mes > 12:
    print("✗ Mes no válido. Debe ser entre 1 y 12.")
else:
    # Obtener nombre del mes
    nombre_mes = nombres_meses[mes]
    
    # Obtener días del mes
    dias = dias_meses[mes]
    
    # Comprobar si es febrero y año bisiesto
    if mes == 2:
        if anio % 4 == 0:
            dias = 29
            print(f"📅 {nombre_mes} de {anio}")
            print(f"   Días: {dias}")
            print(f"   (Año bisiesto)")
        else:
            print(f"📅 {nombre_mes} de {anio}")
            print(f"   Días: {dias}")
    else:
        print(f"📅 {nombre_mes} de {anio}")
        print(f"   Días: {dias}")

print("-" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
