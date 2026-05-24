class Mascota:
    total_mascotas = 0

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self._edad = edad          # <-- guion bajo aquí
        Mascota.total_mascotas += 1

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = nueva_edad

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self._edad} años "


rex = Mascota("Rex", "Perro", 3)
print(rex)

class MascotaExotica(Mascota):

    def __init__(self, nombre, especie, edad, pais_origen):
        super().__init__(nombre,especie,edad)
        self.pais_origen = pais_origen

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self._edad} años | {self.pais_origen}"

    @staticmethod
    def requiere_permiso(especie):
        return especie in ("Serpiente", "Cocodrilo")


kiwi = MascotaExotica("Kiwi", "Loro", 5, "Brasil")
print(kiwi)

print(MascotaExotica.requiere_permiso("Serpiente"))
print(MascotaExotica.requiere_permiso("Perro"))

class Clinica:
    def __init__(self, nombre ):
        self.nombre = nombre
        self.mascotas = []


    def registrar(self,mascota):
        if len(self.mascotas) < 5:
            self.mascotas.append(mascota)
        else:
            print("La clínica está llena , máximo 5 mascotas")

    def listar(self):
        for mascota in self.mascotas:
            print(mascota)
            
clinica = Clinica("Clínica San Antón")
clinica.registrar(rex)
clinica.registrar(kiwi)
clinica.listar()