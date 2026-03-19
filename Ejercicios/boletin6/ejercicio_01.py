# ============================================================================
# BOLETÍN 6 - EJERCICIO 1
# ============================================================================
# ENUNCIADO:
# Escribir una función en python que reciba dos argumentos: el precio y
# el iva y nos calcule y devuelva el pvp una vez aplicado el iva con dos
# decimales
#
# EJEMPLOS DE EJECUCIÓN:
#   print(pvp(14, 0))     → 14
#   print(pvp(34.4, 21))  → 41.62
#
# CONCEPTOS CLAVE:
# - Definición de funciones con def
# - Parámetros y return
# - Cálculo de porcentajes
# - round() para redondear decimales
# ============================================================================

# Definición de la función
def pvp(precio, iva):
    """
    Calcula el PVP aplicando el IVA a un precio.
    
    Parámetros:
        precio (float): Precio sin IVA
        iva (float): Porcentaje de IVA (ej: 21 para 21%)
    
    Retorna:
        float: Precio con IVA aplicado, redondeado a 2 decimales
    """
    # Calcular el precio con IVA
    # Fórmula: precio + (precio * iva / 100)
    # O equivalente: precio * (1 + iva/100)
    
    precio_con_iva = precio * (1 + iva / 100)
    
    # Redondear a 2 decimales
    return round(precio_con_iva, 2)


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 1: Función para calcular PVP con IVA")
print("=" * 50)

# Ejemplos del enunciado
print("\n📊 EJEMPLOS DEL ENUNCIADO:")
print("-" * 40)

resultado1 = pvp(14, 0)
print(f"pvp(14, 0)    = {resultado1}")

resultado2 = pvp(34.4, 21)
print(f"pvp(34.4, 21) = {resultado2}")

# Más ejemplos
print("\n📊 MÁS EJEMPLOS:")
print("-" * 40)
print(f"pvp(100, 21)  = {pvp(100, 21)}")
print(f"pvp(50.5, 10) = {pvp(50.5, 10)}")
print(f"pvp(25, 4)    = {pvp(25, 4)}")

# Versión interactiva
print("\n📊 CÁLCULO INTERACTIVO:")
print("-" * 40)
precio_usuario = float(input("Introduce el precio: "))
iva_usuario = float(input("Introduce el % de IVA: "))

resultado = pvp(precio_usuario, iva_usuario)
print(f"\nPVP: {resultado} €")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
