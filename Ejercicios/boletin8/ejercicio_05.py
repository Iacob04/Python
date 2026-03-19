# ============================================================================
# BOLETÍN 8 - EJERCICIO 5
# ============================================================================
# ENUNCIADO:
# Escribe ahora un programa que dado el diccionario del ejemplo anterior
# sirva para añadir nombres al diccionario. El funcionamiento del programa
# sería así:
#   Introduce el nombre: Felipe
#   Introduce el apellido: Lotas
#   Introduce la edad: 76
#   Felipe Lotas. 76 años. Cliente agregado.
# Si este cliente ya existe debería de mostrar un mensaje advirtiéndolo.
#
# CONCEPTOS CLAVE:
# - Añadir elementos a diccionario
# - Verificar si una clave existe
# - Formateo de clave "Apellido, Nombre"
# ============================================================================

print("=" * 50)
print("EJERCICIO 5: Añadir clientes al diccionario")
print("=" * 50)

# Diccionario de clientes
clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}

print("\n👥 CLIENTES ACTUALES:")
print("-" * 40)
for cliente, edad in clientes.items():
    print(f"  {cliente}: {edad} años")

print("\n" + "=" * 40)
print("AÑADIR NUEVO CLIENTE")
print("=" * 40)

# Pedir datos
nombre = input("Introduce el nombre: ")
apellido = input("Introduce el apellido: ")
edad = int(input("Introduce la edad: "))

# Crear la clave en formato "Apellido, Nombre"
clave = f"{apellido}, {nombre}"

print()

# Verificar si ya existe
if clave in clientes:
    print(f"{nombre} {apellido} ya está en el diccionario de clientes")
else:
    # Añadir al diccionario
    clientes[clave] = edad
    print(f"{nombre} {apellido}. {edad} años. Cliente agregado.")

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
