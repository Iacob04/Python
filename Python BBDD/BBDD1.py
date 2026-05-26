import sqlite3

def set_up():
    conexion = sqlite3.connect('Peliculas.db')
    cursor = conexion.cursor()

    cursor.execute("""CREATE TABLE if not exists pelicula (
    id integer not null primary key autoincrement,
    titulo text not null,
    director text not null,
    anio integer not null,
    precio decimal not null,
    fecha_registro datetime default current_timestamp)""")

    cursor.execute("""insert into pelicula (titulo,director,anio,precio)
                      values (?,?,?,?)""",
                   ("la lista de schidler", "Steven Spielberg", 1993, 3.5))

    datos_nuevos = [
        ("El diablo se viste de prada 2", "david framkel", 1934, 2.5),
        ("Scopby Dog comienza el misterio", "briant levant", 2009, 2)
    ]

    cursor.executemany("""insert  into pelicula (titulo,director,anio,precio)
                          values (?,?,?,?)""", datos_nuevos)

    conexion.commit()
    cursor.close()
    conexion.close()


def mostrar_todo():
    with sqlite3.connect('Peliculas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pelicula")
        peliculas = cursor.fetchall()
        for p in peliculas:
            print("Titulo ", p[1])


def mostrar_apartir_de(anio):
    with sqlite3.connect('Peliculas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pelicula WHERE anio > ?", (anio,))
        peliculas = cursor.fetchall()
        for p in peliculas:
            print("Titulo: " , p[1], " Director :" , p[2], " Año publicado: " ,p[3] , " \n" )


def guardar_nuevo(titulo,director,anio,precio):
    with sqlite3.connect('Peliculas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute(""" insert into pelicula(titulo,director,anio,precio) values (?,?,?,?)""",(titulo,director,anio,precio))
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se ha podido guardar")
        else:
            print("Guardado correctamente")

def actualizar(titulo,director,anio,precio):
    with sqlite3.connect('Peliculas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("""update pelicula set titulo=?,director=?,anio=?,precio=? where  anio = ?""",(titulo,director,anio,precio))
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se ha podido actualizar")
        else:
            print("Actualizado correctamente")
# Ejecutar
set_up()

mostrar_apartir_de(1800)

print()

guardar_nuevo("false","ninguno",2025,2)

print("Todo")

mostrar_todo()