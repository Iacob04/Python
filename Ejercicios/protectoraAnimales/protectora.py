# Listas globales que almacenan animales y adoptantes pendientes
animales_disponibles = []
adoptantes_pendientes = []


class Animal:
    # Clase base para todos los animales del refugio
    def __init__(self, anyo_nacimiento, nombre=None):
        self.anyo_nacimiento = anyo_nacimiento
        self.nombre = nombre
        # Al registrar un animal queda automáticamente como disponible
        animales_disponibles.append(self)

    def obtener_nombre(self):
        return self.nombre


class Perro(Animal):
    # Límite de adopción: máximo 2 perros por adoptante
    def __init__(self, anyo_nacimiento, esta_vacunado, nombre=None):
        super().__init__(anyo_nacimiento, nombre)
        self.esta_vacunado = esta_vacunado


class Gato(Animal):
    # Límite de adopción: máximo 3 gatos por adoptante
    def __init__(self, anyo_nacimiento, esta_vacunado, nombre=None):
        super().__init__(anyo_nacimiento, nombre)
        self.esta_vacunado = esta_vacunado


class Tortuga(Animal):
    # Las tortugas no necesitan vacunas; límite: 1 por adoptante
    def __init__(self, anyo_nacimiento, nombre=None):
        super().__init__(anyo_nacimiento, nombre)


class Adoptante:
    def __init__(self, nombre, apellido, edad, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.animales_adoptados = []  # lista propia de cada adoptante
        adoptantes_pendientes.append(self)

    def realizar_adopcion(self, animal):
        # Comprobaciones de límites antes de permitir la adopción
        if len(self.animales_adoptados) >= 4:
            print(f"{self.nombre} no puede adoptar más animales (máximo 4)")
        elif isinstance(animal, Perro) and len([a for a in self.animales_adoptados if isinstance(a, Perro)]) >= 2:
            # [a for a in self.animales_adoptados if isinstance(a, Perro)] filtra solo perros ya adoptados
            print(f"{self.nombre} no puede adoptar más perros (máximo 2)")
        elif isinstance(animal, Gato) and len([a for a in self.animales_adoptados if isinstance(a, Gato)]) >= 3:
            print(f"{self.nombre} no puede adoptar más gatos (máximo 3)")
        elif isinstance(animal, Tortuga) and len([a for a in self.animales_adoptados if isinstance(a, Tortuga)]) >= 1:
            print(f"{self.nombre} no puede adoptar más tortugas (máximo 1)")
        else:
            self.animales_adoptados.append(animal)
            animales_disponibles.remove(animal)
            # El adoptante sale de la lista de pendientes tras su primera adopción
            if self in adoptantes_pendientes:
                adoptantes_pendientes.remove(self)
            print(f"{animal.obtener_nombre()} ha sido adoptado por {self.nombre}")

    def listar_adoptados(self):
        if not self.animales_adoptados:
            print(f"|||| {self.nombre} todavía no ha adoptado ningún animal ||||")
        else:
            print(f"El adoptante {self.nombre} tiene a su cargo:")
            for a in self.animales_adoptados:
                print(f"  - {a.nombre}")


def listar_animales_disponibles():
    print("--- Animales disponibles en el refugio ---")
    for a in animales_disponibles:
        print(f"  · {a.nombre}")


def listar_adoptantes_pendientes():
    print("=== Adoptantes sin animales aún ===")
    for c in adoptantes_pendientes:
        print(f"  · {c.nombre}")


# --- Creación de objetos de prueba ---
rocky = Perro(2001, True, "Rocky")
boby = Perro(2004, False, "Boby")
luna = Gato(2007, True, "Luna")

alejandro = Adoptante("Alejandro", "Iacob", 21, "611222333")
sara = Adoptante("Sara", "Molina", 24, "699887766")

alejandro.realizar_adopcion(rocky)
alejandro.realizar_adopcion(boby)

alejandro.listar_adoptados()
sara.listar_adoptados()

listar_animales_disponibles()
listar_adoptantes_pendientes()
