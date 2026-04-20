from pathlib import Path

FICHERO = "inventario.txt"


def añadir_producto():
    print("-- AÑADIENDO PRODUCTO --")
    nombre = input("Nombre: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")
    with open(FICHERO, "a", encoding="utf-8") as f:
        # Formato CSV: nombre,cantidad,precio
        f.write(f"{nombre},{cantidad},{precio}\n")
    print("Producto añadido.")


def actualizar_stock():
    print("-- ACTUALIZANDO STOCK --")
    nombre_buscado = input("Nombre del producto a modificar: ")
    encontrado = False  # bandera para saber si se encontró el producto

    with open(FICHERO, "r+", encoding="utf-8") as f:
        lineas = f.readlines()  # lista donde cada elemento es una línea del fichero

        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[0].lower() == nombre_buscado.lower():
                print(f"Producto: {datos[0]} | Cantidad: {datos[1]} | Precio: {datos[2]}")
                operacion = input("¿Sumar(+) o restar(-) cantidad? ")
                delta = int(input("¿Cuánto? "))
                cantidad_actual = int(datos[1])

                if operacion == "+":
                    cantidad_actual += delta
                elif operacion == "-":
                    cantidad_actual -= delta

                # Reemplazamos la línea con la cantidad actualizada
                lineas[i] = f"{datos[0]},{cantidad_actual},{datos[2]}\n"
                encontrado = True

        if encontrado:
            f.seek(0)
            f.writelines(lineas)
            print("Stock actualizado.")
        else:
            print("Producto no encontrado.")


def valor_total_inventario():
    print("-- VALOR TOTAL DEL INVENTARIO --")
    total = 0
    with open(FICHERO, "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if len(datos) == 3:
                cantidad = int(datos[1])
                precio = float(datos[2])
                subtotal = cantidad * precio
                print(f"{datos[0]}: {cantidad} x {precio} = {subtotal}")
                total += subtotal
    print(f"Valor total: {total}")


# --- Punto de entrada ---
ruta = Path(FICHERO)

if not ruta.exists():
    # Si no existe el fichero lo creamos vacío
    ruta.touch()
    print("Fichero de inventario creado.")
else:
    print("1. Añadir producto")
    print("2. Actualizar stock")
    print("3. Informe de valor total")
    opcion = int(input("Elige opción: "))

    if opcion == 1:
        añadir_producto()
    elif opcion == 2:
        actualizar_stock()
    elif opcion == 3:
        valor_total_inventario()
    else:
        print("Opción no válida.")
