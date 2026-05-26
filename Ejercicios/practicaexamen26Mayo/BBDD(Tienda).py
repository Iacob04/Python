# =============================================================================
#  EJERCICIO BASES DE DATOS (RA6) — GESTIÓN DE UNA TIENDA DE VIDEOJUEGOS
# =============================================================================
#  ENUNCIADO:
#  Tabla "juegos": id (PK autoincrement), titulo (TEXT), plataforma (TEXT),
#  precio (REAL), stock (INTEGER), oferta (INTEGER, 0=no / 1=sí).
#
#  P1 (2 pts) Crear la tabla juegos si no existe, con restricciones de
#             integridad (PK, campos obligatorios, valor por defecto de oferta).
#  P2 (2 pts) Insertar 3 juegos usando parámetros (?). Justificar los ?.
#  P3 (2 pts) Mostrar título y precio de los juegos de 'Switch' con precio < 40,
#             ordenados de más barato a más caro.
#  P4 (2 pts) Poner oferta = 1 en todos los juegos con stock > 10.
#  P5 (2 pts) Mostrar cuántos juegos hay de cada plataforma (GROUP BY).
# =============================================================================

import sqlite3   # módulo de Python para trabajar con bases de datos SQLite


# =============================================================================
#  SCRIPT QUE DA EL PROFESOR — crea y rellena tienda.db (NO hay que escribirlo)
# =============================================================================

# connect() crea el fichero tienda.db si no existe; si ya existe, se conecta.
conexion = sqlite3.connect("tienda.db")
# El cursor es el objeto con el que se lanzan las consultas SQL.
cursor = conexion.cursor()

# Borramos la tabla si ya existía, para empezar limpio cada vez que se ejecuta.
cursor.execute("DROP TABLE IF EXISTS juegos")

# Creamos la tabla con sus restricciones de integridad.
cursor.execute("""
    CREATE TABLE juegos (
        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo      TEXT    NOT NULL,
        plataforma  TEXT    NOT NULL,
        precio      REAL    NOT NULL,
        stock       INTEGER NOT NULL,
        oferta      INTEGER NOT NULL DEFAULT 0
    )
""")

# Lista de juegos de ejemplo (sin id: lo pone solo el AUTOINCREMENT).
# Cada tupla = (titulo, plataforma, precio, stock, oferta)
juegos = [
    ("The Legend of Zelda: Tears of the Kingdom", "Switch", 59.99, 15, 0),
    ("Animal Crossing: New Horizons",             "Switch", 39.99, 8,  0),
    ("Mario Kart 8 Deluxe",                       "Switch", 35.00, 20, 0),
    ("God of War Ragnarök",                       "PS5",    69.99, 12, 0),
    ("Spider-Man 2",                              "PS5",    79.99, 5,  0),
    ("Hades II",                                  "PC",     29.99, 30, 0),
    ("Baldur's Gate 3",                           "PC",     59.99, 18, 0),
    ("Stardew Valley",                            "PC",     13.99, 25, 0),
]

# executemany() inserta TODAS las filas de la lista de una vez.
# Los ? son marcadores de posición: SQLite mete cada valor de forma segura.
cursor.executemany("""
    INSERT INTO juegos (titulo, plataforma, precio, stock, oferta)
    VALUES (?, ?, ?, ?, ?)
""", juegos)

# commit() CONFIRMA los cambios. Sin esto, las inserciones no se guardan.
conexion.commit()

# Comprobación rápida: mostramos lo que se ha guardado.
cursor.execute("SELECT * FROM juegos")
print("Base de datos 'tienda.db' creada con estos juegos:")
for fila in cursor.fetchall():
    print(" ", fila)

# Cerramos cursor y conexión al terminar (buena práctica).
cursor.close()
conexion.close()


# =============================================================================
#  PREGUNTA 1 — CREAR LA TABLA CON INTEGRIDAD
# =============================================================================
def ejercicio1():
    # Abrimos conexión con la base de datos.
    conexion = sqlite3.connect("tienda.db")
    # Creamos el cursor para lanzar la consulta.
    cursor = conexion.cursor()

    # CREATE TABLE IF NOT EXISTS -> crea la tabla solo si todavía no existe
    # (IF NOT EXISTS evita el error si ya estaba creada).
    cursor.execute(""" CREATE TABLE IF NOT EXISTS juegos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo       TEXT    NOT NULL,
                   plataforma   TEXT    NOT NULL,
                   precio       REAL    NOT NULL,
                   stock        INTEGER NOT NULL,
                   oferta       INTEGER NOT NULL DEFAULT 0)
                   """)
    # INTEGRIDAD (esto es lo que hay que comentar para los puntos de teoría):
    #   PRIMARY KEY  -> identifica de forma ÚNICA cada fila (no se repite el id).
    #   AUTOINCREMENT-> SQLite asigna el id solo (1, 2, 3...), sin tener que darlo.
    #   NOT NULL     -> el campo es OBLIGATORIO, no puede quedarse vacío.
    #   DEFAULT 0    -> si no se indica oferta al insertar, vale 0 por defecto.

    # commit() confirma la creación de la tabla (es un cambio en la estructura).
    conexion.commit()
    # Cerramos la conexión.
    conexion.close()


