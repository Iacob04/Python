# ============================================================================
# BOLETÍN 3 - EJERCICIO 2
# ============================================================================
# ENUNCIADO:
# Idem, pero que ponga los divisores uno detrás de otro separados por
# comas en lugar de uno debajo de otro
#
# CONCEPTOS CLAVE:
# - Almacenar divisores en una lista
# - join() para unir elementos con separador
# - print() con end="," para imprimir en la misma línea
# ============================================================================

print("=" * 50)
print("EJERCICIO 2: Divisores separados por comas")
print("=" * 50)

# Pedir número
numero = int(input("Introduce un número: "))

print("\n" + "-" * 40)

# FORMA 1: Usando lista y join()
print("--- Forma 1: Usando lista ---")

divisores = []  # Lista vacía para guardar divisores

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(str(i))  # Añadir como string

# join() une los elementos con ", " entre ellos
resultado = ", ".join(divisores)
print(f"Divisores de {numero}: {resultado}")

# FORMA 2: Imprimiendo directamente con end
print("\n--- Forma 2: Imprimiendo directamente ---")

print(f"Divisores de {numero}: ", end="")

for i in range(1, numero + 1):
    if numero % i == 0:
        # end="," hace que no haya salto de línea y se añada ", "
        if i < numero:
            print(i, end=", ")
        else:
            print(i)  # Último sin coma al final

# FORMA 3: Usando comprensión de listas (avanzado)
print("\n--- Forma 3: Comprensión de listas ---")

divisores = [str(i) for i in range(1, numero + 1) if numero % i == 0]
print(f"Divisores de {numero}: {', '.join(divisores)}")

print("-" * 40)

# EXPLICACIÓN DE join():
# --------------------------------------------------------
# | Método              | Resultado                      |
# |---------------------|--------------------------------|
# | ", ".join(["a","b"])| "a, b"                         |
# | "-".join(["1","2"]) | "1-2"                          |
# | "".join(["H","i"])  | "Hi"                           |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
