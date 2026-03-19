# ============================================================================
# BOLETÍN 3 - EJERCICIO 6
# ============================================================================
# ENUNCIADO:
# Modificar el programa anterior para que, además, nos diga cual han
# sido el número mayor y el menor que has introducido
#
# CONCEPTOS CLAVE:
# - Variables para almacenar máximo y mínimo
# - Inicialización del máximo y mínimo con el primer valor
# - Actualización condicional de máximo/mínimo
# ============================================================================

print("=" * 50)
print("EJERCICIO 6: Estadísticas con máximo y mínimo")
print("=" * 50)

# Inicializar variables
contador = 0
suma_total = 0
numero_maximo = None   # None indica que aún no hay valor
numero_minimo = None

print("\nIntroduce números (escribe EXIT para terminar):")
print("-" * 40)

while True:
    entrada = input(f"Número #{contador + 1}: ")
    
    if entrada.upper() == "EXIT":
        break
    
    try:
        numero = int(entrada)
        suma_total += numero
        contador += 1
        
        # Actualizar máximo
        if numero_maximo is None or numero > numero_maximo:
            numero_maximo = numero
            print(f"  ✓ Nuevo MÁXIMO: {numero_maximo}")
        
        # Actualizar mínimo
        if numero_minimo is None or numero < numero_minimo:
            numero_minimo = numero
            print(f"  ✓ Nuevo MÍNIMO: {numero_minimo}")
        
    except ValueError:
        print(f"  ✗ '{entrada}' no es un número válido.")

# Mostrar resultados
print("\n" + "=" * 40)
print("RESULTADOS:")
print("-" * 40)

if contador > 0:
    media = suma_total / contador
    print(f"  Números introducidos: {contador}")
    print(f"  Suma total:           {suma_total}")
    print(f"  Media aritmética:     {media:.2f}")
    print(f"  Número MAYOR:         {numero_maximo}")
    print(f"  Número MENOR:         {numero_minimo}")
else:
    print("  No se introdujo ningún número.")

print("=" * 40)

# EXPLICACIÓN DE LA INICIALIZACIÓN:
# --------------------------------------------------------
# | Variable   | Valor inicial | Razón                    |
# |------------|---------------|--------------------------|
# | maximo     | None          | Cualquier número será >  |
# | minimo     | None          | Cualquier número será <  |
# --------------------------------------------------------
#
# Alternativa: inicializar con el primer número introducido

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
