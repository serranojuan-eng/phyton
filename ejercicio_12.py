# Ejercicio 12: Generar un número aleatorio del 10 al 50 y disminuirlo en 15%
import random
num = random.randint(10, 50)
disminuido = num * 0.85
print("Número aleatorio:", num)
print("Número disminuido en 15%:", disminuido)
