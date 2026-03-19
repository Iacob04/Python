# ============================================================================
# BOLETÍN 8 - EJERCICIO 6
# ============================================================================
# ENUNCIADO:
# Crear, por último, un programa que vuelva a usar el diccionario anterior
# de clientes y nos permita sumar un año a la edad de uno de ellos.
# El funcionamiento del programa sería así:
#   Introduce el nombre: Felipe
#   Introduce el apellido: Lotas
#   Felicidades en tu 77 cumpleaños Felipe. Edad actualizada en el diccionario
# Si no existe debería de informar de ello por consola.
#
# CONCEPTOS CLAVE:
# - Modificar valores en diccionario
# - Verificar existencia de clave
# - Incrementar valores
# ============================================================================

print("=" * 50)
print("EJERCICIO 6: Actualizar edad de cliente")
print("=" * 50)

# Diccionario de clientes
clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56,
    "Lotas, Felipe": 76  # Añadido para el ejemplo
}

print("\n👥 CLIENTES ACTUALES:")
print("-" * 40)
for cliente, edad in clientes.items():
    print(f"  {cliente}: {edad} años")

print("\n" + "=" * 40)
print("ACTUALIZAR EDAD (CUMPLEAÑOS)")
print("=" * 40)

# Pedir datos
nombre = input("Introduce el nombre: ")
apellido = input("Introduce el apellido: ")

# Crear la clave
clave = f"{apellido}, {nombre}"

print()

# Verificar si existe y actualizar
if clave in clientes:
    # Incrementar edad
    edad_anterior = clientes[clave]
    clientes[clave] = edad_anterior + 1
    
    print(f"🎂 Felicidades en tu {clientes[clave]} cumpleaños {nombre}.")
    print(f"   Edad actualizada en el diccionario")
else:
    print(f"{nombre} {apellido} no es cliente nuestro.")
    print(f"Feliz cumpleaños en cualquier caso!")

# Mostrar diccionario actualizado
print("\n" + "=" * 40)
print("CLIENTES ACTUALIZADOS:")
print("-" * 40)
for cliente, edad in sorted(clientes.items()):
    print(f"  {cliente}: {edad} años")

print("=" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
