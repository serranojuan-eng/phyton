# Ejemplo 2.3: Aplicación de funciones matemáticas en Python

import math  # Importamos la librería matemática

# Entrada de datos
numero = float(input("Ingrese un número real: "))

# Proceso: Aplicación de funciones matemáticas
raiz_cuadrada = math.sqrt(abs(numero))  # sqrt solo admite números positivos
potencia_cuadrado = math.pow(numero, 2)
potencia_cubo = math.pow(numero, 3)
valor_absoluto = abs(numero)
parte_entera = math.trunc(numero)
redondeado = round(numero)
seno = math.sin(numero)
coseno = math.cos(numero)
tangente = math.tan(numero)

# Salida de datos
print(f"\nResultados para el número {numero}:")
print(f"Raíz cuadrada: {raiz_cuadrada}")
print(f"Potencia al cuadrado: {potencia_cuadrado}")
print(f"Potencia al cubo: {potencia_cubo}")
print(f"Valor absoluto: {valor_absoluto}")
print(f"Parte entera: {parte_entera}")
print(f"Redondeado: {redondeado}")
print(f"Seno: {seno}")
print(f"Coseno: {coseno}")
print(f"Tangente: {tangente}")