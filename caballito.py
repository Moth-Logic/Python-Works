def es_movimiento_caballo_valido(origen, destino):
    col_origen = ord(origen[0].lower()) - ord('a')
    fila_origen = int(origen[1]) - 1

    col_destino = ord(destino[0].lower()) - ord('a')
    fila_destino = int(destino[1]) - 1

    dx = abs(col_destino - col_origen)
    dy = abs(fila_destino - fila_origen)

    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


def main():
    origen = input("Ingrese la posición inicial (ej: e4): ")
    destino = input("Ingrese la posición destino (ej: f6): ")

    if es_movimiento_caballo_valido(origen, destino):
        print("Movimiento válido del caballo")
    else:
        print("Movimiento inválido")


if __name__ == "__main__":
    main()