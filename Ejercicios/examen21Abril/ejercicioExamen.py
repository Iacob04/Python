import  csv

class Tripulante:
    def __init__(self, nombre, rango, planeta_origen, años_experiencia):
        self.nombre = nombre
        self.rango = rango
        self.planeta_origen = planeta_origen
        self.años_experiencia = años_experiencia

    def to_dict(self):
        return {'nombre':self.nombre,'rango':self.rango,'planeta_origen':self.planeta_origen,'años_experiencia':self.años_experiencia
        }
    def __srt__(self):
        return f'{self.nombre}-{self.rango}-{self.planeta_origen}-{self.años_experiencia}'

Tripulante1 = Tripulante("Zara Voss","Comandante","Kepler-22",12)
Tripulante2 = Tripulante("Rex Null","Ingeniero","Marte",7)
Tripulante3 = Tripulante("Lyra Shin","Médica","Tierra",5)
campos = ["nombre", "rango", "planeta_origen", "años_experiencia"]
with open("tripulacion.csv", 'w', encoding="utf-8") as file:

    Escritor = csv.DictWriter(file, fieldnames=campos)
    Escritor.writeheader()
    Escritor.writerow(Tripulante1.to_dict())
    Escritor.writerow(Tripulante2.to_dict())
    Escritor.writerow(Tripulante3.to_dict())

def agregar_tripulante(archivo,Tripulante):
    with open(archivo, 'a', encoding="utf-8")as file:
        Escritor = csv.DictWriter(file, fieldnames=campos)
        Escritor.writerow(Tripulante.to_dict())

Tripulante4 = Tripulante("Zar Voss","Comandante","Kepler-22",12)
Tripulante5 = Tripulante("Re Null","Ingeniero","Marte",7)
Tripulante6 = Tripulante("Lyr Shin","Médica","Tierra",5)

agregar_tripulante("tripulacion.csv",Tripulante4)
agregar_tripulante("tripulacion.csv",Tripulante5)
agregar_tripulante("tripulacion.csv",Tripulante6)

def cargar_tripulante(archivo):
    from pathlib import Path

    ruta = Path(archivo)

    if not ruta.exists():
        lista = []
        print(lista)

    else:
        with open(archivo, 'r', encoding="utf-8") as file:
            Lector = csv.DictReader(file)
            for linea in Lector:
                print(linea["nombre"], "-", linea["rango"], "-", linea["planeta_origen"], "-",
                      linea["años_experiencia"])



cargar_tripulante("tripulacion.csv")


