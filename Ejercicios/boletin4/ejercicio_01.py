# ============================================================================
# BOLETÍN 4 - EJERCICIO 1
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que pida al usuario una cadena de texto
# y la escriba sin espacios en blanco (si los hubiera). Además, nos debe
# de decir el número de espacios que ha encontrado y suprimido.
#
# CONCEPTOS CLAVE:
# - replace() para eliminar caracteres
# - count() para contar ocurrencias
# - Métodos de strings
# ============================================================================

print("=" * 50)
print("EJERCICIO 1: Eliminar espacios de una cadena")
print("=" * 50)

# Pedir cadena al usuario
cadena = input("Introduce una cadena de texto: ")

print("\n" + "-" * 40)

# Contar espacios antes de eliminarlos
num_espacios = cadena.count(" ")

# Eliminar espacios con replace()
cadena_sin_espacios = cadena.replace(" ", "")

# Mostrar resultados
print(f"Cadena original: '{cadena}'")
print(f"Cadena sin espacios: '{cadena_sin_espacios}'")
print(f"Número de espacios eliminados: {num_espacios}")

print("-" * 40)

# EXPLICACIÓN DE LOS MÉTODOS:
# --------------------------------------------------------
# | Método           | Descripción                       | Ejemplo          |
# |------------------|-----------------------------------|------------------|
# | cadena.count(" ")| Cuenta espacios en la cadena      | "a b".count(" ")=1|
# | cadena.replace() | Reemplaza caracteres              | "a b".replace()  |
# |                  | (" ", "") elimina espacios        | = "ab"           |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
