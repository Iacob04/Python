import csv

# =============================================================================
# Ejercicio – Agenda en CSV
# Operaciones: listar, añadir, filtrar por nombre, eliminar por nombre
# =============================================================================

print("Listar")
with open("Agenda.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila["nombre"], fila["telefono"], fila["email"])


print("Añadir gente")
datos = [{"nombre": "Perez", "telefono": "874568457", "email": "manolo@gmail.com"}]

with open("Agenda.csv", "a", encoding="utf-8") as f:
    campos = ["nombre", "telefono", "email"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writerows(datos)


print("Filtrar por Nombre")
with open("Agenda.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        if fila["nombre"] == "Mario":
            print(fila["nombre"], fila["telefono"], fila["email"])


print("Eliminar por nombre")
Eliminar = "Manolo"
filas = []

# 1. Leer todas las filas excepto la que queremos borrar
with open("Agenda.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        if fila["nombre"] != Eliminar:
            filas.append(fila)

# 2. Reescribir el fichero completo sin la fila eliminada
with open("Agenda.csv", "w", encoding="utf-8") as f:
    campos = ["nombre", "telefono", "email"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(filas)
