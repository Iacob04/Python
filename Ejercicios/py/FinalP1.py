import  csv
import random
class Pelicula:
    def __init__(self,id,titulo,director,duracion_min,duracion_max):
        self.id = id
        self.titulo = titulo
        self.director = director
        self.duracion_t = round(random.uniform(duracion_min,duracion_max),2)

    def to_dict(self):
        return {'id':self.id,'titulo':self.titulo,'director':self.director,'duracion_t':self.duracion_t
        }
    def __srt__(self):
        return f'{self.id}-{self.titulo}-{self.director}-{self.duracion_t}'
Pelicula1 =Pelicula(1,"The amazing-Spiderman","Andrew Garfield",40,200)
Pelicula2 = Pelicula(2,"Spiderman Home-Coming","Tom Holland",40,200)
Pelicula3 = Pelicula(3,"SPIDER-MAN","Tobey Maguayer",40,200)

campos=["id","titulo","director","duracion_t"]

with open("FinalP1.csv",'w',encoding="utf-8") as file:
    Escritor = csv.DictWriter(file,fieldnames=campos)
    Escritor.writeheader()
    Escritor.writerow(Pelicula1.to_dict())
    Escritor.writerow(Pelicula2.to_dict())
    Escritor.writerow(Pelicula3.to_dict())
print("Listar de forma bonita")
with open("FinalP1.csv",'r',encoding="utf-8") as file:
    Lector = csv.DictReader(file)
    for linea in Lector:
        print(linea["id"],"-",linea["titulo"],"-",linea["director"],"-",linea["duracion_t"])


