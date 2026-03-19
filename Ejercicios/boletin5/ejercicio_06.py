# ============================================================================
# BOLETÍN 5 - EJERCICIO 6
# ============================================================================
# ENUNCIADO:
# Haced un programa en python que nos permita cargar datos (nombre del
# país y población) desde el teclado. Los países deberían de estar en una
# lista y los datos de población en otra diferente pero las posiciones
# deberían de coincidir. La entrada de datos finaliza cuando se introduzca
# un -1 como nombre de un país. En ese momento nuestro programa debería
# de listar los países con sus poblaciones respectiva.
#
# CONCEPTOS CLAVE:
# - Dos listas relacionadas por índice
# - Listas paralelas
# - Bucle con condición de salida
# ============================================================================

print("=" * 50)
print("EJERCICIO 6: Listas paralelas - Países y poblaciones")
print("=" * 50)

# Listas paralelas (relacionadas por índice)
paises = []
poblaciones = []

print("\n🌍 INTRODUCCIÓN DE DATOS DE PAÍSES")
print("   (Escribe -1 como nombre para terminar)")
print("-" * 40)

while True:
    # Pedir nombre del país
    pais = input("\nNombre del país: ")
    
    # Condición de salida
    if pais == "-1":
        print("-" * 40)
        print("Finalizando entrada de datos...")
        break
    
    # Pedir población
    poblacion = int(input(f"Población de {pais}: "))
    
    # Añadir a las listas
    paises.append(pais)
    poblaciones.append(poblacion)
    
    print(f"  ✓ {pais} añadido. Total: {len(paises)} países")

# Mostrar resultados
print("\n" + "=" * 40)
print("LISTADO DE PAÍSES Y POBLACIONES")
print("=" * 40)

if len(paises) > 0:
    for i in range(len(paises)):
        # Accedemos a ambas listas con el mismo índice
        print(f"{i+1:2d}. {paises[i]:20s} - {poblaciones[i]:,} habitantes")
    
    print("-" * 40)
    print(f"Total de países: {len(paises)}")
    
    # Calcular población total
    poblacion_total = sum(poblaciones)
    print(f"Población total: {poblacion_total:,} habitantes")
else:
    print("No se introdujo ningún país.")

print("=" * 40)

# CONCEPTO DE LISTAS PARALELAS:
# --------------------------------------------------------
# | Índice | Países       | Poblaciones | Relación       |
# |--------|--------------|-------------|----------------|
# |   0    | "España"     | 47000000    | España tiene   |
# |        |              |             | 47 millones    |
# |   1    | "Francia"    | 67000000    | Francia tiene  |
# |        |              |             | 67 millones    |
# |   2    | "Italia"     | 59000000    | Italia tiene   |
# |        |              |             | 59 millones    |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
