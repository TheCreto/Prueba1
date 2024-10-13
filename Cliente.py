'''
Clase Cliente

Atributos
- nombre: str
- direccion: str
- telefono: str

Metodos

+ Cliente(nom: str, dir: str, tel: str)
+ getNombre(): str
+ getTelefono(): str
+ getDireccion(): str
+ setNombre(nom: str): void
+ setTelefono(tel: str): void
+ setdireccion(dir: str): void
'''


class Cliente:
    def __init__(self, cnombre, cdireccion, ctelefono):
        nombre = 'Error'
        direccion = 'Error'
        telefono = 'Error'

        try:
            nombre = str(cnombre)
            direccion = str(cdireccion)
            for char in ctelefono:
                if char != '+' and char != ' ':
                    int(char)
            telefono = str(ctelefono)

        except ValueError:
            print('Error al crear instancia')
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono

    def getNombre(self):
        return self._nombre

    def getTelefono(self):
        return self._telefono

    def getDireccion(self):
        return self._direccion

    def setNombre(self, nombre):
        try:
            self._nombre = str(nombre)
        except ValueError:
            print('Error al cambiar de nombre')

    def setTelefono(self, telefono):
        try:
            for char in telefono:
                if (char != '+') and (char != ' '):
                    int(char)
            self._telefono = str(telefono)
        except ValueError:
            print('Error al cambiar de telefono')

    def setDireccion(self, direccion):
        try:
            self._direccion = str(direccion)
        except ValueError:
            print('Error al cambiar de direccion')
