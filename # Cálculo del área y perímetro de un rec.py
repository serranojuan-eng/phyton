# Cálculo del área y perímetro de un rectángulo

# Entrada de datos
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Proceso
area = base * altura
perimetro = 2 * (base + altura)

# Salida de datos
print(f"\nEl área del rectángulo es: {area:.2f}")
print(f"El perímetro del rectángulo es: {perimetro:.2f}")