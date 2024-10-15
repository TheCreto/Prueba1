from Factura import Factura
from Cliente import Cliente
from Linea import Linea

nombre = 'Jose Luis'
direccion = 'Calle falsa 123'
telefono = '+34 123 456 789'

cliente = Cliente(nombre, direccion, telefono)

fecha = '22/10/2024'

factura = Factura(cliente, fecha)

factura.anyadirLinea(1, 'Raton USB', 8.43)
factura.anyadirLinea(2, 'Memoria RAM 2GB', 21.15)
factura.anyadirLinea(1, 'Altavoces', 12.66)

factura.printeame()