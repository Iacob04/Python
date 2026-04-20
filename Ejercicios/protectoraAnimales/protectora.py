# Listas globales que almacenan animales y clientes pendientes de adopción
animales_sin_adoptar = []
clientes_sin_adoptar = []


class Animal:
    # Clase base para todos los animales de la protectora
    def __init__(self, nacimiento, nombre=None):
        self.nacimiento = nacimiento
        self.nombre = nombre
        # Al crear un animal se registra automáticamente como disponible
        animales_sin_adoptar.append(self)

    def mostrar_nombre(self):
        return self.nombre


class Perro(Animal):
    # Límite de adopción: máximo 2 perros por cliente
    def __init__(self, nacimiento, vacunado, nombre=None):
        super().__init__(nacimiento, nombre)
        self.vacunado = vacunado


class Gato(Animal):
    # Límite de adopción: máximo 3 gatos por cliente
    def __init__(self, nacimiento, vacunado, nombre=None):
        super().__init__(nacimiento, nombre)
        self.vacunado = vacunado


class Tortuga(Animal):
    # Las tortugas no requieren vacunas; límite: 1 por cliente
    def __init__(self, nacimiento, nombre=None):
        super().__init__(nacimiento, nombre)


class Cliente:
    def __init__(self, nombre, apellido, edad, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.adoptados = []  # lista independiente por cliente
        clientes_sin_adoptar.append(self)

    def adoptar(self, animal):
        # Comprobaciones de límites antes de permitir la adopción
        if len(self.adoptados) >= 4:
            print(f"{self.nombre} no puede adoptar más animales (máximo 4)")
        elif isinstance(animal, Perro) and len([a for a in self.adoptados if isinstance(a, Perro)]) >= 2:
            # [a for a in self.adoptados if isinstance(a, Perro)] filtra solo perros ya adoptados
            print(f"{self.nombre} no puede adoptar más perros (máximo 2)")
        elif isinstance(animal, Gato) and len([a for a in self.adoptados if isinstance(a, Gato)]) >= 3:
            print(f"{self.nombre} no puede adoptar más gatos (máximo 3)")
        elif isinstance(animal, Tortuga) and len([a for a in self.adoptados if isinstance(a, Tortuga)]) >= 1:
            print(f"{self.nombre} no puede adoptar más tortugas (máximo 1)")
        else:
            self.adoptados.append(animal)
            animales_sin_adoptar.remove(animal)
            # El cliente deja de estar en la lista de sin adoptar tras su primera adopción
            if self in clientes_sin_adoptar:
                clientes_sin_adoptar.remove(self)
            print(f"{animal.mostrar_nombre()} fue adoptado por {self.nombre}")

    def mostrar_adoptados(self):
        if not self.adoptados:
            print(f"|||| {self.nombre} no adoptó ningún animal ||||")
        else:
            print(f"El cliente {self.nombre} tiene adoptados a:")
            for a in self.adoptados:
                print(f"  - {a.nombre}")


def mostrar_animales_sin_adoptar():
    print("--- Animales disponibles para adopción ---")
    for a in animales_sin_adoptar:
        print(f"  · {a.nombre}")


def mostrar_clientes_sin_adoptar():
    print("=== Clientes que aún no adoptaron ===")
    for c in clientes_sin_adoptar:
        print(f"  · {c.nombre}")


# --- Creación de objetos de prueba ---
tobi = Perro(2000, False, "Tobi")
zeus = Perro(2003, True, "Zeus")
garfield = Gato(2005, True, "Garfield")

kevin = Cliente("Kevin", "García", 25, "644444222")
david = Cliente("David", "Mejía", 22, "633333332")

kevin.adoptar(tobi)
kevin.adoptar(zeus)

kevin.mostrar_adoptados()
david.mostrar_adoptados()

mostrar_animales_sin_adoptar()
mostrar_clientes_sin_adoptar()
