import random

class Pokemon:
    def __init__(self, codigo, nombre, tipo1, tipo2, peso_min, peso_max, altura_min, altura_max):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.peso = random.uniform(peso_min, peso_max)
        self.altura = random.uniform(altura_min, altura_max)

    def mostrar(self):
        print("-----------------------------------------------------------")
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo1)
        if self.tipo2 is not None:
            print("Segundo tipo:", self.tipo2)
        print("Peso:", round(self.peso, 2), "kg")
        print("Altura:", round(self.altura, 2), "m")
        print("-----------------------------------------------------------")

# Crear objetos
pikachu   = Pokemon(12, "Pikachu",   "Eléctrico", "Ratón",   7,  15, 1, 3)
charizard = Pokemon(34, "Charizard", "Fuego",     "Dragón",  20, 50, 1, 3)
greninja  = Pokemon(50, "Greninja",  "Acuático",  None,      20, 40, 1, 3)

# Mostrar información
pikachu.mostrar()
charizard.mostrar()
greninja.mostrar()


class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.pokemons = []

    def agregar_pokemon(self, pokemon):
        if len(self.pokemons) < 3:
            self.pokemons.append(pokemon)
        else:
            print("El equipo ya tiene 3 Pokémon")

    def mostrar_equipo(self):
        print("------------------------------------------")
        print("Equipo:", self.nombre)
        print("Entrenador:", self.entrenador)
        print("Pokémon del equipo:")
        for p in self.pokemons:
            print(p.nombre)
        print("--------------------------------------------")


equipo1 = Equipo("Equipo de Pueblo Paleta", "Ash Ketchum")
equipo1.agregar_pokemon(pikachu)
equipo1.agregar_pokemon(charizard)
equipo1.agregar_pokemon(greninja)
equipo1.mostrar_equipo()