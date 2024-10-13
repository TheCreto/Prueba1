from Coordenada import Coordenada


def pedir_coordenadas():
    x = input('Introduzca la coordenada x: ')
    y = input('Introduzca la coordenada y: ')
    return x, y


def main():
    x, y = pedir_coordenadas()
    coord_1 = Coordenada(x, y)
    coord_2 = Coordenada(coord_1)
    print(coord_1, coord_2)
    coord_1.setX(2)
    print(coord_1, coord_2)


if __name__ == '__main__':
    main()
