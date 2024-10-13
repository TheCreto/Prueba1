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
    def __init__(self, ctitular, ccantidad=0):
        titular = 'Error'
        cantidad = 0
        if isinstance(ctitular, Persona):
            titular = ctitular
        else:
            print('Error al crear instancia, el titular no es una persona')
        if ccantidad:
            try:
                cantidad = float(ccantidad)
            except ValueError:
                print('Error al introducir cantidad')

        self.titular = titular
        self.cantidad = cantidad

    def gettitular(self):
        return self.titular

    def getcantidad(self):
        return self.cantidad

    def settitular(self, ctitular):
        if isinstance(ctitular, Persona):
            self.titular = ctitular
        else:
            print('Error al cambiar de titular')

    def setcantidad(self):
        print('Para cambiar la cantidad utilice los métodos ingresar/retirar')

    def ingresar(self, cantidad):
        ingreso = 0
        try:
            ingreso = float(cantidad)
        except ValueError:
            print('Error al realizar ingreso')

        if ingreso >= 0:
            self.cantidad += ingreso
        else:
            print('Introduzca una cantidad positiva')

    def retirar(self, cantidad):
        retiro = 0
        try:
            retiro = float(cantidad)
        except ValueError:
            print('Error al realizar ingreso')

        if retiro >= 0:
            self.cantidad += -retiro
        else:
            print('Introduzca una cantidad positiva')
