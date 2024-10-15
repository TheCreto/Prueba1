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
    def __init__(self, nombre, direccion, telefono):
        if not isinstance(nombre, str):
            raise ValueError('Error al crear instancia, error al introducir el nombre')
        elif not isinstance(direccion, str):
            raise ValueError('Error al crear instancia, error al introducir la direccion')
        elif not isinstance(telefono, str):
            raise ValueError('Error al crear instancia, error al introducir telefono')
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
        if not isinstance(nombre, str):
            raise ValueError('Error al cambiar de nombre')       
        self._nombre = str(nombre)


    def setTelefono(self, telefono):
        if not isinstance(telefono, str):
            raise ValueError('Error al cambiar de telefono')
        self._telefono = telefono

    def setDireccion(self, direccion):
        if not isinstance(direccion, str):
            raise ValueError('Error al cambiar de direccion')
        self._direccion = str(direccion)
