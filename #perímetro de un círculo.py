#perímetro de un círculo

# Definimos la constante PI
PI = 3.1416

# Entrada de datos
radio = float(input("Ingrese el valor del radio del circulo"))

# Proceso: Cálculo del área y perímetro
area = PI * (radio ** 2)
perimetro = 2 * PI * radio

# Salida de datos
print("El área del círculo es: {area}")
print("El perímetro del círculo es: {perimetro}")
