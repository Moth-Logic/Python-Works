def imprimir_triangulo(n):
    """Imprime un triángulo numérico centrado y simétrico.
Entradas: Un numero positivo entero
Salidas: Un triangulito muy bonito del tamaño que se pidio."""
    for i in range(1, n + 1):
        # Espacios para centrar
        print(" " * (n - i), end="")

        # Parte ascendente
        for j in range(i):
            print((j + i) % 10, end="")

        # Parte descendente (sin repetir el centro)
        for j in range(i - 2, -1, -1):
            print((j + i) % 10, end="")
        print()

# Programa principal
n = input("Escriba el tamaño del triángulo bonito: ")

if n == "Navidad":
    print("🎄 ¡Feliz Navidad!")
else:
    try:
        n = int(n)
        if n > 0:
            imprimir_triangulo(n)
        else:
            print("ERROR: n debe ser un entero positivo.")
    except ValueError:
        print("ERROR: SOLO NÚMEROS ENTEROS POSITIVOS")
