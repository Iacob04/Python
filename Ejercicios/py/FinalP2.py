#*
#
#
# Ejercicio — Gestor de Películas
# Crea una clase Pelicula con los atributos id, titulo, director y duracion. La duración se genera aleatoriamente entre un mínimo y máximo.
# Parte 1:
# Crea 3 películas con rangos de duración distintos
# Guárdalas en peliculas.csv
# Implementa __str__ y to_dict()
# Parte 2:
# Lee el CSV y reconstruye los objetos Pelicula en una lista
# Muestra todos los objetos con print()
#
# *#

import csv
import random


class PeliculaC:
    def __init__(self,id,titulo,director,duracion_min,duracion_max,duracion_t=None):
        self.id = id
        self.titulo = titulo
        self.director = director
        self.duracion_t= duracion_t if duracion_t else random.uniform(duracion_min,duracion_max)

    def to_dict(self):
        return {'id':self.id,'titulo':self.titulo,'director':self.director,'duracion_t':self.duracion_t
        }
    def __srt__(self):
        return f'{self.id}-{self.titulo}-{self.director}-{self.duracion_t}'

PeliculasB=[]
with open("FinalP1.csv","r",encoding="utf-8") as f:
    lector = csv.DictReader(f)

    for row in lector:
        Pelicula = PeliculaC(row["id"],row["titulo"],row["director"],0,0,row["duracion_t"])
        PeliculasB.append(Pelicula)
for Pelicula in PeliculasB:
    print(Pelicula.to_dict())
