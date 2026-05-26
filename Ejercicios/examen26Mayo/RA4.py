class Tripulante:
    def __init__(self, nombre, rango, planeta_origen,anios_experiencia):
        self._nombre = nombre
        self.rango = rango
        self._planeta_origen = planeta_origen
        self.anios_experiencia = anios_experiencia

    def __str__(self):
        return f"({self.rango}) - {self._nombre} , origen: {self._planeta_origen}, tiempo en el cuerpo: {self.anios_experiencia} años"



class Nave:
    def __init__(self, nombre):
        self._nombre = nombre
        self.tripulantes = []

    def agregar_tripulante(self,tripulante):
        self.tripulantes.append(tripulante)

    def __str__(self):

       for tripulante in self.tripulantes:

             return (f" Tripulantes: "
                     f"{tripulante.__str__()}")




Zara = Tripulante("Zara Voss", "Comandante", "Kepler-22b", 12)
#print(Zara)
Rex = Tripulante("Rex NUll", "Ingeniero", "Marte", 7)
#print(Rex)
Lyra = Tripulante("Lyra Shin", "Médica", "Tierra", 5)
#print(Lyra)


Apolo99 = Nave("Apolo99")
Apolo99.agregar_tripulante(Zara)
Apolo99.agregar_tripulante(Lyra)
Apolo99.agregar_tripulante(Rex)
print(Apolo99)


#Parte 1
#1
# La principar diferencia es que los atributos de instancia utiliza los objetos para sobree escribirlo y los atributos de clase sirven para crear dichos objetos
#2
# El método __str__ sirve para definir qué se muestra al hacer print(objeto)


