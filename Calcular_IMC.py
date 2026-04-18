def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    
    if imc < 16:
        clasificacion = "Delgadez severa"
    elif imc < 17:
        clasificacion = "Delgadez moderada"
    elif imc < 18.5:
        clasificacion = "Delgadez leve"
    elif imc < 25:
        clasificacion = "Normal"
    elif imc < 30:
        clasificacion = "Preobesidad"
    elif imc < 35:
        clasificacion = "Obesidad 1"
    elif imc < 40:
        clasificacion = "Obesidad 2"
    else:
        clasificacion = "Obesidad 3"
    
    return imc, clasificacion


# Ejemplo de uso
peso = float(input("Ingrese el peso (kg): "))
estatura = float(input("Ingrese la estatura (m): "))

imc, clasificacion = calcular_imc(peso, estatura)

print("IMC:", round(imc, 2))
print("Clasificación:", clasificacion)