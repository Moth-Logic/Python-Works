import math
def esprimo(num):
    """Programa que lee un numero entero o positivo y imprime todos los numeros primos desde 2 hasta N.
Entradas y Restricciones:
- Número entero y positivo.
Salidas:
- Lista de numeros primos desde 2 hasta N"""
    if type(num) != int or num<2:
        raise Exception("Número debe ser Integer Positivo mayor a 2")
    for m in range(2, int(math.sqrt(num))+1):
        if num%m != 0:
            return True
        else:
            return None

def main():
    try:
        Base = 2
        num= int(input("Escriba un numero entero positivo:  "))
        for i in range(2, num+1):
            if esprimo(num) == True:
                print(f"{i}")
    except Exception  as e:
        print(f"Error: {e}")

main()
