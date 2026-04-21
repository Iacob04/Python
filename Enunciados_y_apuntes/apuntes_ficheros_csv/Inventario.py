import csv

print("Añadir Productos")
datos1 = [{"Nombre": "Sal",     "Cantidad": "2",    "Precio": "13"}]
datos2 = [{"Nombre": "Platanos","Cantidad": "2.01", "Precio": "5.6"}]

with open("Inventario.csv", 'w', encoding="utf-8") as f:
    campos = ["Nombre", "Cantidad", "Precio"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(datos1)
    escritor.writerows(datos2)

print("Filtrar por Nombre")
with open("Inventario.csv", 'r', encoding="utf-8") as f:
    lector = csv.DictReader(f)
    Producto = "Platano"
    for linea in lector:
        if Producto in linea["Nombre"]:
            print("Nombre:", linea["Nombre"], "Cantidad:", linea["Cantidad"], "Precio:", linea["Precio"])

print("Calcular valor")
total = 0
with open("Inventario.csv", 'r', encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        num_c = float(linea["Cantidad"])
        num_p = float(linea["Precio"])
        valor = num_c * num_p
        print(round(valor, 2), linea["Nombre"])  # muestra el valor de cada producto
        total += valor
print("total:", round(total, 2))


# Ejemplo comentado: modificar un campo y guardar
#
# import csv
#
# # Leer todos los datos
# with open("Inventario.csv", 'r', encoding="utf-8", newline='') as f:
#     lector = csv.DictReader(f)
#     datos = list(lector)
#
# # Cambiar cantidad de "Sal" de 2 a 3
# for fila in datos:
#     if fila["Nombre"] == "Sal":
#         fila["Cantidad"] = "3"
#
# # Guardar
# with open("Inventario.csv", 'w', encoding="utf-8", newline='') as f:
#     campos = ["Nombre", "Cantidad", "Precio"]
#     escritor = csv.DictWriter(f, fieldnames=campos)
#     escritor.writeheader()
#     escritor.writerows(datos)
