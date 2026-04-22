def esvocal(letra):
    if type(letra) != str or len(letra) != 1:
        raise Exception("Debe ser string")
    vocales = {'a','e','i','o','u','A','E','I','O','U',
               'á','é','í','ó','ú','Á','É','Í','Ó','Ú'}
    print(f"{letra in vocales}")

esvocal("¿")