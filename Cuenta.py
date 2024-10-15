'''
Clase llamada cuenta

Atributos

titular (persona)
Cantidad (float)
El titular es obligatorio, la cantidad es opcional

metodos

Constructor donde la cantidad puede ser vacia
setters y getters
Atributo solo se puede modificar ingresando o retirando dinero

metodo str

ingresar(cantidad)
retirar(cantidad)
'''
from Persona import Persona


class Cuenta:
    def __init__(self, titular, cantidad=0):
        if not isinstance(titular, Persona) and not isinstance(cantidad, (int, float)):
            raise ValueError('Error al crear instancia')
        self.titular = titular
        self.cantidad = cantidad

    def getTitular(self):
        return self.titular

    def getCantidad(self):
        return self.cantidad

    def setTitular(self, titular):
        if not isinstance(titular, Persona):
            raise ValueError('Error al cambiar de titular')
        self.titular = titular


    def setCantidad(self):
        print('Para cambiar la cantidad utilice los métodos ingresar/retirar')

    def ingresar(self, ingreso):
        if not isinstance(ingreso, (int, float)):
            raise ValueError('Error al realizar ingreso')
        if ingreso <= 0:
            raise ValueError('Error al realizar ingreso, introduzca una cantidad positiva')
        self.cantidad += ingreso

    def retirar(self, retiro):
        if not isinstance(retiro, (int, float)):
            raise ValueError('Error al realizar el retiro')
        if retiro <= 0:
            raise ValueError('Error al realizar el retiro, introduzca una cantidad positiva.')
        self.cantidad += -retiro

