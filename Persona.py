"""
Vamos a crear la clase persona
Atributos

nombre
edad
DNI

Metodos

Constructor donde los datos puedan estar vacios

setters y getters de cada atributo

Método __str__()
esMayorDeEdad():bool
"""


class Persona:
    def __init__(self, nombre='', edad=0, DNI=''):
        if not isinstance(nombre, str) and not isinstance(edad, int) and not isinstance(DNI, str):
            raise ValueError('Error al crear instancia')
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def getnombre(self):
        return self.nombre

    def getedad(self):
        return self.edad

    def getDNI(self):
        return self.DNI

    def setnombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError('Error al cambiar de nombre')
        self.nombre = nombre

    def setedad(self, edad):
        if not isinstance(edad, int):
            raise ValueError('Error al cambiar la edad')
        self.edad = edad

    def setDNI(self, DNI):
        if not isinstance(DNI, str):
            raise ValueError('Error al cambiar de DNI')
        self.DNI = DNI

    def __str__(self):
        return f'Nombre: {self.getnombre()}, Edad: {self.getedad()}, DNI: {self.getDNI()}'

    def esMayorDeEdad(self):
        edad = self.getedad()
        if edad > 18:
            return True
        else:
            return False
