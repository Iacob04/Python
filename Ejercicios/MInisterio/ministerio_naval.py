import sqlite3
from datetime import date

DB_NAME = "ministerio_naval.db"


def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS naves (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre           TEXT    NOT NULL,
            tipo             TEXT,
            año_construccion INTEGER,
            epoca            TEXT
        );

        CREATE TABLE IF NOT EXISTS agentes (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre          TEXT    NOT NULL,
            año_nacimiento  INTEGER,
            especialidad    TEXT,
            activo          INTEGER DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS misiones (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            id_agente      INTEGER NOT NULL REFERENCES agentes(id),
            id_nave        INTEGER NOT NULL REFERENCES naves(id),
            fecha_partida  TEXT    NOT NULL,
            fecha_regreso  TEXT,
            exito          INTEGER DEFAULT 0,
            incidencias    TEXT
        );
    """)
    conn.commit()
    conn.close()


def registrar_nave(nombre, tipo, año, epoca):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO naves (nombre, tipo, año_construccion, epoca) VALUES (?, ?, ?, ?)",
        (nombre, tipo, año, epoca)
    )
    conn.commit()
    nave_id = cursor.lastrowid
    conn.close()
    return nave_id


def enviar_agente(id_agente, id_nave, fecha_partida):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.id, a.nombre
        FROM misiones m
        JOIN agentes a ON a.id = m.id_agente
        WHERE m.id_agente = ? AND m.fecha_regreso IS NULL
    """, (id_agente,))
    mision_activa = cursor.fetchone()

    if mision_activa:
        cursor.execute("SELECT nombre FROM agentes WHERE id = ?", (id_agente,))
        agente = cursor.fetchone()
        nombre_agente = agente["nombre"] if agente else f"ID {id_agente}"
        print(f"Error: El agente {nombre_agente} ya esta en mision. Paradoja temporal detectada?")
        conn.close()
        return None

    cursor.execute(
        "INSERT INTO misiones (id_agente, id_nave, fecha_partida) VALUES (?, ?, ?)",
        (id_agente, id_nave, fecha_partida)
    )
    conn.commit()
    mision_id = cursor.lastrowid
    conn.close()
    return mision_id


def cerrar_mision(id_mision, exito, incidencias=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE misiones
        SET fecha_regreso = ?, exito = ?, incidencias = ?
        WHERE id = ?
    """, (str(date.today()), exito, incidencias, id_mision))
    conn.commit()
    conn.close()


def naves_sin_capitan():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT n.*
        FROM naves n
        WHERE n.id NOT IN (
            SELECT DISTINCT id_nave
            FROM misiones
            WHERE fecha_regreso IS NULL
        )
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado


def historial_agente(id_agente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            a.nombre        AS agente,
            n.nombre        AS nave,
            n.epoca         AS epoca,
            m.fecha_partida,
            m.fecha_regreso,
            m.exito,
            m.incidencias
        FROM misiones m
        JOIN agentes a ON a.id = m.id_agente
        JOIN naves   n ON n.id = m.id_nave
        WHERE m.id_agente = ?
        ORDER BY m.fecha_partida ASC
    """, (id_agente,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado


def misiones_fallidas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            n.nombre        AS nave,
            a.nombre        AS agente,
            m.fecha_partida,
            m.fecha_regreso,
            m.incidencias
        FROM misiones m
        JOIN agentes a ON a.id = m.id_agente
        JOIN naves   n ON n.id = m.id_nave
        WHERE m.exito = 0 AND m.fecha_regreso IS NOT NULL
        ORDER BY m.fecha_partida ASC
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado


def poblar_datos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM naves")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return
    conn.close()

    registrar_nave("Santa Maria",   "nao",     1460, "Siglo de Oro")
    registrar_nave("San Martin",    "galeon",  1580, "Siglo de Oro")
    registrar_nave("La Victoria",   "nao",     1519, "Siglo de Oro")
    registrar_nave("L'Hermione",    "fragata", 1779, "Ilustracion")
    registrar_nave("Drakkar Ulven", "drakkar",  870, "Edad Media")

    conn = conectar()
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO agentes (nombre, año_nacimiento, especialidad) VALUES (?, ?, ?)",
        [
            ("Elena Vazquez",    1988, "infiltracion"),
            ("Rodrigo Almeida",  1975, "combate"),
            ("Sofia del Tiempo", 1992, "diplomacia"),
            ("Marco Ferreira",   1981, "navegacion"),
        ]
    )
    conn.commit()
    conn.close()

    m1 = enviar_agente(1, 1, "1492-08-03")
    cerrar_mision(m1, exito=1, incidencias="Todo segun lo previsto. Colon no noto nada.")

    m2 = enviar_agente(2, 2, "1588-07-22")
    cerrar_mision(m2, exito=0, incidencias="Tormenta inesperada. Cubierta expuesta a canonazos. Regreso forzoso.")

    m3 = enviar_agente(3, 3, "1519-09-20")
    cerrar_mision(m3, exito=1, incidencias="Primera vuelta al mundo completada. Magallanes sospecho, pero callamos.")

    m4 = enviar_agente(4, 4, "1780-06-15")
    cerrar_mision(m4, exito=0, incidencias="Agente confundido con espia ingles. Huida precipitada en bote salvavidas.")

    enviar_agente(1, 5, "0872-04-12")

    m6 = enviar_agente(2, 1, "1492-10-12")
    cerrar_mision(m6, exito=1, incidencias="Regreso con Colon. Nadie lo vio saltar del barco.")

    print("\n[TEST DE PARADOJA]")
    enviar_agente(1, 2, "0872-05-01")


def mostrar_informe():
    print("\n" + "=" * 55)
    print("        MINISTERIO DEL TIEMPO - INFORME NAVAL")
    print("=" * 55)

    sin_capitan = naves_sin_capitan()
    print(f"\nNaves sin capitan asignado: {len(sin_capitan)}")
    for nave in sin_capitan:
        print(f"   - {nave['nombre']} ({nave['epoca']}, {nave['año_construccion']})")

    agente_ejemplo_id = 3
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM agentes WHERE id = ?", (agente_ejemplo_id,))
    nombre_ejemplo = cursor.fetchone()["nombre"]
    conn.close()

    misiones_agente = historial_agente(agente_ejemplo_id)
    print(f"\nHistorial de {nombre_ejemplo}:")
    if misiones_agente:
        for m in misiones_agente:
            estado  = "Exito" if m["exito"] else "Fallida"
            regreso = m["fecha_regreso"] if m["fecha_regreso"] else "En curso"
            incid   = m["incidencias"] if m["incidencias"] else "Sin incidencias"
            print(f"   - Nave: {m['nave']} | Epoca: {m['epoca']}")
            print(f"     Partida: {m['fecha_partida']} | Regreso: {regreso}")
            print(f"     Estado: {estado} | Incidencia: {incid}")
    else:
        print("   Sin misiones registradas.")

    fallidas = misiones_fallidas()
    print(f"\nMisiones fallidas registradas: {len(fallidas)}")
    for mf in fallidas:
        incid = mf["incidencias"] if mf["incidencias"] else "Sin descripcion"
        print(f"   - {mf['nave']} | {mf['agente']} | Incidencia: {incid}")

    print("\n" + "=" * 55 + "\n")


if __name__ == "__main__":
    crear_tablas()
    poblar_datos()
    mostrar_informe()
