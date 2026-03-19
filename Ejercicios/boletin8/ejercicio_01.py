# ============================================================================
# BOLETÍN 8 - EJERCICIO 1
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que guarde en un diccionario los precios
# de las frutas de la tabla. El diccionario no debe crearse interactivamente
# desde el teclado, sino que debe estar ya creado en el código.
# El programa debe preguntar al usuario por una fruta y un número de kilos
# y mostrar por pantalla el precio de ese número de kilos de fruta con dos
# decimales. El número de kilos debe admitir decimales. Si la fruta no está
# en el diccionario debe mostrar un mensaje informando de ello. Captura
# las posibles excepciones.
#
# Tabla de frutas:
#   Aguacate: 4.35 €/Kg
#   Mandarina: 2.60 €/Kg
#   Kiwi: 3.75 €/Kg
#   Naranja: 1.80 €/Kg
#
# CONCEPTOS CLAVE:
# - Diccionarios predefinidos
# - Acceso a valores con get() o []
# - Manejo de excepciones con try-except
# - Cálculo de precios
# ============================================================================

print("=" * 50)
print("EJERCICIO 1: Precios de frutas")
print("=" * 50)

# Diccionario con los precios (predefinido en el código)
precios_frutas = {
    "Aguacate": 4.35,
    "Mandarina": 2.60,
    "Kiwi": 3.75,
    "Naranja": 1.80
}

print("\n🍎 FRUTAS DISPONIBLES:")
print("-" * 40)
for fruta, precio in precios_frutas.items():
    print(f"  {fruta}: {precio:.2f} €/Kg")

print("-" * 40)

# Pedir datos al usuario
try:
    fruta_elegida = input("\n¿Qué fruta quieres comprar? ")
    
    # Verificar si la fruta existe (forma segura)
    if fruta_elegida not in precios_frutas:
        print(f"\nLo siento mucho pero no vendemos {fruta_elegida}")
    else:
        try:
            kilos = float(input("¿Cuántos kilos quieres? "))
            
            # Calcular precio total
            precio_kilo = precios_frutas[fruta_elegida]
            precio_total = kilos * precio_kilo
            
            print(f"\n{kilos} de {fruta_elegida} cuestan {precio_total:.2f} €")
            
        except ValueError:
            print("\nNo has introducido bien la cantidad que quieres")

except Exception as e:
    print(f"\nError inesperado: {e}")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
