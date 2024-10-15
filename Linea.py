"""
Clase linea

Atributos
- cantidad: int
- precio: float
- descripcion: str

Metodos
+ Linea()
+ getSubtotal(): float
+ getCantidad(): int
+ getPrecio(): float
+ getDescripcion(): str
+ setCantidad(cant: int): void
+ setPrecio(precio: float): void
+ setDescripcion(desc: str): void
"""


class Linea:
    def __init__(self, cantidad, precio, descripcion):
        if not isinstance(cantidad, int):
            raise ValueError('Error al crear instancia, error al introducir al cantidad')
        elif not isinstance(precio, (int,float)):
            raise ValueError('Error al crear instancia, error al fijar el precio')
        elif not isinstance(descripcion, str):
            raise ValueError('Error al crear instancia, error de descripcion')

        self._cantidad = cantidad
        self._precio = precio
        self._descripcion = descripcion

    def getSubtotal(self):
        return self._cantidad * self._precio

    def getCantidad(self):
        return self._cantidad

    def getPrecio(self):
        return self._precio

    def getDescripcion(self):
        return self._descripcion

    def setCantidad(self, cantidad):
        if not isinstance(cantidad, int):
            raise ValueError('Error al cambiar la cantidad')
        self._cantidad = int(cantidad)
            

    def setPrecio(self, precio):
        if not isinstance(precio, float):
            raise ValueError('Error al cambiar de precio')
        self._precio = precio


    def setDescripcion(self, descripcion):
        if not isinstance(descripcion, str):
            raise ValueError('Error al cambiar descripcion')
        self._descripcion = descripcion
