"""
Clase Factura

Atributos

-- sigID int = 1
-+ IVA int = 21
-fecha:str
-id:int

+Factura(c:Cliente, fecha:str)
+anyadirLinea(cant:int, desc:str, prec:float):void
-getSigId():int
__str()__:str
"""

from Cliente import Cliente
from Linea import Linea


class Factura:
    sigId = 0
    IVA = 21

    def __init__(self, cliente, fecha):
        if not isinstance(cliente, Cliente):
            raise ValueError(
                'Error al crear instancia, error al asignar cliente')
        elif not isinstance(fecha, str):
            raise ValueError(
                'Error al crear instancia, error al asignar fecha')

        self.id = Factura.sigId
        self._fecha = fecha
        self._cliente = cliente
        self._lineas = []

        Factura.sigId += 1

    def anyadirLinea(self, cant, desc, prec):
        if not isinstance(cant, int):
            raise ValueError('Error al introducir la cantidad')
        elif not isinstance(desc, str):
            raise ValueError('Error al introducir la descripcion')
        elif not isinstance(prec, (int, float)):
            raise ValueError('Error al introcudir el precio')

        self._lineas.append(Linea(cant, prec, desc))

    @classmethod
    def _getSigId(cls):
        a = cls.sigId
        cls.sigId += 1
        return a

    def printeame(self):
        print(f'Factura nº: {self.id}\n')
        print(f'Fecha: {self._fecha}\n\n')
        print('Datos del cliente\n')
        print('---------------------\n')
        print(f'Nombre: {self._cliente.getNombre()}\n')
        print(f'Direccion: {self._cliente.getDireccion()}\n')
        print(f'Telefono: {self._cliente.getTelefono()}\n\n')
        print('Detalle de factura\n')
        print('---------------------\n')
        print('Línea; Producto; antidad; Precio ud.; Precio total\n')
        print('---------------------\n')
        counter = 1
        subtotal = 0
        for linea in self._lineas:
            print(f'{counter}, {linea.getDescripcion()}, {linea.getCantidad()}, {
                  linea.getPrecio()}, {linea.getSubtotal()}\n')
            subtotal += linea.getSubtotal()
            counter += 1
        print('\n')
        print(f'Subtotal: {subtotal} €\n')
        print(f'IVA (21%): {subtotal*0.21} €\n')
        print(f'TOTAL = {subtotal * 1.21} €\n')

    def __str__(self):
        counter = 1
        subtotal = 0
        chain_aux = ''
        for linea in self._lineas:
            chain_aux += (f'{counter}, {linea.getDescripcion()}, {linea.getCantidad()}, {
                linea.getPrecio()}, {linea.getSubtotal()}\n')
            subtotal += linea.getSubtotal()
            counter += 1

        chain = f'Factura nº: {self.id}\n' + f'Fecha: {self._fecha}\n\n' + 'Datos del cliente\n' + \
            '---------------------\n' + \
            f'Nombre: {self._cliente.getNombre()}\n' + \
            f'Direccion: {self._cliente.getDireccion()}\n' + \
            f'Telefono: {self._cliente.getTelefono()}\n\n' + \
            'Detalle de factura\n' + \
            '---------------------\n' + \
            'Línea; Producto; antidad; Precio ud.; Precio total\n' + \
            '---------------------\n' + \
            f'{chain_aux}' + \
            '\n' + \
            f'Subtotal: {subtotal} €\n' + \
            f'IVA (21%): {subtotal*0.21} €\n' + \
            f'TOTAL = {subtotal * 1.21} €\n'
        return chain
