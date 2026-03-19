# ============================================================================
# BOLETÍN 8 - EJERCICIO 4
# ============================================================================
# ENUNCIADO:
# Crear un programa que muestre un diccionario con los datos de los
# clientes de una tienda y su edad ordenados por nombre de pila.
# El diccionario, ya creado en el código, tendrá esta forma:
#   clientes = {
#       "Chuletón, José": 35,
#       "Tosidad, Rubén": 27,
#       "Rupto, Francisco": 44,
#       "Cotón, Carmelo": 56
#   }
# Y la salida por consola sería:
#   Carmelo Cotón (56)
#   Francisco Rupto (44)
#   José Chuletón (35)
#   Rubén Tosidad (27)
#
# CONCEPTOS CLAVE:
# - Ordenar diccionario por valor procesado
# - Manipulación de strings (split, join)
# - sorted() con key personalizada
# ============================================================================

print("=" * 50)
print("EJERCICIO 4: Clientes ordenados por nombre")
print("=" * 50)

# Diccionario de clientes (formato "Apellido, Nombre")
clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}

print("\n👥 CLIENTES ORDENADOS POR NOMBRE:")
print("=" * 40)

# Función para extraer el nombre de pila (para ordenar)
def obtener_nombre(clave):
    """
    Extrae el nombre de pila de una clave como "Apellido, Nombre".
    """
    partes = clave.split(", ")
    return partes[1]  # El nombre está después de la coma


# Ordenar las claves por nombre de pila
claves_ordenadas = sorted(clientes.keys(), key=obtener_nombre)

# Mostrar resultados
for clave in claves_ordenadas:
    # Separar apellido y nombre
    apellido, nombre = clave.split(", ")
    edad = clientes[clave]
    
    # Mostrar en formato "Nombre Apellido (edad)"
    print(f"{nombre} {apellido} ({edad})")

print("=" * 40)

# EXPLICACIÓN DEL PROCESO:
# --------------------------------------------------------
# | Paso | Operación                    | Resultado      |
# |------|------------------------------|----------------|
# | 1    | "Chuletón, José".split(", ") | ["Chuletón"]   |
# |      |                              | ["José"]       |
# | 2    | Obtener índice 1             | "José"         |
# | 3    | Ordenar por este valor       | Carmelo, Fran..|
# | 4    | Mostrar invertido            | José Chuletón  |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
