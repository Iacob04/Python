import sqlite3

def crear_bbdd():
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    # Borrar tabla si existe
    cursor.execute("DROP TABLE IF EXISTS libros")

    # Crear tabla
    cursor.execute("""
        CREATE TABLE libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            anio INTEGER NOT NULL,
            prestado INTEGER NOT NULL DEFAULT 0
        )
    """)

    # Datos iniciales
    libros = [
        ("La sombra del viento", "Carlos Ruiz Zafón", "Novela", 2001, 0),
        ("Sapiens", "Yuval Noah Harari", "Ensayo", 2011, 0),
        ("Veinte poemas", "Pablo Neruda", "Poesía", 1924, 0),
        ("Patria", "Fernando Aramburu", "Novela", 2016, 0),
        ("El infinito en un junco", "Irene Vallejo", "Ensayo", 2019, 0),
        ("Reina roja", "Juan Gómez-Jurado", "Novela", 2018, 0),
        ("Rayuela", "Julio Cortázar", "Novela", 1963, 0),
    ]

    cursor.executemany("""
        INSERT INTO libros (titulo, autor, genero, anio, prestado)
        VALUES (?, ?, ?, ?, ?)
    """, libros)

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente")

crear_bbdd()


# ---------------------------------------------------
# EJERCICIO 1
# ---------------------------------------------------

def ejercicio1():

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            anio INTEGER NOT NULL,
            prestado INTEGER NOT NULL DEFAULT 0
        )
    """)

    conexion.commit()
    conexion.close()

ejercicio1()


# ---------------------------------------------------
# EJERCICIO 2
# ---------------------------------------------------

def ejercicio2():

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    libros = [
        ("Caperucita Roja", "Ale", "Novela", 2002, 0),
        ("Drácula", "Bram Stoker", "Terror", 1897, 0),
        ("1984", "George Orwell", "Distopía", 1949, 0)
    ]

    # Se usan ? para evitar inyección SQL y pasar parámetros de forma segura
    cursor.executemany("""
        INSERT INTO libros (titulo, autor, genero, anio, prestado)
        VALUES (?, ?, ?, ?, ?)
    """, libros)

    conexion.commit()
    conexion.close()

ejercicio2()


# ---------------------------------------------------
# EJERCICIO 3
# ---------------------------------------------------

def ejercicio3():

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT titulo, anio
        FROM libros
        WHERE genero = ? AND anio > ?
        ORDER BY anio DESC
    """, ("Novela", 2000))

    libros = cursor.fetchall()

    print("Novelas publicadas después del 2000:")

    for libro in libros:
        print(libro)

    conexion.close()

ejercicio3()


# ---------------------------------------------------
# EJERCICIO 4
# ---------------------------------------------------

def ejercicio4():

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE libros
        SET prestado = ?
        WHERE id = ?
    """, (1, 2))

    conexion.commit()
    conexion.close()

    print("Libro marcado como prestado")

ejercicio4()


# ---------------------------------------------------
# EJERCICIO 5
# ---------------------------------------------------

def ejercicio5():

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT genero, COUNT(*)
        FROM libros
        GROUP BY genero
    """)

    resultados = cursor.fetchall()

    print("Cantidad de libros por género:")

    for resultado in resultados:
        print(resultado)

    conexion.close()

ejercicio5()