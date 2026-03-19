# ============================================================================
# BOLETÍN 7 - EJERCICIO 3
# ============================================================================
# ENUNCIADO:
# Ser un auténtico fiestero es un arte. Consideramos que los invitados de
# una fiesta que son auténticos profesionales de pasárselo bien son aquellos
# que siempre llegan a la misma cuando ya está al menos la mitad de la gente
# que ha sido invitada pero no si son los dos últimos.
# Haced una función en python que reciba una tupla con los asistentes a una
# fiesta en el orden en que han llegado y nos diga por pantalla quienes son
# los que realmente saben hacerlo bien.
#
# Ejemplo:
#   ('Jorge', 'Alba', 'Nadia', 'Héctor', 'Óscar', 'Ricardo', 'Kevin')
# El único profesional del festejo sería Óscar.
#
# CONCEPTOS CLAVE:
# - Cálculo de índices basado en longitud
# - Condiciones compuestas para determinar rango válido
# - Slicing de tuplas
# ============================================================================

def profesionales_fiesta(asistentes):
    """
    Determina quiénes son los "profesionales" de la fiesta.
    
    Un profesional llega cuando:
    - Ya está al menos la mitad de los invitados
    - NO es de los dos últimos en llegar
    
    Parámetros:
        asistentes (tuple): Tupla con nombres en orden de llegada
    """
    total = len(asistentes)
    
    if total < 4:
        print("No hay suficientes invitados para determinar profesionales.")
        return
    
    # Calcular índices
    mitad = total // 2           # A partir de aquí hay al menos la mitad
    ultimos_dos = total - 2      # A partir de aquí son los dos últimos
    
    # Los profesionales están entre mitad y ultimos_dos (sin incluir)
    profesionales = asistentes[mitad:ultimos_dos]
    
    print(f"Total de invitados: {total}")
    print(f"Llegaron antes de la mitad: {asistentes[:mitad]}")
    print(f"Profesionales del festejo: {profesionales}")
    print(f"Los dos últimos: {asistentes[ultimos_dos:]}")
    
    if len(profesionales) == 1:
        print(f"\n🎉 El único profesional del festejo es {profesionales[0]}")
    elif len(profesionales) > 1:
        print(f"\n🎉 Los profesionales del festejo son: {', '.join(profesionales)}")
    else:
        print("\n😕 No hay profesionales del festejo en esta fiesta")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print("=" * 50)
print("EJERCICIO 3: Profesionales del festejo")
print("=" * 50)

# Ejemplo del enunciado
print("\n📊 Ejemplo del enunciado:")
print("-" * 40)
fiesta = ('Jorge', 'Alba', 'Nadia', 'Héctor', 'Óscar', 'Ricardo', 'Kevin')
print(f"Asistentes: {fiesta}")
print()
profesionales_fiesta(fiesta)

# Más ejemplos
print("\n📊 Fiesta con más invitados:")
print("-" * 40)
fiesta2 = ('Ana', 'Luis', 'Pepe', 'María', 'Juan', 'Carmen', 'Pedro', 'Sara', 'Tomás', 'Lucía')
print(f"Asistentes: {fiesta2}")
print()
profesionales_fiesta(fiesta2)

print("\n📊 Fiesta pequeña:")
print("-" * 40)
fiesta3 = ('A', 'B', 'C', 'D')
print(f"Asistentes: {fiesta3}")
print()
profesionales_fiesta(fiesta3)

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
