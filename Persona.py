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
    def __init__(self, pnombre='', pedad=0, pDNI=''):
        nombre, edad, DNI = '', 0, ''

        try:
            edad = int(pedad)
        except ValueError:
            print('Error al crear instancia')

        nombre, DNI = pnombre, pDNI

        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def getnombre(self):
        return self.nombre

    def getedad(self):
        return self.edad

    def getDNI(self):
        return self.DNI

    def setnombre(self, pnombre):
        self.nombre = pnombre

    def setedad(self, pedad):
        try:
            edad = int(pedad)
            self.edad = edad
        except ValueError:
            print('Error al introducir la edad')

    def setDNI(self, pDNI):
        self.DNI = pDNI

    def __str__(self):
        return f'Nombre: {self.getnombre()}, Edad: {self.getedad()}, DNI: {self.getDNI()}'

    def esMayorDeEdad(self):
        edad = self.getedad()
        if edad > 18:
            return True
        else:
            return False
