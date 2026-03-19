# ============================================================================
# BOLETÍN 4 - EJERCICIO 8
# ============================================================================
# ENUNCIADO:
# Las matrículas españolas constan de un número de cuatro dígitos y tres
# letras cualesquiera en mayúsculas a excepción de la Ñ y la Q.
# Escribe un programa en Python que detecte si una matrícula introducida
# por el usuario es válida o no.
#
# CONCEPTOS CLAVE:
# - Validación por partes
# - isdigit() para números
# - isalpha() para letras
# - in para comprobar caracteres prohibidos
# ============================================================================

print("=" * 50)
print("EJERCICIO 8: Validación de matrícula española")
print("=" * 50)

# Pedir matrícula
matricula = input("Introduce una matrícula (formato: 1234ABC): ").upper()

print("\n" + "-" * 40)

# Variable de validación
es_valida = True
errores = []

# 1. Comprobar longitud
if len(matricula) != 7:
    es_valida = False
    errores.append(f"Longitud incorrecta: {len(matricula)} (debe ser 7)")

# 2. Comprobar los 4 primeros son números
if len(matricula) >= 4:
    numeros = matricula[:4]
    if not numeros.isdigit():
        es_valida = False
        errores.append("Los 4 primeros caracteres deben ser números")

# 3. Comprobar las 3 últimas son letras válidas
if len(matricula) >= 7:
    letras = matricula[4:7]
    letras_prohibidas = "ÑQ"
    
    for letra in letras:
        if not letra.isalpha():
            es_valida = False
            errores.append(f"'{letra}' no es una letra")
        elif letra in letras_prohibidas:
            es_valida = False
            errores.append(f"La letra '{letra}' no está permitida en matrículas")

# Mostrar resultado
if es_valida:
    print(f"✓ La matrícula '{matricula}' es VÁLIDA")
else:
    print(f"✗ La matrícula '{matricula}' es INVÁLIDA")
    print("\nErrores encontrados:")
    for error in errores:
        print(f"  - {error}")

print("-" * 40)

# FORMATO DE MATRÍCULA:
# --------------------------------------------------------
# | Posición | Tipo      | Restricciones               |
# |----------|-----------|-----------------------------|
# | 1-4      | Números   | Cualquier dígito 0-9        |
# | 5-7      | Letras    | Mayúsculas, excepto Ñ y Q   |
# |          |           | Ejemplo válido: 1234ABC     |
# |          |           | Ejemplo inválido: 1234AÑC   |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
