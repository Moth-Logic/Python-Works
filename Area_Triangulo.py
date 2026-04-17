def area_triangulo(base, altura):
    """Funcion que calcula el area de un triangulo.
    Entradas y restricciones :
    -base: int o float positivo.
    -altura: int o float positivo.
    Salidas:
    Area del triangulo (float)"""
    if type(base) not in (int,float) or base <= 0:
        raise Exception("base debe ser int o float positivo.")
    if type(altura) not in (int, float) or altura <= 0:
        raise Exception("base debe ser int o float positivo.")
    area = base*altura/2
    return area

def main():
    """Programa Principal del area triangulo"""
    continuar = True
    while continuar:
         try:
             base = float(input("Escriba la base del triangulo:"))
             altura = float(input("Escriba la altura del triangulo:"))
             resultado = area_triangulo(base,altura)
             print(f"El area es {resultado}")
             continuar = False
         except Exception as manuelito:
             print(f"ERROR: {manuelito}")

main()
