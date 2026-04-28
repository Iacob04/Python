import sqlite3

# ─────────────────────────────────────────────
#  EJERCICIO 2 – Gestión de alumnos y sus notas
#  Tabla: alumnos  (id, nombre, apellido, curso)
#  Tabla: notas    (id, id_alumno, asignatura, nota)
#  → Ejemplo con DOS tablas relacionadas (clave foránea)
# ─────────────────────────────────────────────

# ── Conexión global ──────────────────────────
conexion = sqlite3.connect("alumnos.db")
conexion.row_factory = sqlite3.Row   # Acceso a columnas por nombre
cursor = conexion.cursor()


# ── 1. Crear ambas tablas ────────────────────
def crear_tablas():
    """Crea las tablas 'alumnos' y 'notas' si no existen."""

    # Tabla principal de alumnos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nombre   TEXT    NOT NULL,
            apellido TEXT    NOT NULL,
            curso    TEXT    NOT NULL
        )
    """)

    # Tabla de notas relacionada con alumnos mediante id_alumno (clave foránea)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_alumno  INTEGER NOT NULL,
            asignatura TEXT    NOT NULL,
            nota       REAL    NOT NULL,
            FOREIGN KEY (id_alumno) REFERENCES alumnos(id)
        )
    """)

    conexion.commit()
    print("Tablas 'alumnos' y 'notas' listas.")


# ── 2. Insertar alumno ───────────────────────
def insertar_alumno(nombre, apellido, curso):
    """Añade un alumno y devuelve su id autogenerado."""
    cursor.execute("""
        INSERT INTO alumnos (nombre, apellido, curso)
        VALUES (?, ?, ?)
    """, (nombre, apellido, curso))
    conexion.commit()

    id_nuevo = cursor.lastrowid   # id que SQLite asignó al registro recién insertado
    print(f"Alumno '{nombre} {apellido}' insertado con id={id_nuevo}.")
    return id_nuevo


# ── 3. Insertar nota ─────────────────────────
def insertar_nota(id_alumno, asignatura, nota):
    """Registra una nota para el alumno indicado."""
    cursor.execute("""
        INSERT INTO notas (id_alumno, asignatura, nota)
        VALUES (?, ?, ?)
    """, (id_alumno, asignatura, nota))
    conexion.commit()
    print(f"  Nota {nota} en '{asignatura}' añadida al alumno id={id_alumno}.")


# ── 4. Mostrar alumnos ───────────────────────
def mostrar_alumnos():
    """Lista todos los alumnos registrados."""
    cursor.execute("SELECT * FROM alumnos")
    registros = cursor.fetchall()

    print("\n─── Alumnos ───")
    for r in registros:
        print(f"[{r['id']}] {r['nombre']} {r['apellido']} – {r['curso']}")
    print()


# ── 5. Ver notas de un alumno ────────────────
def notas_de_alumno(id_alumno):
    """Muestra todas las notas de un alumno concreto."""
    cursor.execute("""
        SELECT asignatura, nota
        FROM notas
        WHERE id_alumno = ?
        ORDER BY nota DESC    -- Ordena de mayor a menor nota
    """, (id_alumno,))
    registros = cursor.fetchall()

    print(f"\n─── Notas del alumno id={id_alumno} ───")
    for r in registros:
        print(f"  {r['asignatura']}: {r['nota']}")
    print()


# ── 6. Media de un alumno ────────────────────
def media_alumno(id_alumno):
    """Calcula la media de todas las notas de un alumno usando AVG de SQL."""
    cursor.execute("""
        SELECT AVG(nota) AS media   -- AVG() es una función de agregado de SQL
        FROM notas
        WHERE id_alumno = ?
    """, (id_alumno,))

    resultado = cursor.fetchone()   # fetchone() devuelve solo la primera fila
    media = resultado["media"]

    if media is None:
        print(f"El alumno id={id_alumno} no tiene notas registradas.")
    else:
        print(f"Media del alumno id={id_alumno}: {media:.2f}")


# ── 7. Actualizar curso de un alumno ─────────
def actualizar_curso(id_alumno, nuevo_curso):
    """Modifica el curso del alumno indicado."""
    cursor.execute("""
        UPDATE alumnos
        SET curso = ?
        WHERE id = ?
    """, (nuevo_curso, id_alumno))
    conexion.commit()
    print(f"Curso del alumno id={id_alumno} actualizado a '{nuevo_curso}'.")


# ── 8. Eliminar alumno (y sus notas) ─────────
def eliminar_alumno(id_alumno):
    """Borra primero las notas del alumno y luego el propio alumno.
    
    El orden importa: si borramos el alumno primero, las notas quedarían
    huérfanas (sin referencia válida en la tabla padre).
    """
    cursor.execute("DELETE FROM notas   WHERE id_alumno = ?", (id_alumno,))
    cursor.execute("DELETE FROM alumnos WHERE id = ?",        (id_alumno,))
    conexion.commit()
    print(f"Alumno id={id_alumno} y sus notas eliminados.")


# ── Programa principal ───────────────────────
crear_tablas()

# Insertar alumnos y guardar sus ids para usarlos al insertar notas
id_ana   = insertar_alumno("Ana",    "García",  "1DAM")
id_luis  = insertar_alumno("Luis",   "Martínez","1DAM")
id_sara  = insertar_alumno("Sara",   "López",   "2DAM")

# Insertar notas
insertar_nota(id_ana,  "Java",            8.5)
insertar_nota(id_ana,  "Bases de Datos",  9.0)
insertar_nota(id_ana,  "Sistemas",        7.0)

insertar_nota(id_luis, "Java",            5.5)
insertar_nota(id_luis, "Bases de Datos",  6.0)

insertar_nota(id_sara, "Java",            9.5)
insertar_nota(id_sara, "Bases de Datos",  8.0)
insertar_nota(id_sara, "Sistemas",        9.0)

# Mostrar alumnos
mostrar_alumnos()

# Ver notas de Ana y su media
notas_de_alumno(id_ana)
media_alumno(id_ana)

# Actualizar curso de Luis
actualizar_curso(id_luis, "2DAM")
mostrar_alumnos()

# Eliminar a Sara
eliminar_alumno(id_sara)
mostrar_alumnos()

# ── Cerrar conexión ──────────────────────────
cursor.close()
conexion.close()
print("Conexión cerrada.")
