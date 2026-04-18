"""
Moth_Logic:
Este programa solicita un año límite (mayor o igual a 1582) y muestra
todos los años bisiestos desde 1582 hasta ese límite. Usa una función
para determinar si un año es bisiesto según las reglas del calendario:
divisible entre 4, pero no entre 100, a menos que también sea divisible entre 400.
"""

def bisi(vueltas_al_sol):
    return (vueltas_al_sol % 4 == 0) and (
        (vueltas_al_sol % 100 != 0) or (vueltas_al_sol % 400 == 0)
    )


AL = int(input("Introduzca el año límite: "))

if AL >= 1582:
    for i in range(1582, AL + 1):
        if bisi(i):
            print(i)
else:
    print("Ese no sirve lol xd")
