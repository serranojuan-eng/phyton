# Cálculo del volumen de un cilindro sin usar librerías

# Definimos el valor de PI
PI = 3.1416

# Entrada de datos
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Proceso
volumen = PI * (radio ** 2) * altura

# Salida de datos
print(f"\nEl volumen del cilindro es: {volumen:.2f} unidades cúbicas")