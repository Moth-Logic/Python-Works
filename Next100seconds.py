"""Moth_Logic:
Este programa recibe una hora inicial (horas, minutos y segundos)
y simula el paso del tiempo durante 100 segundos. En cada iteración,
incrementa los segundos y ajusta minutos y horas cuando corresponde
(segundos a 60, minutos a 60, horas a 24). Finalmente, imprime cada
nuevo segundo en formato h:m:s."""

def sigsec(h, m, s):
    i = 1

    while i <= 100:
        s += 1

        if s == 60:
            s = 0
            m += 1

        if m == 60:
            m = 0
            h += 1

        if h == 24:
            h = 0

        print(f"{h}:{m}:{s}")

        i += 1


# Programa principal
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

sigsec(h, m, s)
