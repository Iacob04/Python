import  sqlite3

def set_up():
   with sqlite3.connect("juegos.db") as conexion:

        conexion = sqlite3.connect("juegos.db")
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS juegos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL, 
                numero_ugadores TEXT NOT NULL, 
                duraciom INTEGER NOT NULL, 
                fecha_inserccion DATETIME DEFAULT CURRENT_TIMESTAMP)
                """)

        conexion.commit()


conexion = sqlite3.connect("juegos.db") # si la base de datos no existe la crea y si está creada o existe se conecta
conexion.row_factory = sqlite3.Row # esto lo convierte a un diccionario
cursor = conexion.cursor()



def cargar_valores():
    cursor.execute(""" 
        INSERT INTO juegos (nombre, numero_ugadores, duraciom) 
        VALUES (?, ?, ?)
        """, ("SCRABLE", "2 - 8", 30))
    conexion.commit()

cursor.execute("""
        SELECT * FROM juegos
        """)

cursor.execute("""
    UPDATE JUEGOS SET numero_ugadores =?
    WHERE id =?
    """, ("3-4", 1))
conexion.commit()

cursor.execute(""" 
    DELETE FROM juegos WHERE id =?
 """,(1,))
conexion.commit()

registros = cursor.fetchall()
for registro in registros:
    print(registro["nombre"], registro["duraciom"]) # [] devuelve la columna que quieras exactamenete en este caso solo el nombre

cursor.close()
conexion.close()