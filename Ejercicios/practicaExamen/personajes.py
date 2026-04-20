from abc import ABC, abstractmethod


class Personaje(ABC):
    """
    Clase abstracta base. Solo hereda lo que comparten TODOS: el nombre.
    El resto de atributos son distintos en cada subclase y no se heredan.
    """

    def __init__(self, nombre: str):
        self._nombre = nombre   # protegido (_) → accesible desde subclases

    # --- getter del nombre (heredado por todas las subclases) ---
    @property
    def nombre(self) -> str:
        return self._nombre

    # --- setter del nombre (heredado por todas las subclases) ---
    @nombre.setter
    def nombre(self, nuevo: str):
        if not nuevo.strip():
            print("El nombre no puede estar vacío.")
        else:
            self._nombre = nuevo

    # --- __str__ abstracto: cada hija DEBE redefinirlo ---
    @abstractmethod
    def __str__(self) -> str:
        pass

    # --- método de clase: lista cualquier colección de Personajes ---
    @classmethod
    def listar(cls, lista: list):
        # "\n\n".join(...) pone una línea en blanco entre cada personaje
        print("\n\n".join(str(p) for p in lista))


# ──────────────────────────────────────────────────────────────
# FUTBOLISTA
# Atributos propios (privados): dorsal, altura, equipo, edad
# ──────────────────────────────────────────────────────────────
class Futbolista(Personaje):

    def __init__(self, nombre: str, dorsal: int, altura: float,
                 equipo: str, edad: int):
        super().__init__(nombre)        # nombre lo gestiona la clase madre
        self.__dorsal = dorsal          # privado (__): solo accesible aquí
        self.__altura = altura
        self.__equipo = equipo
        self.__edad   = edad

    def __str__(self) -> str:
        return (f"Nombre: {self._nombre}\n"
                f"Altura: {self.__altura}\n"
                f"Equipo: {self.__equipo}\n"
                f"Edad: {self.__edad} años\n"
                f"Dorsal habitual: {self.__dorsal}")


# ──────────────────────────────────────────────────────────────
# PERSONAJE DE ANIME
# Atributos propios (privados): anime, mangaka
# ──────────────────────────────────────────────────────────────
class PersonajeAnime(Personaje):

    def __init__(self, nombre: str, anime: str, mangaka: str):
        super().__init__(nombre)
        self.__anime   = anime
        self.__mangaka = mangaka

    def __str__(self) -> str:
        return (f"Nombre: {self._nombre}\n"
                f"Anime: {self.__anime}\n"
                f"Mangaka: {self.__mangaka}")


# ──────────────────────────────────────────────────────────────
# SUPERHEROE
# nombre = identidad secreta (Peter Parker), privados: superheroe, editorial
# ──────────────────────────────────────────────────────────────
class Superheroe(Personaje):

    def __init__(self, nombre: str, superheroe: str, editorial: str):
        super().__init__(nombre)
        self.__superheroe = superheroe
        self.__editorial  = editorial

    def __str__(self) -> str:
        return (f"Nombre: {self._nombre}\n"
                f"Superheroe: {self.__superheroe}\n"
                f"Editorial: {self.__editorial}")


# ══════════════════════════════════════════════════════════════
# PRUEBAS
# ══════════════════════════════════════════════════════════════

# 1. Crear los tres objetos del enunciado
futbolista1 = Futbolista("Lamine Yamal", 19, 1.79, "Futbol Club Barcelona", 18)
personaje1  = PersonajeAnime("Shinji Ikari", "Neon Genesis Evangelion", "Yoshiyuki Sadamoto")
superheroe1 = Superheroe("Peter Parker", "Spiderman", "Marvel")

# 2. Probar print individual (llama a __str__ de cada clase)
print("=== print individual ===")
print(futbolista1)
print()
print(personaje1)
print()
print(superheroe1)

# 3. Probar getter y setter del nombre (definidos una sola vez en Personaje)
print("\n=== getter / setter ===")
print(futbolista1.nombre)          # getter → "Lamine Yamal"
futbolista1.nombre = "Lamine"      # setter → cambia el nombre
print(futbolista1.nombre)          # getter → "Lamine"
futbolista1.nombre = ""            # setter → "El nombre no puede estar vacío."
print(futbolista1.nombre)          # sigue siendo "Lamine"

# 4. Probar el método de clase listar()
print("\n=== listar() ===")
lista = [futbolista1, personaje1, superheroe1]
Personaje.listar(lista)
