def evaluar_nota(nota):
    if nota < 60:
        return "reprobado"
    elif nota < 70:
        return "recuperación"
    elif nota < 90:
        return "aprobado"
    else:
        return "aprobado con honores"


nota = float(input("Ingrese la nota del estudiante: "))

resultado = evaluar_nota(nota)
print("Resultado:", resultado)