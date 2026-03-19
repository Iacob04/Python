# ============================================================================
# BOLETÍN 4 - EJERCICIO 6
# ============================================================================
# ENUNCIADO:
# Escribe un programa en Python que valide si un NIF español es correcto.
# La longitud exacta de la cadena ha de ser de 9 caracteres.
# Los ocho primeros han de ser números comprendidos entre el 0 y el 9
# y el último una letra, no importa que esté en mayúsculas o minúsculas.
# Usa para ello las funciones isdigit e isalpha.
#
# CONCEPTOS CLAVE:
# - len() para longitud
# - isdigit() para comprobar si son números
# - isalpha() para comprobar si es letra
# - Acceso por índice a strings
# ============================================================================

print("=" * 50)
print("EJERCICIO 6: Validación de NIF")
print("=" * 50)

# Pedir NIF
nif = input("Introduce un NIF (8 números + 1 letra): ")

print("\n" + "-" * 40)

# Variable para controlar si es válido
es_valido = True
errores = []

# 1. Comprobar longitud
if len(nif) != 9:
    es_valido = False
    errores.append(f"Longitud incorrecta: {len(nif)} (debe ser 9)")

# 2. Comprobar que los 8 primeros son números
if len(nif) >= 8:
    numeros = nif[:8]  # Primeros 8 caracteres
    if not numeros.isdigit():
        es_valido = False
        errores.append("Los 8 primeros caracteres deben ser números")

# 3. Comprobar que el último es una letra
if len(nif) >= 9:
    letra = nif[8]  # Noveno carácter (índice 8)
    if not letra.isalpha():
        es_valido = False
        errores.append("El último carácter debe ser una letra")

# Mostrar resultado
if es_valido:
    print(f"✓ El NIF '{nif}' es VÁLIDO")
else:
    print(f"✗ El NIF '{nif}' es INVÁLIDO")
    print("\nErrores encontrados:")
    for error in errores:
        print(f"  - {error}")

print("-" * 40)

# EXPLICACIÓN DE LOS MÉTODOS:
# --------------------------------------------------------
# | Método      | Descripción                    | Ejemplo           |
# |-------------|--------------------------------|-------------------|
# | isdigit()   | True si todos son dígitos      | "123".isdigit()   |
# |             |                                | → True            |
# | isalpha()   | True si todos son letras       | "ABC".isalpha()   |
# |             |                                | → True            |
# | len()       | Devuelve longitud              | len("ABC") → 3    |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
