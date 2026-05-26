# =============================================================================
#  EJERCICIO POO (NIVEL DIFÍCIL) — SISTEMA DE FLOTA DE VEHÍCULOS DE ALQUILER
# =============================================================================
#  ENUNCIADO:
#
#  a) Crea una clase abstracta Vehiculo (con ABC) con un atributo protegido
#     _matricula y un atributo precio_dia (float). Define el getter y el setter
#     de precio_dia: el setter no permite valores negativos ni cero (si los
#     recibe, imprime "Precio no válido" y no cambia el valor). Declara un
#     método abstracto __str__ y un método abstracto coste_alquiler(dias).
#
#  b) Crea TRES subclases con atributos privados (doble guion bajo):
#     - Coche: añade num_puertas y tiene_gps (bool). coste_alquiler suma 5 €/día
#       extra si tiene GPS.
#     - Moto: añade cilindrada (int). coste_alquiler es el precio normal.
#     - Furgoneta: añade capacidad_carga (kg, float). coste_alquiler suma un 20%
#       al total si la carga supera los 1000 kg.
#     Cada subclase implementa su propio __str__ y su propio coste_alquiler(dias).
#
#  c) Crea un @classmethod flota_mas_cara(cls, lista) que reciba una lista de
#     vehículos y devuelva el de mayor precio_dia.
#
#  d) Crea un @staticmethod es_matricula_valida(matricula) que devuelva True si
#     la matrícula tiene exactamente 7 caracteres, y False si no.
#
#  e) Crea una segunda clase Cliente con nombre y una lista alquilados (vacía).
#     Método alquilar(vehiculo, dias) que use isinstance() para aplicar reglas:
#     un cliente no puede tener más de 2 furgonetas a la vez (aviso y no añade).
#     Si se puede, añade el vehículo e imprime el coste usando coste_alquiler.
#
#  f) En el principal: crea un vehículo de cada tipo, mételos en una lista,
#     recórrela imprimiendo cada uno con su coste para 3 días, llama al
#     @classmethod y al @staticmethod, y prueba alquilar forzando el límite.
# =============================================================================


# Importamos ABC (Abstract Base Class) y abstractmethod desde el módulo abc.
# ABC -> permite que una clase sea ABSTRACTA (no se pueden crear objetos de ella).
# abstractmethod -> marca un método como OBLIGATORIO de implementar en las hijas.
from abc import ABC, abstractmethod


# =============================================================================
#  APARTADO A — CLASE ABSTRACTA BASE
# =============================================================================

# "class Vehiculo(ABC)" -> Vehiculo hereda de ABC, por eso es abstracta.
# No podrás hacer Vehiculo(...) directamente: dará error. Solo sus hijas.
class Vehiculo(ABC):

    # Constructor: se ejecuta automáticamente al crear cada objeto hijo.
    # Recibe la matrícula y el precio por día.
    def __init__(self, matricula, precio_dia):
        # _matricula con UN guion bajo = atributo PROTEGIDO.
        # Convención: accesible desde las subclases, no se toca desde fuera.
        self._matricula = matricula
        # self.precio_dia = ... NO guarda directo: pasa por el SETTER de abajo,
        # porque precio_dia es una property. Así se valida ya al crear el objeto.
        self.precio_dia = precio_dia

    # ----- GETTER de precio_dia -----
    # @property convierte el método en un "atributo de solo lectura aparente".
    # Se usa como objeto.precio_dia (SIN paréntesis).
    @property
    def precio_dia(self):
        # Devuelve el valor interno real, guardado en _precio_dia.
        return self._precio_dia

    # ----- SETTER de precio_dia -----
    # @precio_dia.setter -> se ejecuta cuando haces objeto.precio_dia = valor.
    # OJO: necesita que ANTES exista la @property precio_dia (la de arriba).
    @precio_dia.setter
    def precio_dia(self, valor):
        # Regla de validación: ni negativo ni cero.
        if valor <= 0:
            # Si no es válido, avisamos y NO cambiamos nada.
            print("Precio no válido")
        else:
            # Si es válido, lo guardamos en el atributo interno _precio_dia.
            self._precio_dia = valor

    # ----- MÉTODO ABSTRACTO __str__ -----
    # @abstractmethod obliga a CADA subclase a escribir su propio __str__.
    # Si una hija no lo implementa, Python no deja crear objetos de esa hija.
    @abstractmethod
    def __str__(self):
        pass  # "pass" = no hace nada; el cuerpo real va en las hijas.

    # ----- MÉTODO ABSTRACTO coste_alquiler -----
    # También abstracto: cada vehículo calcula su coste de forma distinta.
    @abstractmethod
    def coste_alquiler(self, dias):
        pass

    # ----- APARTADO C — MÉTODO DE CLASE -----
    # @classmethod recibe "cls" (la clase) en vez de "self" (un objeto).
    # Sirve para operar sobre una COLECCIÓN de vehículos, no sobre uno solo.
    @classmethod
    def flota_mas_cara(cls, lista):
        # max() recorre la lista y devuelve el elemento mayor.
        # key=... le dice POR QUÉ comparar: aquí, por su precio_dia.
        # "lambda v: v.precio_dia" = función rápida que, dado un vehículo v,
        # devuelve su precio_dia para que max() compare por ese valor.
        return max(lista, key=lambda v: v.precio_dia)

    # ----- APARTADO D — MÉTODO ESTÁTICO -----
    # @staticmethod no recibe ni "self" ni "cls": es una función normal
    # que vive dentro de la clase. Útil para validaciones generales.
    @staticmethod
    def es_matricula_valida(matricula):
        # len(matricula) cuenta los caracteres. Devuelve True/False directamente.
        return len(matricula) == 7


