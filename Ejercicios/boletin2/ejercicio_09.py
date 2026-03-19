# ============================================================================
# BOLETÍN 2 - EJERCICIO 9
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que nos pida nuestro nombre y apellidos
# (dos peticiones hechas en ese orden) y nos lo escriba formateado de la
# siguiente forma:
# Morales Vázquez, José María
#
# CONCEPTOS CLAVE:
# - Concatenación de strings
# - Formato "Apellidos, Nombre" (formato español)
# - Uso de f-strings para formateo
# ============================================================================

print("=" * 50)
print("EJERCICIO 9: Formateo de nombre y apellidos")
print("=" * 50)

# Pedir datos al usuario
# El orden es importante: primero nombre, luego apellidos
nombre = input("Introduce tu nombre: ")
apellidos = input("Introduce tus apellidos: ")

print("\n" + "-" * 40)

# FORMA 1: Concatenación con +
print("--- Forma 1: Concatenación con + ---")
formateado1 = apellidos + ", " + nombre
print(formateado1)

# FORMA 2: Usando f-string (recomendada)
print("\n--- Forma 2: f-string (recomendada) ---")
formateado2 = f"{apellidos}, {nombre}"
print(formateado2)

# FORMA 3: Usando format()
print("\n--- Forma 3: método format() ---")
formateado3 = "{}, {}".format(apellidos, nombre)
print(formateado3)

print("-" * 40)

# EJEMPLO COMPLETO CON VARIOS NOMBRES:
print("\n--- Ejemplo con nombre compuesto ---")
# Si el usuario introduce: "José María" y "Morales Vázquez"
# El resultado será: "Morales Vázquez, José María"

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
