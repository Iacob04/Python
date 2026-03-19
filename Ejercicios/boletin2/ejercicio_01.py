# ============================================================================
# BOLETÍN 2 - EJERCICIO 1
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que nos pida tres números en cualquier
# orden y nos los muestre en pantalla ordenados de menor a mayor
#
# CONCEPTOS CLAVE:
# - Condicionales anidados para comparar números
# - Algoritmo de ordenación manual (sin usar sort())
# - Intercambio de valores
# ============================================================================

print("=" * 50)
print("EJERCICIO 1: Ordenar 3 números de menor a mayor")
print("=" * 50)

# Pedir los tres números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

print("\n" + "-" * 40)
print(f"Números introducidos: {num1}, {num2}, {num3}")
print("-" * 40)

# FORMA 1: Usando condicionales (algoritmo de ordenación manual)
print("\n--- Forma 1: Ordenación manual ---")

# Hacemos copias para no modificar los originales
a, b, c = num1, num2, num3

# Ordenar a y b
if a > b:
    a, b = b, a  # Intercambio simultáneo en Python

# Ordenar b y c
if b > c:
    b, c = c, b

# Volver a ordenar a y b (por si el segundo intercambio desordenó)
if a > b:
    a, b = b, a

print(f"Números ordenados: {a}, {b}, {c}")

# FORMA 2: Usando lista y sort() (más sencilla)
print("\n--- Forma 2: Usando sort() ---")

numeros = [num1, num2, num3]
numeros.sort()  # Ordena la lista de menor a mayor
print(f"Números ordenados: {numeros[0]}, {numeros[1]}, {numeros[2]}")

# FORMA 3: Usando sorted() (crea nueva lista)
print("\n--- Forma 3: Usando sorted() ---")

ordenados = sorted([num1, num2, num3])
print(f"Números ordenados: {ordenados}")

print("-" * 40)

# EXPLICACIÓN DE LAS FORMAS:
# --------------------------------------------------------
# | Forma    | Método        | Ventaja                   |
# |----------|---------------|---------------------------|
# | 1        | Condicionales | Entiendes el algoritmo    |
# | 2        | sort()        | Modifica lista original   |
# | 3        | sorted()      | Crea nueva lista          |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
