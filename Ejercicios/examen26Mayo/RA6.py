import sqlite3

def Pregunta1():
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT nombre, nivel_radiacion FROM habitantes WHERE rol = ? AND nivel_radiacion > ?
    """,("Explorador", 75))

    print("Exploradores con nivel de radiación superior a 75")
    habitantes = cursor.fetchall()
    for habitante in habitantes:
        print(habitante)


    cursor.close()
    conexion.close()

Pregunta1()

def Pregunta2():
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()

    cursor.execute(""" 
           UPDATE habitantes SET consumo_oxigeno = consumo_oxigeno + ? WHERE rol = ?
       """, (1.2, "Ingeniero"))


    conexion.commit()
    cursor.close()
    conexion.close()

Pregunta2()

def Pregunta3():
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()

    cursor.execute(""" 
               DELETE FROM habitantes WHERE nombre = ? 
           """, ("USUARIO_TEST",))

    conexion.commit()
    cursor.close()
    conexion.close()

Pregunta3()

def Pregunta4():
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()

    cursor.execute(""" 
           SELECT COUNT(*) FROM habitantes WHERE rol = ?
       """,("Médico",))


    habitantes = cursor.fetchall()

    print("Número total de habitantes con rol Médico")

    for habitante in habitantes:
        print(habitante)

    cursor.execute(""" 
               SELECT  AVG(consumo_oxigeno) FROM habitantes WHERE rol = ?
           """, ("Médico",))
    habitantes = cursor.fetchall()

    print("Promedio de consumo de oxígeno del rol Médico")

    for habitante in habitantes:
        print(habitante)


    cursor.close()
    conexion.close()

Pregunta4()

def Pregunta5():
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()


    cursor.execute(""" 
           INSERT INTO habitantes (nombre, rol, consumo_oxigeno, nivel_radiacion)
           VALUES (?, ?, ?, ?)
       """,("Kaelen Voss","Cultivador",8.5, 12))


    conexion.commit()
    conexion.close()

Pregunta5()