# =============================================================================
#  APARTADO B — SUBCLASE COCHE
# =============================================================================

# "class Coche(Vehiculo)" -> Coche HEREDA de Vehiculo.
class Coche(Vehiculo):

    def __init__(self, matricula, precio_dia, num_puertas, tiene_gps):
        # super().__init__(...) llama al constructor del PADRE (Vehiculo)
        # para que inicialice _matricula y precio_dia (con su validación).
        super().__init__(matricula, precio_dia)
        # Atributos PRIVADOS (doble guion bajo __): propios solo de Coche.
        self.__num_puertas = num_puertas
        self.__tiene_gps = tiene_gps

    # __str__ propio: lo que se ve al hacer print(coche).
    def __str__(self):
        # Operador ternario: "Sí" si tiene_gps es True, "No" si es False.
        gps = "Sí" if self.__tiene_gps else "No"
        # f-string: el \n hace salto de línea entre cada dato.
        return (f"COCHE - Matrícula: {self._matricula}\n"
                f"  Precio/día: {self.precio_dia} €\n"
                f"  Puertas: {self.__num_puertas}\n"
                f"  GPS: {gps}")

    # coste_alquiler propio: precio base por días + extra de GPS.
    def coste_alquiler(self, dias):
        # Coste base: precio de un día multiplicado por los días.
        coste = self.precio_dia * dias
        # Si tiene GPS, sumamos 5 € por cada día.
        if self.__tiene_gps:
            coste += 5 * dias
        return coste


# =============================================================================
#  APARTADO B — SUBCLASE MOTO
# =============================================================================

class Moto(Vehiculo):

    def __init__(self, matricula, precio_dia, cilindrada):
        super().__init__(matricula, precio_dia)  # inicializa padre
        self.__cilindrada = cilindrada           # atributo privado propio

    def __str__(self):
        return (f"MOTO - Matrícula: {self._matricula}\n"
                f"  Precio/día: {self.precio_dia} €\n"
                f"  Cilindrada: {self.__cilindrada} cc")

    def coste_alquiler(self, dias):
        # La moto no tiene extras: precio por días y ya está.
        return self.precio_dia * dias


# =============================================================================
#  APARTADO B — SUBCLASE FURGONETA
# =============================================================================

class Furgoneta(Vehiculo):

    def __init__(self, matricula, precio_dia, capacidad_carga):
        super().__init__(matricula, precio_dia)        # inicializa padre
        self.__capacidad_carga = capacidad_carga       # privado propio

    def __str__(self):
        return (f"FURGONETA - Matrícula: {self._matricula}\n"
                f"  Precio/día: {self.precio_dia} €\n"
                f"  Capacidad de carga: {self.__capacidad_carga} kg")

    def coste_alquiler(self, dias):
        coste = self.precio_dia * dias  # coste base
        # Si la carga supera 1000 kg, recargo del 20% sobre el total.
        if self.__capacidad_carga > 1000:
            coste = coste * 1.20  # multiplicar por 1.20 = sumar el 20%
        return coste


