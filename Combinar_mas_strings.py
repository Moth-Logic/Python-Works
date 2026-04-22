def nuevo_combo(str1, str2):
    """Programa que pida al usuario dos strings A y B, divida el primer string en tres segmentos del mismo
tamaño (o lo más parecidos posible), el segundo en dos segmentos, y que imprima la concatenación de dichos
segmentos de la siguiente forma: tercer segmento de A, primer segmento de B invertido, segundo segmento
de A, segundo segmento de B invertido, primer segmento de A.
Entradas: 2 strings
Salidas: La concatenación de dichos segmentos de la siguiente forma: tercer segmento de A, primer segmento de B invertido, segundo segmento
de A, segundo segmento de B invertido, primer segmento de A. """
    if type(str1) != str or type(str2) != str:
        raise Exception("Debe ser string")

    n = len(str1)
    base = n // 3
    extra = n % 3

    a1 = str1[:base + (1 if extra > 0 else 0)]
    a2 = str1[len(a1):len(a1) + base + (1 if extra > 1 else 0)]
    a3 = str1[len(a1) + len(a2):]

    m = len(str2)
    mitad = m // 2

    b1 = str2[:mitad]
    b2 = str2[mitad:]

    b1_inv = b1[::-1]
    b2_inv = b2[::-1]

    resultado = a3 + b1_inv + a2 + b2_inv + a1
    print(resultado)

nuevo_combo("Naomi","Tecnologico de Costa Rica")