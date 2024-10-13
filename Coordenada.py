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
    def __init__(self, cx=0, cy=0):
        x, y = 0, 0
        if isinstance(cx, Coordenada):
            x, y = copy(cx._x), copy(cx._y)
        else:
            try:
                x, y = float(cx), float(cy)
            except ValueError:
                print('Error al crear la clase')
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, cx):
        try:
            self._x = float(cx)
        except ValueError:
            print('Error al modificar x')

    def setY(self, cy):
        try:
            self._y = float(cy)
        except ValueError:
            print('Error al modificar y')

    def __str__(self):
        return f'({self._x},{self._y})'
