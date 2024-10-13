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
    def __init__(self, ccantidad, cprecio, cdescripcion):
        cantidad, precio, descripcion = 0, 0, ''
        try:
            cantidad = int(ccantidad)
            precio = float(cprecio)
            descripcion = str(cdescripcion)
        except ValueError:
            print('Error al crear instancia')

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
        if isinstance(cantidad, int):
            self._cantidad = int(cantidad)
        else:
            print('Error al cambiar la cantidad')

    def setPrecio(self, precio):
        if isinstance(precio, float):
            self._precio = precio
        else:
            print('Error al cambiar de precio')

    def setDescripcion(self, descripcion):
        if isinstance(descripcion, str):
            self._descripcion =