# =============================================================================
#  APARTADO E — SEGUNDA CLASE: CLIENTE (se relaciona con Vehiculo)
# =============================================================================

# Cliente NO hereda de Vehiculo: es una clase aparte que USA vehículos.
class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre        # nombre del cliente
        self.alquilados = []        # lista vacía: aquí guardaremos sus vehículos

    def alquilar(self, vehiculo, dias):
        # Contamos cuántas FURGONETAS tiene ya este cliente.
        # [v for v in self.alquilados if isinstance(v, Furgoneta)] =
        #   recorre alquilados y se queda solo con las que son Furgoneta.
        # isinstance(v, Furgoneta) -> True si v es una Furgoneta.
        # len(...) cuenta cuántas hay.
        num_furgonetas = len([v for v in self.alquilados if isinstance(v, Furgoneta)])

        # REGLA: si el vehículo nuevo es furgoneta y ya tiene 2, no se permite.
        if isinstance(vehiculo, Furgoneta) and num_furgonetas >= 2:
            print(f"{self.nombre} no puede alquilar más de 2 furgonetas.")
            return  # "return" corta el método aquí: no añade nada.

        # Si pasa la regla, añadimos el vehículo a su lista.
        self.alquilados.append(vehiculo)
        # Calculamos el coste llamando al coste_alquiler del vehículo concreto.
        # Aquí ocurre el POLIMORFISMO: cada vehículo calcula su coste a su manera.
        coste = vehiculo.coste_alquiler(dias)
        # :.2f -> muestra el número con 2 decimales (ej. 105.00).
        print(f"{self.nombre} alquila {vehiculo._matricula} por {dias} días. Coste: {coste:.2f} €")


# =============================================================================
#  APARTADO F — PROGRAMA PRINCIPAL (pruebas)
# =============================================================================

# Creamos un vehículo de cada tipo.
coche1 = Coche("1234ABC", 40, 5, True)        # con GPS
moto1 = Moto("5678DEF", 25, 600)
furgo1 = Furgoneta("9012GHI", 60, 1500.0)     # carga > 1000 -> recargo

# Los metemos todos en una lista (puede mezclar tipos sin problema).
flota = [coche1, moto1, furgo1]

# Recorremos la lista e imprimimos cada vehículo con su coste para 3 días.
print("===== FLOTA COMPLETA =====")
for vehiculo in flota:
    print(vehiculo)  # llama al __str__ de cada uno (polimorfismo)
    # Mostramos su coste de alquiler para 3 días, con 2 decimales.
    print(f"  Coste 3 días: {vehiculo.coste_alquiler(3):.2f} €")
    print("-" * 30)

# APARTADO C: vehículo más caro de la flota.
print("\n===== APARTADO C =====")
caro = Vehiculo.flota_mas_cara(flota)  # se llama desde la clase
print(f"El más caro es: {caro._matricula} ({caro.precio_dia} €/día)")

# APARTADO D: validar matrículas (método estático).
print("\n===== APARTADO D =====")
print("¿'1234ABC' válida?", Vehiculo.es_matricula_valida("1234ABC"))  # 7 -> True
print("¿'123' válida?", Vehiculo.es_matricula_valida("123"))          # 3 -> False

# APARTADO E: probar el cliente y forzar el límite de furgonetas.
print("\n===== APARTADO E =====")
cliente1 = Cliente("Gabriel")
# Creamos 3 furgonetas para forzar el tope de 2.
f1 = Furgoneta("AAA1111", 60, 800.0)
f2 = Furgoneta("BBB2222", 70, 900.0)
f3 = Furgoneta("CCC3333", 80, 1200.0)
cliente1.alquilar(f1, 2)   # 1ª furgoneta -> OK
cliente1.alquilar(f2, 3)   # 2ª furgoneta -> OK
cliente1.alquilar(f3, 1)   # 3ª furgoneta -> debe rechazarla

# Probamos también el setter de precio (validación).
print("\n===== PRUEBA SETTER =====")
coche1.precio_dia = -10    # inválido -> "Precio no válido", no cambia
print("Precio tras intento inválido:", coche1.precio_dia)  # sigue siendo 40
coche1.precio_dia = 50     # válido -> cambia a 50
print("Precio tras intento válido:", coche1.precio_dia)