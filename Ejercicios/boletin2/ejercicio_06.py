# ============================================================================
# BOLETÍN 2 - EJERCICIO 6
# ============================================================================
# ENUNCIADO:
# Escribir un programa en python que pida una entrada por teclado hasta
# que escribamos la palabra FIN (con mayúsculas). En ese caso terminamos
# y mostramos por pantalla el número de entradas válidas que hemos hecho
# (sin contar esta última que sólo sirve para finalizar el programa)
#
# CONCEPTOS CLAVE:
# - Bucle while con condición de salida
# - Contador de iteraciones
# - Comparación de strings (distingue mayúsculas/minúsculas)
# ============================================================================

print("=" * 50)
print("EJERCICIO 6: Contador de entradas hasta FIN")
print("=" * 50)

# Inicializar contador
contador = 0

print("\nEscribe palabras (escribe FIN para terminar):")
print("-" * 40)

# Bucle infinito que termina cuando escribimos "FIN"
while True:
    entrada = input(f"Entrada #{contador + 1}: ")
    
    # Comprobar si es la palabra de salida
    if entrada == "FIN":
        print("-" * 40)
        print("¡Programa finalizado!")
        break  # Sale del bucle
    
    # Si no es FIN, incrementamos el contador
    contador += 1
    print(f"  ✓ Entrada válida registrada")

# Mostrar resultado final
print("\n" + "=" * 40)
print(f"TOTAL DE ENTRADAS VÁLIDAS: {contador}")
print("=" * 40)

# NOTAS IMPORTANTES:
# --------------------------------------------------------
# - "FIN" es diferente de "fin" o "Fin" (distingue mayúsculas)
# - Si quieres que acepte cualquier variante, usa: entrada.upper() == "FIN"
# - El contador NO incrementa cuando escribimos FIN
# --------------------------------------------------------

# VERSIÓN CASE-INSENSITIVE (acepta fin, FIN, Fin...):
print("\n--- Versión que acepta 'fin' en cualquier formato ---")
contador = 0
while True:
    entrada = input(f"Entrada #{contador + 1}: ")
    
    # upper() convierte a mayúsculas para comparar
    if entrada.upper() == "FIN":
        print(f"Total de entradas válidas: {contador}")
        break
    
    contador += 1

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
