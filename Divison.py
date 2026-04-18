def division_por_restas(N, D):
    # Validación básica
    if D == 0:
        return "Error: no se puede dividir entre 0"
    
    C = 0  # cociente
    R = N  # residuo
    
    while R >= D:
        R = R - D
        C = C + 1
    
    return C, R


# Ejemplo de uso
N = int(input("Ingrese el dividendo (N): "))
D = int(input("Ingrese el divisor (D): "))

cociente, residuo = division_por_restas(N, D)

print("Cociente:", cociente)
print("Residuo:", residuo)