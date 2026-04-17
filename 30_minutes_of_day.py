"""Moth_Logic:
Este programa recorre todas las horas del día (0 a 23) y, por cada hora,
imprime dos momentos específicos: el minuto 0 y el minuto 30. Es decir,
muestra la hora en intervalos de 30 minutos en formato h:m."""

h = 0

while h < 24:
    m = 0

    while m < 60:
        print(f"{h}:{m}")
        m += 30

    h += 1
