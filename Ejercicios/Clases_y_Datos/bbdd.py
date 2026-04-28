import sqlite3

def inicializar_base_datos():
    # Esto creará el archivo tienda.db en el mismo directorio donde ejecutes el script
    conexion = sqlite3.connect('tienda.db')
    cursor = conexion.cursor()

    # Ejecutar el script SQL
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        );

        INSERT INTO productos (nombre, categoria, precio, stock) VALUES
            ('Portátil Gaming X', 'Informática', 1200.50, 5),
            ('Monitor 27 Pulgadas', 'Informática', 250.00, 10),
            ('Ratón Inalámbrico', 'Informática', 25.99, 0),
            ('Smartphone Pro Max', 'Telefonía', 999.99, 15),
            ('Auriculares Bluetooth', 'Audio', 75.00, 20),
            ('Altavoz Inteligente', 'Audio', 45.00, 0),
            ('Teclado Mecánico', 'Informática', 85.50, 8),
            ('Tablet 10 Pulgadas', 'Informática', 550.00, 12),
            ('Cargador USB-C', 'Telefonía', 15.00, 50),
            ('Barra de Sonido', 'Audio', 150.00, 3);
    ''')

    conexion.commit()
    conexion.close()
    print("Base de datos 'tienda.db' creada y poblada con éxito.")


conexion = sqlite3.connect("tienda.db")
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()

def pregunta1():
    cursor.execute(""" SELECT nombre,precio FROM productos WHERE precio > 500 AND categoria 'Informática' """)
    recursos = cursor.fetchall()
    for recurso in recursos:
         print(recurso['nombre'], ": ", recurso['precio'], "€")

pregunta1()

def pregunta3():
    cursor.execute(""" DELETE FROM productos WHERE stock = 0  """)


pregunta3()

def pregunta5():
    cursor.execute(""" INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?,?,?,?) """,
                   ("Auriculares Inalámbricos Pro", "Audio", 89.99 , 15) )


pregunta5()


def pregunta4():
    cursor.execute(""" SELECT nombre FROM productos WHERE categoria = Telefonía  """ )
    recursos = cursor.fetchall()
    for recurso in recursos:
        print(recurso['nombre'], ": ", recurso['precio'])

pregunta4()