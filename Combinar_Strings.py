def combistrin(str1, str2):
    """un programa que pida dos strings al usuario y calcule dos strings nuevos. El primero debe estar
formado por la primera mitad del primer string y la segunda mitad del segundo. El segundo string debe estar
formado por la primera mitad del segundo string y la segunda mitad del primer string.
Entradas: 2 strings.
Salidas: dos strings nuevos. El primero debe estar
formado por la primera mitad del primer string y la segunda mitad del segundo. El segundo string debe estar
formado por la primera mitad del segundo string y la segunda mitad del primer string. """
    if type(str1) != str or type(str2) != str:
        raise Exception("Debe ser un string")
    mit1 = len(str1) // 2
    mit2 = len(str2) // 2
    MitadPri1 = str1[:mit1]
    MitadUlt1 = str1[mit1:]
    MitadPri2 = str2[:mit2]
    MitadUlt2 = str2[mit2:]
    print(MitadPri1+MitadUlt2)
    print(MitadPri2+MitadUlt1)

combistrin("Yancy","Naomi")