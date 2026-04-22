import math

def raiz(n):
    e = 0.00001
    g1 = n / 2
    g2 = (g1 + n / g1) / 2

    while abs(g1 - g2) > e:
        g1 = g2
        g2 = (g1 + n / g1) / 2

    return g2


def main():
    n = float(input("Ingrese un número real positivo: "))

    if n <= 0:
        print("Error: debe ser positivo")
    else:
        aproximacion = raiz(n)
        real = math.sqrt(n)
        diferencia = abs(aproximacion - real)

        print(f"Aproximación: {aproximacion}")
        print(f"Raíz real: {real}")
        print(f"Diferencia: {diferencia}")


if __name__ == "__main__":
    main()