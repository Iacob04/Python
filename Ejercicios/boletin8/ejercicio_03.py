# ============================================================================
# BOLETÍN 8 - EJERCICIO 3
# ============================================================================
# ENUNCIADO:
# Escribe un programa en Python que sirva para gestionar las facturas
# pendientes de cobro de una empresa. Las facturas se almacenarán en un
# diccionario donde la clave será el número de factura (sólo puede ser
# entero) y el valor el coste de la factura (que puede tener decimales).
# El programa debe preguntar al usuario si quiere añadir una nueva factura,
# pagar una existente o terminar. Si desea añadir una nueva factura se
# preguntará por el número de factura y su coste y se añadirá al diccionario.
# Si se desea pagar una factura se preguntará por el número de factura y
# se eliminará del diccionario si existe. Después de cada operación el
# programa debe mostrar la cantidad cobrada hasta el momento y la cantidad
# pendiente de cobro.
#
# CONCEPTOS CLAVE:
# - Menú interactivo con bucle
# - Operaciones CRUD en diccionarios
# - Acumuladores de totales
# ============================================================================

print("=" * 50)
print("EJERCICIO 3: Gestión de facturas")
print("=" * 50)

# Diccionario para almacenar facturas
# Clave: número de factura (int)
# Valor: coste (float)
facturas = {}

# Variables para llevar la cuenta
cobrado = 0.0

print("\n💼 SISTEMA DE GESTIÓN DE FACTURAS")
print("=" * 40)

while True:
    print(f"\nRecaudado: {cobrado:.1f}")
    print(f"Pendiente de cobro: {sum(facturas.values()):.1f}")
    print()
    
    # Mostrar menú
    opcion = input("¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ").upper()
    
    if opcion == "T":
        print("\nFin del programa")
        break
    
    elif opcion == "A":
        try:
            num_factura = int(input("Introduce el número de la factura: "))
            coste = float(input("Introduce el coste de la factura: "))
            
            # Verificar que no exista ya
            if num_factura in facturas:
                print("\nYa existe esa factura")
            else:
                facturas[num_factura] = coste
                print(f"\nFactura {num_factura} añadida por {coste:.1f} €")
        
        except ValueError:
            print("\nError: El número debe ser entero y el coste un número")
    
    elif opcion == "P":
        try:
            num_factura = int(input("Introduce el número de la factura a pagar: "))
            
            if num_factura in facturas:
                # Pagar la factura
                cobrado += facturas[num_factura]
                del facturas[num_factura]
                print("\nFactura pagada")
            else:
                print("\nNo existe esa factura")
        
        except ValueError:
            print("\nError: El número de factura debe ser entero")
    
    else:
        print("\nOpción no válida. Usa A, P o T.")

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