# =============================================================================
#  PREGUNTA 2 — INSERTAR 3 JUEGOS CON PARÁMETROS (?)
# =============================================================================
def ejercicio2():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    # Lista con los 3 juegos a insertar. Cada tupla es una fila.
    juegos = [
        ("The Legend of Zelda: Tears of the Kingdom", "Switch", 59.99, 15, 0),
        ("Animal Crossing: New Horizons", "Switch", 39.99, 8, 0),
        ("Mario Kart 8 Deluxe", "Switch", 35.00, 20, 0),
    ]

    # executemany() inserta varias filas de golpe (una por cada tupla de la lista).
    # Los ? son marcadores de posición: cada ? se rellena con un valor de la tupla.
    # POR QUÉ SE USAN LOS ? (comentar para los puntos):
    #   - Evitan la INYECCIÓN SQL: el valor entra como dato, nunca como código.
    #   - SQLite escapa solos los caracteres raros (comillas, etc.).
    #   - Es la forma SEGURA y recomendada de meter datos en una consulta.
    cursor.executemany(""" 
        INSERT INTO juegos (titulo, plataforma, precio, stock, oferta)
        VALUES (?, ?, ?, ?, ?)
    """, juegos)

    # commit() OBLIGATORIO: el INSERT modifica datos, hay que confirmar.
    conexion.commit()
    conexion.close()


# =============================================================================
#  PREGUNTA 3 — CONSULTA CON FILTRO (Switch < 40 €, de barato a caro)
# =============================================================================
def ejercicio3():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    # SELECT titulo, precio -> solo pedimos esas dos columnas.
    # WHERE plataforma = ? AND precio < 40 -> filtramos: Switch Y precio menor a 40.
    # ORDER BY precio ASC -> ordena de menor a mayor precio (barato -> caro).
    #   (ASC = ascendente; sería DESC si fuese de caro a barato).
    # El ? se sustituye por "Switch". OJO: va como TUPLA de un elemento ("Switch",)
    #   con la COMA obligatoria al final.
    cursor.execute(""" 
        SELECT titulo, precio FROM juegos
        WHERE plataforma = ? AND precio < 40
        ORDER BY precio ASC
    """, ("Switch",))

    # fetchall() recoge TODAS las filas que devuelve el SELECT.
    juegos = cursor.fetchall()
    # Recorremos los resultados e imprimimos cada juego (título, precio).
    for juego in juegos:
        print(juego)

    # Un SELECT solo LEE: no necesita commit().
    cursor.close()
    conexion.close()


# =============================================================================
#  PREGUNTA 4 — ACTUALIZAR: poner oferta = 1 si stock > 10
# =============================================================================
def ejercicio4():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    # UPDATE juegos SET oferta = ? -> cambia el valor de la columna oferta.
    # WHERE stock > ? -> pero SOLO en las filas cuyo stock sea mayor que 10.
    # Los dos ? se rellenan con la tupla (1, 10): primero el 1 (oferta), luego el 10.
    cursor.execute(""" 
        UPDATE juegos SET oferta = ? WHERE stock > ?
    """, (1, 10))

    # commit() OBLIGATORIO: el UPDATE modifica datos, hay que confirmar.
    conexion.commit()
    cursor.close()
    conexion.close()


# =============================================================================
#  PREGUNTA 5 — ESTADÍSTICAS: cuántos juegos hay por plataforma (GROUP BY)
# =============================================================================
def ejercicio5():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    # COUNT(*) -> cuenta filas.
    # GROUP BY plataforma -> agrupa las filas por plataforma y cuenta cada grupo.
    #   Resultado: una fila por plataforma con su número de juegos.
    cursor.execute(""" 
        SELECT plataforma, COUNT(*) FROM juegos GROUP BY plataforma
    """)

    # fetchall() recoge todas las filas (una por plataforma).
    juegos = cursor.fetchall()

    print("Juegos por plataforma:")
    # Recorremos e imprimimos cada par (plataforma, cantidad).
    for juego in juegos:
        print(juego)

    # SELECT: no necesita commit().
    cursor.close()
    conexion.close()


# =============================================================================
#  LLAMADAS A LAS FUNCIONES (se ejecutan en orden)
# =============================================================================
ejercicio1()   # crea la tabla (si no existía)
ejercicio2()   # inserta los 3 juegos
ejercicio3()   # consulta Switch < 40
ejercicio4()   # pone ofertas
ejercicio5()   # cuenta por plataforma