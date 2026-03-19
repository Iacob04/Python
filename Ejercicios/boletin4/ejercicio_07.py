# ============================================================================
# BOLETÍN 4 - EJERCICIO 7
# ============================================================================
# ENUNCIADO:
# Mejorar el programa anterior para que detecte si se trata de un NIF,
# un NIE o un CIF de empresa y nos comunique, además de si es válido,
# de qué tipo es.
# - Un CIF es una cadena de 9 caracteres donde la primera es una letra
#   y las otras ocho cifras.
# - Un NIE es una cadena de 9 caracteres que siempre empieza por X, Y o Z
#   y a continuación vienen 7 cifras y una letra final.
#
# CONCEPTOS CLAVE:
# - Diferenciar tipos de documentos
# - Condicionales anidados
# -startswith() para comprobar inicio de cadena
# ============================================================================

print("=" * 50)
print("EJERCICIO 7: Validación de NIF, NIE y CIF")
print("=" * 50)

# Pedir documento
documento = input("Introduce un documento (NIF, NIE o CIF): ").upper()

print("\n" + "-" * 40)

# Variable para el tipo detectado
tipo = None
es_valido = False

# Comprobar longitud primero
if len(documento) != 9:
    print(f"✗ Longitud incorrecta: {len(documento)} (debe ser 9)")
else:
    # Detectar tipo y validar
    
    # NIE: empieza por X, Y o Z
    if documento[0] in "XYZ":
        tipo = "NIE"
        # NIE: X/Y/Z + 7 números + 1 letra
        numeros = documento[1:8]  # Posiciones 1-7 (7 números)
        letra_final = documento[8]  # Última posición
        
        if numeros.isdigit() and letra_final.isalpha():
            es_valido = True
    
    # CIF: empieza por letra
    elif documento[0].isalpha():
        tipo = "CIF"
        # CIF: letra + 8 números
        numeros = documento[1:9]  # Posiciones 1-8 (8 números)
        
        if numeros.isdigit():
            es_valido = True
    
    # NIF: empieza por número
    elif documento[0].isdigit():
        tipo = "NIF"
        # NIF: 8 números + 1 letra
        numeros = documento[:8]  # Primeros 8
        letra_final = documento[8]  # Último
        
        if numeros.isdigit() and letra_final.isalpha():
            es_valido = True

# Mostrar resultado
if tipo:
    if es_valido:
        print(f"✓ El documento '{documento}' es un {tipo} VÁLIDO")
    else:
        print(f"✗ El documento '{documento}' parece ser un {tipo} pero es INVÁLIDO")
else:
    print(f"✗ No se pudo determinar el tipo de documento")

print("-" * 40)

# FORMATOS:
# --------------------------------------------------------
# | Tipo | Formato              | Ejemplo            |
# |------|----------------------|--------------------|
# | NIF  | 8 números + letra    | 12345678A          |
# | NIE  | X/Y/Z + 7 núm + letra| X1234567A          |
# | CIF  | Letra + 8 números    | A12345678          |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
