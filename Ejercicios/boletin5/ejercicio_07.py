# ============================================================================
# BOLETÍN 5 - EJERCICIO 7
# ============================================================================
# ENUNCIADO:
# Haced ahora un programa donde las listas conteniendo los países y sus
# poblaciones ya viene escrita en el código. Tú programa ahora tendrá que
# pedir el nombre de un país por teclado y mostrar su población. Si el
# país que se pide no está en la lista debería de informar de ello
#
# CONCEPTOS CLAVE:
# - Listas predefinidas en el código
# - Búsqueda en listas con index() o in
# - Manejo de error si no se encuentra
# ============================================================================

print("=" * 50)
print("EJERCICIO 7: Búsqueda de población por país")
print("=" * 50)

# Listas predefinidas (datos de ejemplo)
paises = [
    "España",
    "Francia",
    "Italia",
    "Alemania",
    "Portugal",
    "Reino Unido",
    "China",
    "India",
    "Estados Unidos",
    "Brasil"
]

poblaciones = [
    47420568,    # España
    67749632,    # Francia
    59109668,    # Italia
    83190556,    # Alemania
    10270865,    # Portugal
    67326569,    # Reino Unido
    1411778724,  # China
    1380004385,  # India
    331449281,   # Estados Unidos
    212559417    # Brasil
]

print("\n🌍 PAÍSES DISPONIBLES:")
print("-" * 40)
for pais in paises:
    print(f"  • {pais}")

print("-" * 40)

# Pedir país a buscar
pais_buscar = input("\nIntroduce el nombre de un país: ")

print("\n" + "-" * 40)

# FORMA 1: Usando in y index()
if pais_buscar in paises:
    # Obtener el índice del país
    indice = paises.index(pais_buscar)
    # Obtener la población con el mismo índice
    poblacion = poblaciones[indice]
    
    print(f"✓ {pais_buscar}")
    print(f"  Población: {poblacion:,} habitantes")
else:
    print(f"✗ '{pais_buscar}' no está en la lista de países.")

# FORMA 2: Usando try-except (también válida)
print("\n--- Forma 2: Con try-except ---")
try:
    indice = paises.index(pais_buscar)
    print(f"{pais_buscar}: {poblaciones[indice]:,} habitantes")
except ValueError:
    print(f"País no encontrado")

print("-" * 40)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
