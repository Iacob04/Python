# ============================================================================
# BOLETÍN 2 - EJERCICIO 8
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que pida una contraseña por teclado
# (dos veces) y si no coinciden nos las vuelva a pedir hasta que lo hagan
#
# CONCEPTOS CLAVE:
# - Bucle while con condición de validación
# - Comparación de strings
# - Validación de entrada de usuario
# ============================================================================

print("=" * 50)
print("EJERCICIO 8: Validación de contraseña")
print("=" * 50)

print("\n🔐 CONFIGURACIÓN DE CONTRASEÑA")
print("-" * 40)

# Bucle que se repite hasta que las contraseñas coincidan
intentos = 0

while True:
    intentos += 1
    
    # Pedir contraseña dos veces
    print(f"\n--- Intento #{intentos} ---")
    password1 = input("Introduce la contraseña: ")
    password2 = input("Repite la contraseña:   ")
    
    # Comparar las contraseñas
    if password1 == password2:
        print("\n✓ ¡Contraseñas coinciden!")
        print("  Contraseña configurada correctamente.")
        break  # Salir del bucle
    else:
        print("\n✗ Las contraseñas NO coinciden.")
        print("  Inténtalo de nuevo.")

print("-" * 40)
print(f"Número de intentos necesarios: {intentos}")

# VERSIÓN ALTERNATIVA (con while condición):
print("\n--- Versión alternativa ---")

password1 = ""
password2 = "diferente"  # Valores diferentes para entrar al bucle

while password1 != password2:
    password1 = input("Contraseña: ")
    password2 = input("Repite:     ")
    
    if password1 != password2:
        print("No coinciden. Inténtalo de nuevo.\n")

print("¡Contraseña guardada!")

# NOTAS DE SEGURIDAD:
# --------------------------------------------------------
# - En programas reales, NUNCA almacenes contraseñas en texto plano
# - Usa librerías como hashlib o bcrypt para cifrarlas
# - Considera ocultar la entrada con getpass (no muestra caracteres)
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
