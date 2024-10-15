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
            raise ValueError('Error al crear instancia, error al asignar cliente')
        elif not isinstance(fecha, str):
            raise ValueError('Error al crear instancia, error al asignar fecha')
    
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
        print(f'Factura nº: {self.id}')
        print(f'Fecha: {self._fecha}')
        print('\nDatos del cliente')
        print('---------------------')
        print(f'Nombre: {self._cliente.getNombre()}')
        print(f'Direccion: {self._cliente.getDireccion()}')
        print(f'Telefono: {self._cliente.getTelefono()}')
        print('\nDetalle de factura')
        print('---------------------')
        print('Línea; Producto; antidad; Precio ud.; Precio total')
        print('---------------------')
        counter = 1
        subtotal = 0
        for linea in self._lineas:
            print(f'{counter}, {linea.getDescripcion()}, {linea.getCantidad()}, {linea.getPrecio()}, {linea.getSubtotal()}')
            subtotal += linea.getSubtotal()
            counter += 1
        print('\n')
        print(f'Subtotal: {subtotal} €')
        print(f'IVA (21%): {subtotal*0.21} €')
        print(f'TOTAL = {subtotal *1.21} €')