import sqlite3

# ─────────────────────────────────────────────
#  EJERCICIO 1 – Base de datos de una biblioteca
#  Tabla: libros (id, titulo, autor, anio, disponible)
# ─────────────────────────────────────────────

# ── Conexión global ──────────────────────────
# Si el archivo .db no existe lo crea; si ya existe se conecta
conexion = sqlite3.connect("biblioteca.db")
conexion.row_factory = sqlite3.Row   # Permite acceder a las columnas por nombre: registro["titulo"]
cursor = conexion.cursor()


# ── 1. Crear la tabla ────────────────────────
def crear_tabla():
    """Crea la tabla 'libros' si todavía no existe."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            titulo      TEXT    NOT NULL,
            autor       TEXT    NOT NULL,
            anio        INTEGER NOT NULL,
            disponible  INTEGER NOT NULL DEFAULT 1   -- 1 = disponible, 0 = prestado
        )
    """)
    conexion.commit()   # Confirma los cambios en la base de datos
    print("Tabla 'libros' lista.")


# ── 2. Insertar un libro ─────────────────────
def insertar_libro(titulo, autor, anio):
    """Inserta un nuevo libro en la tabla.
    
    Los '?' son marcadores de posición que evitan inyección SQL.
    Los valores reales se pasan como tupla en el segundo argumento.
    """
    cursor.execute("""
        INSERT INTO libros (titulo, autor, anio)
        VALUES (?, ?, ?)
    """, (titulo, autor, anio))
    conexion.commit()
    print(f"Libro '{titulo}' insertado correctamente.")


# ── 3. Mostrar todos los libros ──────────────
def mostrar_libros():
    """Recupera y muestra todos los registros de la tabla."""
    cursor.execute("SELECT * FROM libros")
    registros = cursor.fetchall()   # Devuelve una lista con todas las filas

    if not registros:
        print("No hay libros registrados.")
        return

    print("\n─── Listado de libros ───")
    for registro in registros:
        # Accedemos a cada columna por su nombre gracias a row_factory
        estado = "Disponible" if registro["disponible"] == 1 else "Prestado"
        print(f"[{registro['id']}] {registro['titulo']} – {registro['autor']} ({registro['anio']}) | {estado}")
    print()


# ── 4. Actualizar disponibilidad ─────────────
def cambiar_disponibilidad(id_libro, nuevo_estado):
    """Cambia el campo 'disponible' de un libro concreto.
    
    nuevo_estado: 1 (disponible) o 0 (prestado)
    """
    cursor.execute("""
        UPDATE libros
        SET disponible = ?
        WHERE id = ?
    """, (nuevo_estado, id_libro))
    conexion.commit()
    print(f"Disponibilidad del libro id={id_libro} actualizada a {nuevo_estado}.")


# ── 5. Eliminar un libro ─────────────────────
def eliminar_libro(id_libro):
    """Borra el registro cuyo id coincida con el parámetro."""
    cursor.execute("""
        DELETE FROM libros
        WHERE id = ?
    """, (id_libro,))   # Ojo: la coma convierte el valor en tupla (obligatorio con un solo parámetro)
    conexion.commit()
    print(f"Libro id={id_libro} eliminado.")


# ── 6. Buscar por autor ──────────────────────
def buscar_por_autor(autor):
    """Filtra los libros cuyo autor coincida (búsqueda exacta)."""
    cursor.execute("""
        SELECT * FROM libros
        WHERE autor = ?
    """, (autor,))
    registros = cursor.fetchall()

    print(f"\n─── Libros de '{autor}' ───")
    for registro in registros:
        print(f"  {registro['titulo']} ({registro['anio']})")
    print()


# ── Programa principal ───────────────────────
crear_tabla()

# Insertar datos de prueba
insertar_libro("Cien años de soledad", "Gabriel García Márquez", 1967)
insertar_libro("El principito",        "Antoine de Saint-Exupéry", 1943)
insertar_libro("1984",                 "George Orwell", 1949)
insertar_libro("Rayuela",              "Julio Cortázar", 1963)

# Mostrar todos
mostrar_libros()

# Marcar el libro con id=2 como prestado
cambiar_disponibilidad(2, 0)

# Volver a mostrar para ver el cambio
mostrar_libros()

# Buscar libros de un autor concreto
buscar_por_autor("George Orwell")

# Eliminar el libro con id=3
eliminar_libro(3)

# Listado final
mostrar_libros()

# ── Cerrar conexión ──────────────────────────
cursor.close()
conexion.close()
print("Conexión cerrada.")
