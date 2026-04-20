# =============================================================
#  APUNTES EXAMEN — CLASES Y OBJETOS
# =============================================================
# ÍNDICE:
#   1. Estructura básica de una clase
#   2. El constructor __init__
#   3. Métodos de instancia
#   4. __str__  (equivalente al toString de Java)
#   5. @property y @setter  (atributos protegidos)
#   6. @staticmethod  (métodos de clase, no de objeto)
#   7. Crear objetos (instanciar)
# =============================================================


# ─────────────────────────────────────────────────────────────
# 1 · ESTRUCTURA BÁSICA
# ─────────────────────────────────────────────────────────────
# class NombreClase:          ← siempre en PascalCase
#     def __init__(self, ...):
#         self.atributo = ...
#
# "self" es la referencia al propio objeto (como "this" en Java)


# ─────────────────────────────────────────────────────────────
# 2 · CONSTRUCTOR  __init__
# ─────────────────────────────────────────────────────────────
class Pokemon:
    # Se ejecuta automáticamente al crear el objeto
    def __init__(self, nombre, tipo, nivel=1):  # nivel=1 → parámetro con valor por defecto
        self.nombre = nombre   # atributo público
        self.tipo   = tipo
        self.nivel  = nivel
        self.vida   = nivel * 10   # atributo calculado en el constructor


# ─────────────────────────────────────────────────────────────
# 3 · MÉTODOS DE INSTANCIA
# ─────────────────────────────────────────────────────────────
# Son funciones dentro de la clase. Siempre reciben "self" primero.
class Pokemon:
    def __init__(self, nombre, tipo, nivel=1):
        self.nombre = nombre
        self.tipo   = tipo
        self.nivel  = nivel
        self.vida   = nivel * 10

    def subir_nivel(self):
        self.nivel += 1
        self.vida  += 10
        print(f"{self.nombre} subió al nivel {self.nivel}!")

    def atacar(self, objetivo):
        # "objetivo" es otro objeto Pokemon
        dano = self.nivel * 2
        objetivo.vida -= dano
        print(f"{self.nombre} atacó a {objetivo.nombre} y le quitó {dano} de vida.")


# ─────────────────────────────────────────────────────────────
# 4 · __str__  →  lo que se imprime al hacer print(objeto)
# ─────────────────────────────────────────────────────────────
class Pokemon:
    def __init__(self, nombre, tipo, nivel=1):
        self.nombre = nombre
        self.tipo   = tipo
        self.nivel  = nivel
        self.vida   = nivel * 10

    def subir_nivel(self):
        self.nivel += 1
        self.vida  += 10

    def atacar(self, objetivo):
        dano = self.nivel * 2
        objetivo.vida -= dano
        print(f"{self.nombre} atacó a {objetivo.nombre} y le quitó {dano} de vida.")

    def __str__(self):
        # Siempre devuelve un string (return, no print)
        return f"Pokemon({self.nombre}, tipo={self.tipo}, nivel={self.nivel}, vida={self.vida})"


# ─────────────────────────────────────────────────────────────
# 5 · @property y @setter  →  atributos "protegidos"
# ─────────────────────────────────────────────────────────────
# Convención: _ delante del nombre → atributo protegido (no tocar desde fuera)
# @property  → getter (leer el valor)
# @xxx.setter → setter (modificar el valor con control)

class Entrenador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad  = edad    # _ indica que es protegido

    @property
    def edad(self):
        return self._edad     # se accede como si fuera un atributo normal

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            print("La edad no puede ser negativa.")
        else:
            self._edad = nueva_edad


# ─────────────────────────────────────────────────────────────
# 6 · @staticmethod  →  método que NO necesita "self"
# ─────────────────────────────────────────────────────────────
# Se llama con  NombreClase.metodo()  sin crear objeto
class Pokemon:
    def __init__(self, nombre, tipo, nivel=1):
        self.nombre = nombre
        self.tipo   = tipo
        self.nivel  = nivel
        self.vida   = nivel * 10

    def subir_nivel(self):
        self.nivel += 1
        self.vida  += 10

    def atacar(self, objetivo):
        dano = self.nivel * 2
        objetivo.vida -= dano
        print(f"{self.nombre} atacó a {objetivo.nombre} y le quitó {dano} de vida.")

    def __str__(self):
        return f"Pokemon({self.nombre}, tipo={self.tipo}, nivel={self.nivel}, vida={self.vida})"

    @staticmethod
    def descripcion():
        return "Los Pokemon son criaturas con habilidades especiales."


# ─────────────────────────────────────────────────────────────
# 7 · CREAR OBJETOS (instanciar)
# ─────────────────────────────────────────────────────────────
pikachu   = Pokemon("Pikachu",   "Eléctrico", nivel=5)
charmander = Pokemon("Charmander", "Fuego",    nivel=3)

print(pikachu)           # llama a __str__
pikachu.subir_nivel()
pikachu.atacar(charmander)
print(f"Vida de Charmander: {charmander.vida}")

# Método estático → sin crear objeto
print(Pokemon.descripcion())

# Property
ash = Entrenador("Ash", 10)
print(ash.edad)     # getter → imprime 10
ash.edad = -5       # setter → "La edad no puede ser negativa."
ash.edad = 11       # setter → asigna 11
print(ash.edad)     # imprime 11
