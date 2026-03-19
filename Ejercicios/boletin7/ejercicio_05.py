# ============================================================================
# BOLETÍN 7 - EJERCICIO 5
# ============================================================================
# ENUNCIADO:
# Haz una función en python que reciba dos fechas en formato "DD/MM/YYYY"
# y compruebe si ambas son correctas y en caso afirmativo cual de ambas
# es mas antigua. Contempla los meses que tienen 30 y/o 31 días, los años
# bisiestos, etc.
#
# CONCEPTOS CLAVE:
# - Validación de fechas
# - Año bisiesto: divisible por 4
# - Meses con 30/31 días
# - Comparación de fechas
# ============================================================================

def es_bisiesto(anio):
    """Comprueba si un año es bisiesto."""
    return anio % 4 == 0


def dias_del_mes(mes, anio):
    """Devuelve los días de un mes, considerando bisiestos."""
    if mes in [1, 3, 5, 7, 8, 10, 12]:  # Meses con 31 días
        return 31
    elif mes in [4, 6, 9, 11]:  # Meses con 30 días
        return 30
    elif mes == 2:  # Febrero
        return 29 if es_bisiesto(anio) else 28
    else:
        return 0  # Mes inválido


def fecha_valida(dia, mes, anio):
    """Comprueba si una fecha es válida."""
    # Validar mes
    if mes < 1 or mes > 12:
        return False
    
    # Validar día
    max_dias = dias_del_mes(mes, anio)
    if dia < 1 or dia > max_dias:
        return False
    
    return True


def comparar_fechas(fecha1, fecha2):
    """
    Compara dos fechas en formato DD/MM/YYYY.
    
    Parámetros:
        fecha1, fecha2 (str): Fechas en formato "DD/MM/YYYY"
    """
    try:
        # Dividir las fechas
        partes1 = fecha1.split("/")
        partes2 = fecha2.split("/")
        
        # Extraer componentes
        dia1, mes1, anio1 = int(partes1[0]), int(partes1[1]), int(partes1[2])
        dia2, mes2, anio2 = int(partes2[0]), int(partes2[1]), int(partes2[2])
        
        # Validar fechas
        if not fecha_valida(dia1, mes1, anio1):
            print(f"✗ La fecha '{fecha1}' no es válida")
            return
        
        if not fecha_valida(dia2, mes2, anio2):
            print(f"✗ La fecha '{fecha2}' no es válida")
            return
        
        # Ambas fechas son válidas, comparar
        print(f"✓ Ambas fechas son válidas")
        
        # Comparar por año, mes, día
        if anio1 < anio2:
            print(f"  '{fecha1}' es más antigua que '{fecha2}'")
        elif anio1 > anio2:
            print(f"  '{fecha2}' es más antigua que '{fecha1}'")
        else:  # Mismo año
            if mes1 < mes2:
                print(f"  '{fecha1}' es más antigua que '{fecha2}'")
            elif mes1 > mes2:
                print(f"  '{fecha2}' es más antigua que '{fecha1}'")
            else:  # Mismo mes
                if dia1 < dia2:
                    print(f"  '{fecha1}' es más antigua que '{fecha2}'")
                elif dia1 > dia2:
                    print(f"  '{fecha2}' es más antigua que '{fecha1}'")
                else:
                    print(f"  Ambas fechas son iguales")
    
    except (ValueError, IndexError):
        print("✗ Formato incorrecto. Usa DD/MM/YYYY")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 5: Comparación de fechas")
print("=" * 50)

# Ejemplos
print("\n📊 Ejemplos:")
print("-" * 40)

print("\n1. Fechas válidas:")
comparar_fechas("15/03/2023", "20/05/2022")

print("\n2. Misma fecha:")
comparar_fechas("10/10/2023", "10/10/2023")

print("\n3. Fecha inválida:")
comparar_fechas("31/02/2023", "15/03/2023")

print("\n4. Año bisiesto:")
comparar_fechas("29/02/2024", "28/02/2024")

# Versión interactiva
print("\n📊 VERSIÓN INTERACTIVA:")
print("-" * 40)
f1 = input("Primera fecha (DD/MM/YYYY): ")
f2 = input("Segunda fecha (DD/MM/YYYY): ")
print()
comparar_fechas(f1, f2)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
