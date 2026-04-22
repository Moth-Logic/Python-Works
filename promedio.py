def calcular_promedio():
    suma = 0.0
    contador = 0

    print("Ingrese números positivos (0 para terminar):")

    while True:
        num = float(input())

        if num == 0:
            break
        elif num < 0:
            print("No se aceptan negativos")
        else:
            suma += num
            contador += 1

    return suma, contador


def main():
    suma, cantidad = calcular_promedio()

    if cantidad == 0:
        print("No se ingresaron números válidos")
    else:
        promedio = suma / cantidad
        print(f"Cantidad de números: {cantidad}")
        print(f"Promedio: {promedio}")


if __name__ == "__main__":
    main()