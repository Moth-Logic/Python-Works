"""Moth_Logic:
Este programa recibe un número entero positivo n y calcula la suma
acumulada desde 1 hasta n. En cada iteración muestra el valor parcial
de la suma, y al final imprime el resultado total."""

n = int(input("Ingrese un número: "))

if n > 0:
    i = 1
    suma = 0

    while i <= n:
        suma += i
        print(suma)
        i += 1

    print(suma)
else:
    print("Error")
