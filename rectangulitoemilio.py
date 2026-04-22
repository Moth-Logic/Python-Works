def esta_dentro(r1, r2):
    """
    Retorna True si el rectángulo r1 está completamente dentro de r2
    r = (x1, x2, y1, y2)
    """
    return (r1[0] >= r2[0] and  # x1
            r1[1] <= r2[1] and  # x2
            r1[2] >= r2[2] and  # y1
            r1[3] <= r2[3])     # y2


def son_iguales(r1, r2):
    return r1 == r2


def leer_rectangulo(num):
    print(f"\nValores del rectángulo {num}")
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    y1 = int(input("y1: "))
    y2 = int(input("y2: "))
    return (x1, x2, y1, y2)


def main():
    r1 = leer_rectangulo(1)
    r2 = leer_rectangulo(2)

    if son_iguales(r1, r2):
        print("Los rectángulos son iguales")
    elif esta_dentro(r1, r2):
        print("El primer rectángulo está dentro del segundo")
    elif esta_dentro(r2, r1):
        print("El segundo rectángulo está dentro del primero")
    else:
        print("Ninguno de los dos rectángulos está dentro del otro")


if __name__ == "__main__":
    main()