
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.edad = edad

    @property
    def edad(self):
            return self._edad
    @edad.setter
    def edad(self, valor):
        if valor < 0:
                print("Edad no válida")
        else:
                self._edad = valor

    def __str__(self):
        pass

class Perro(Animal):
    def __init__(self, _nombre, edad, raza , vacunado):
        super().__init__(_nombre, edad)
        self.raza = raza
        self.vacunado = vacunado


    def __str__(self):
        estado = "vacunado" if self.vacunado else "sin vacunar"
        return f"{self._nombre} ({self.raza}), Edad: {self.edad}, {estado}"

Tobi = Perro("Tobi", 5, "Golden Retriever", False)
print(Tobi)


class Gato(Animal):
    def __init__(self, _nombre, edad, pelo_largo, numero_chip):
        super().__init__(_nombre, edad)
        self._pelo_largo = pelo_largo
        self._numero_chip = numero_chip

    def __str__(self):
        tipoPelo = "Pelo Largo " if self._pelo_largo else "Pelo Corto"
        return f"{self._nombre} ({tipoPelo}), Edad: {self.edad}, {self._numero_chip}"

Miau = Gato("Miau", 5, False, 1234)
Miau.edad = -3
print(Miau)
Miau.edad = 6
print(Miau)

#Meter objetos en lista y recorrerla
animales = [Tobi, Miau]

for animal in animales:
    print(animal)