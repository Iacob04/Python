from abc import ABC, abstractmethod


# ─────────────────────────────────────────────
# APARTADO A - Clase abstracta base
# ─────────────────────────────────────────────

class ElementoMultimedia(ABC):
    """Clase abstracta base para todos los elementos del catálogo.
    Solo contiene el atributo 'titulo', que es común a todas las subclases."""

    def __init__(self, titulo: str):
        # Atributo protegido: accesible desde subclases pero no desde fuera directamente
        self._titulo = titulo

    # ─────────────────────────────────────────
    # APARTADO C - Getter y setter del título
    # Declarados aquí para no repetirlos en cada subclase
    # ─────────────────────────────────────────

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self._titulo = nuevo_titulo

    # ─────────────────────────────────────────
    # APARTADO D - __str__ abstracto
    # Obliga a cada subclase a definir su propia representación
    # ─────────────────────────────────────────

    @abstractmethod
    def __str__(self) -> str:
        pass

    # ─────────────────────────────────────────
    # APARTADO E - Escritura a CSV (método de clase)
    # Recibe una lista de ElementoMultimedia y la guarda en catalogo.csv
    # ─────────────────────────────────────────

    @classmethod
    def guardar_csv(cls, elementos: list):
        with open("catalogo.csv", "w", encoding="utf-8") as f:
            for elemento in elementos:
                f.write(elemento.a_csv() + "\n")

    # ─────────────────────────────────────────
    # APARTADO F - Lectura desde CSV (método estático)
    # Lee catalogo.csv y reconstruye la lista de objetos
    # ─────────────────────────────────────────

    @staticmethod
    def leer_csv() -> list:
        elementos = []
        with open("catalogo.csv", "r", encoding="utf-8") as f:
            for linea in f:
                # Eliminar salto de línea y separar por ";"
                campos = linea.strip().split(";")
                tipo = campos[0]

                if tipo == "Videojuego":
                    # campos: Videojuego;titulo;genero;plataforma;desarrolladora;año
                    elementos.append(Videojuego(campos[1], campos[2], campos[3], campos[4], int(campos[5])))
                elif tipo == "Serie":
                    # campos: Serie;titulo;temporadas;plataforma;pais
                    elementos.append(Serie(campos[1], int(campos[2]), campos[3], campos[4]))
                elif tipo == "Libro":
                    # campos: Libro;titulo;autor;genero;año;paginas
                    elementos.append(Libro(campos[1], campos[2], campos[3], int(campos[4]), int(campos[5])))

        return elementos

    # Método auxiliar que cada subclase implementa para formatear su línea CSV
    @abstractmethod
    def a_csv(self) -> str:
        pass


# ─────────────────────────────────────────────
# APARTADO A - Subclase Videojuego
# ─────────────────────────────────────────────

class Videojuego(ElementoMultimedia):

    def __init__(self, titulo: str, genero: str, plataforma: str, desarrolladora: str, año: int):
        super().__init__(titulo)            # Hereda _titulo de la clase madre
        self.__genero       = genero        # Privado
        self.__plataforma   = plataforma    # Privado
        self.__desarrolladora = desarrolladora  # Privado
        self.__año          = año           # Privado

    # APARTADO D
    def __str__(self) -> str:
        return (f"Título: {self._titulo}\n"
                f"Género: {self.__genero}\n"
                f"Plataforma: {self.__plataforma}\n"
                f"Desarrolladora: {self.__desarrolladora}\n"
                f"Año: {self.__año}")

    # APARTADO E - línea CSV de este elemento
    def a_csv(self) -> str:
        return f"Videojuego;{self._titulo};{self.__genero};{self.__plataforma};{self.__desarrolladora};{self.__año}"


# ─────────────────────────────────────────────
# APARTADO A - Subclase Serie
# ─────────────────────────────────────────────

class Serie(ElementoMultimedia):

    def __init__(self, titulo: str, temporadas: int, plataforma: str, pais: str):
        super().__init__(titulo)
        self.__temporadas = temporadas  # Privado
        self.__plataforma = plataforma  # Privado
        self.__pais       = pais        # Privado

    # APARTADO D
    def __str__(self) -> str:
        return (f"Título: {self._titulo}\n"
                f"Temporadas: {self.__temporadas}\n"
                f"Plataforma: {self.__plataforma}\n"
                f"País: {self.__pais}")

    # APARTADO E
    def a_csv(self) -> str:
        return f"Serie;{self._titulo};{self.__temporadas};{self.__plataforma};{self.__pais}"


# ─────────────────────────────────────────────
# APARTADO A - Subclase Libro
# ─────────────────────────────────────────────

class Libro(ElementoMultimedia):

    def __init__(self, titulo: str, autor: str, genero: str, año: int, paginas: int):
        super().__init__(titulo)
        self.__autor   = autor    # Privado
        self.__genero  = genero   # Privado
        self.__año     = año      # Privado
        self.__paginas = paginas  # Privado

    # APARTADO D
    def __str__(self) -> str:
        return (f"Título: {self._titulo}\n"
                f"Autor: {self.__autor}\n"
                f"Género: {self.__genero}\n"
                f"Año: {self.__año}\n"
                f"Páginas: {self.__paginas}")

    # APARTADO E
    def a_csv(self) -> str:
        return f"Libro;{self._titulo};{self.__autor};{self.__genero};{self.__año};{self.__paginas}"


# ─────────────────────────────────────────────
# APARTADO B - Instancias de ejemplo
# ─────────────────────────────────────────────

videojuego1 = Videojuego("The Legend of Zelda: Breath of the Wild", "Aventura", "Nintendo Switch", "Nintendo", 2017)
serie1      = Serie("Breaking Bad", 5, "Netflix", "Estados Unidos")
libro1      = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía épica", 1954, 1200)

print("── APARTADO B ──────────────────────────")
print(videojuego1)
print()
print(serie1)
print()
print(libro1)

# ─────────────────────────────────────────────
# APARTADO C - Prueba getter y setter del título
# ─────────────────────────────────────────────

print("\n── APARTADO C ──────────────────────────")
print("Título original:", serie1.titulo)
serie1.titulo = "Breaking Bad (Edición Completa)"
print("Título modificado:", serie1.titulo)
serie1.titulo = "Breaking Bad"  # Restauramos para los siguientes apartados

# ─────────────────────────────────────────────
# APARTADO E - Guardar en CSV
# ─────────────────────────────────────────────

catalogo = [videojuego1, serie1, libro1]
ElementoMultimedia.guardar_csv(catalogo)
print("\n── APARTADO E ──────────────────────────")
print("Catálogo guardado en catalogo.csv")

# ─────────────────────────────────────────────
# APARTADO F - Leer desde CSV e imprimir
# ─────────────────────────────────────────────

print("\n── APARTADO F ──────────────────────────")
elementos_leidos = ElementoMultimedia.leer_csv()
for elemento in elementos_leidos:
    print(elemento)
    print()
