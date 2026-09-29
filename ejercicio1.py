nota1 = float(input("Ingrese nota 1: "))
while nota1 < 1.0 or nota1 > 7.0:
    print("Nota fuera de rango (debe ser entre 1.0 y 7.0).")
    nota1 = float(input("Reingrese nota 1: "))

nota2 = float(input("Ingrese nota 2: "))
while nota2 < 1.0 or nota2 > 7.0:
    print("Nota fuera de rango (debe ser entre 1.0 y 7.0).")
    nota2 = float(input("Reingrese nota 2: "))

promedio = (nota1 + nota2) / 2
print(f"El promedio es: {promedio}")
