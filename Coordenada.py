from copy import copy

"""
Crea una Clase con el siguiente diagrama UML

Atributos
- x: float
- y: float

Metodos
+ Coordenada(cx: float=0, cy: float = 0)
+ Coordenada(coord: Coordenada)
+ getX(): float
+ getY(): float
+ setX(cs: float): void
+ setY(cy: float): void
+ __str__(): str
"""


class Coordenada:
    def __init__(self, x=0, y=0):
        if isinstance(x, Coordenada):
            x, y = copy(x.getX()), copy(x.getY())
        elif not isinstance(x, (int, float) and not isinstance(y, (int, float))):
            raise ValueError('Error al crear la clase')
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError('Error al modificar x')
        self.__x = float(x)

    def setY(self, y):
        if not isinstance(y, (int, float)):
            self.__y = float(y)
        raise ValueError('Error al modificar y')

    def __str__(self):
        return f'({self.__x},{self.__y})'
