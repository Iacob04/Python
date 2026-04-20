# =============================================================
#  APUNTES EXAMEN — HERENCIA
# =============================================================
# ÍNDICE:
#   1. Qué es la herencia
#   2. super().__init__()  →  llamar al constructor del padre
#   3. Sobreescribir métodos (override)
#   4. isinstance()  →  comprobar el tipo de un objeto
#   5. Ejemplo completo: Animal → Perro / Gato / Tortuga
# =============================================================


# ─────────────────────────────────────────────────────────────
# 1 · QUÉ ES LA HERENCIA
# ─────────────────────────────────────────────────────────────
# class Hija(Padre):   ← la clase Hija hereda todo lo de Padre
#
# La hija tiene:
#   · Todos los atributos del padre
#   · Todos los métodos del padre
#   · Puede añadir atributos/métodos propios
#   · Puede sobreescribir métodos del padre


# ─────────────────────────────────────────────────────────────
# 2 · super().__init__()
# ─────────────────────────────────────────────────────────────
# Cuando la hija tiene su propio __init__, DEBE llamar al padre
# con super().__init__(...) para que los atributos del padre
# también se inicialicen.

class Animal:
    def __init__(self, nombre, nacimiento):
        self.nombre     = nombre
        self.nacimiento = nacimiento

    def presentarse(self):
        print(f"Soy {self.nombre}, nacido en {self.nacimiento}")

    def __str__(self):
        return f"Animal({self.nombre})"


class Perro(Animal):
    def __init__(self, nombre, nacimiento, vacunado):
        super().__init__(nombre, nacimiento)  # inicializa nombre y nacimiento del padre
        self.vacunado = vacunado              # atributo propio de Perro


class Gato(Animal):
    def __init__(self, nombre, nacimiento, vacunado):
        super().__init__(nombre, nacimiento)
        self.vacunado = vacunado


class Tortuga(Animal):
    # Tortuga no tiene vacunas → no añade atributos nuevos
    def __init__(self, nombre, nacimiento):
        super().__init__(nombre, nacimiento)


# ─────────────────────────────────────────────────────────────
# 3 · SOBREESCRIBIR MÉTODOS (override)
# ─────────────────────────────────────────────────────────────
# La hija puede redefinir un método del padre para cambiar su comportamiento.

class Perro(Animal):
    def __init__(self, nombre, nacimiento, vacunado):
        super().__init__(nombre, nacimiento)
        self.vacunado = vacunado

    # Sobreescribimos __str__ del padre
    def __str__(self):
        estado = "vacunado" if self.vacunado else "sin vacunar"
        return f"Perro({self.nombre}, {estado})"

    # Método propio que no tiene Animal
    def ladrar(self):
        print(f"{self.nombre}: ¡Guau!")


# ─────────────────────────────────────────────────────────────
# 4 · isinstance()  →  comprobar si un objeto es de cierta clase
# ─────────────────────────────────────────────────────────────
# isinstance(objeto, Clase)  →  True / False
#
# MUY ÚTIL en adoptar() para poner límites por tipo de animal:
#   if isinstance(animal, Perro) and cantidad_perros >= 2:
#       print("No puedes adoptar más perros")

tobi = Perro("Tobi", 2020, True)

print(isinstance(tobi, Perro))   # True
print(isinstance(tobi, Animal))  # True  ← también es Animal por herencia
print(isinstance(tobi, Gato))    # False


# ─────────────────────────────────────────────────────────────
# 5 · EJEMPLO COMPLETO: protectora de animales
# ─────────────────────────────────────────────────────────────

animales_sin_adoptar = []
clientes_sin_adoptar = []


class Animal:
    def __init__(self, nombre, nacimiento):
        self.nombre     = nombre
        self.nacimiento = nacimiento
        animales_sin_adoptar.append(self)  # se registra solo al crearse

    def __str__(self):
        return f"Animal({self.nombre})"


class Perro(Animal):
    def __init__(self, nombre, nacimiento, vacunado):
        super().__init__(nombre, nacimiento)
        self.vacunado = vacunado


class Gato(Animal):
    def __init__(self, nombre, nacimiento, vacunado):
        super().__init__(nombre, nacimiento)
        self.vacunado = vacunado


class Tortuga(Animal):
    def __init__(self, nombre, nacimiento):
        super().__init__(nombre, nacimiento)


class Cliente:
    def __init__(self, nombre, apellido):
        self.nombre    = nombre
        self.apellido  = apellido
        self.adoptados = []                # lista independiente por cliente
        clientes_sin_adoptar.append(self)

    def adoptar(self, animal):
        # Contamos cuántos de cada tipo ya tiene el cliente
        # [a for a in lista if condicion]  →  filtra la lista y cuenta
        num_perros   = len([a for a in self.adoptados if isinstance(a, Perro)])
        num_gatos    = len([a for a in self.adoptados if isinstance(a, Gato)])
        num_tortugas = len([a for a in self.adoptados if isinstance(a, Tortuga)])

        if len(self.adoptados) >= 4:
            print("Máximo 4 animales en total.")
        elif isinstance(animal, Perro) and num_perros >= 2:
            print("Máximo 2 perros.")
        elif isinstance(animal, Gato) and num_gatos >= 3:
            print("Máximo 3 gatos.")
        elif isinstance(animal, Tortuga) and num_tortugas >= 1:
            print("Máximo 1 tortuga.")
        else:
            self.adoptados.append(animal)
            animales_sin_adoptar.remove(animal)
            if self in clientes_sin_adoptar:
                clientes_sin_adoptar.remove(self)
            print(f"{animal.nombre} adoptado por {self.nombre}.")

    def mostrar_adoptados(self):
        if not self.adoptados:
            print(f"{self.nombre} no ha adoptado ningún animal.")
        else:
            print(f"{self.nombre} tiene: {[a.nombre for a in self.adoptados]}")


# --- Prueba ---
tobi      = Perro("Tobi", 2020, True)
garfield  = Gato("Garfield", 2019, False)
franklin  = Tortuga("Franklin", 2018)

ana = Cliente("Ana", "López")
ana.adoptar(tobi)
ana.adoptar(garfield)
ana.adoptar(franklin)
ana.mostrar_adoptados()
