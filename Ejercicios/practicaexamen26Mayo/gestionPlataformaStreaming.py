from abc import ABC, abstractmethod

class Contenido(ABC):

    def __init__(self, titulo, valoracion):
        self._titulo = titulo
        self.valoracion = valoracion

    @property
    def valoracion(self):
        return self._valoracion

    @valoracion.setter
    def valoracion(self, valor):
        if valor <0 or valor >10:
            print("Valoración no valida")
        else:
            self._valoracion = valor

    @abstractmethod
    def __str__(self):
        pass


class Pelicula(Contenido):
    def __init__(self,titulo,valoracion, director, duracion_min):
        self._director = director
        self._duracion_min = duracion_min
        super().__init__(titulo, valoracion)


    def __str__(self):
        return f"{self._titulo} , {self._director} , ({self._duracion_min} minutos) , Valoración : {self._valoracion}"

class Serie(Contenido):
    def __init__(self,titulo,valoracion, temporadas, plataforma):
        self._temporadas = temporadas
        self._plataforma = plataforma
        super().__init__(titulo, valoracion)

    def __str__(self):
        return f"{self._titulo} , Temporadas : {self._temporadas} ,  Plataforma : {self._plataforma} , Valoración : {self._valoracion}"


Pelicula1 = Pelicula("Guardianes de La Galaxia", 10, "Alexandru", 120)
Pelicula1.valoracion = 15
print(Pelicula1)
Pelicula2 = Pelicula("Guardianes de La Galaxia", 10, "Alexandru", 120)
Pelicula2.valoracion = 8
print(Pelicula2)
Serie1 = Serie("StrangerThings", 9, 4, "Netflix")
print(Serie1)
