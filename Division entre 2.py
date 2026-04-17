def divisiones(num):
    """Funcion que recibe un numero y dice cuantas veces es divisible entre 2.
Entradas y restricciones:
- Numero Entero POsitivo
Salidas:
Cuantas veces es divisible entre dos (int)"""
    if type(num) != int or num<0:
        raise Exception("Numero debe ser un entero positivo.")
    divi = 0
    while num%2 == 0:
        num = num//2
        divi += 1
    return divi

def main():
    #Programa Principal de la cantidad de veces
    try:
        num = int(input("Escriba un numero entero positivo."))
        result = divisiones(num)
        print(f"La cantidad de veces que puede dividir {num} entre 2 es {result}")
    except Exception as e:
        print (f"ERROR: {e}")

main()
    
