# Ejercicio 13: Intercambiar los valores de dos palabras
a = input("Introduce la primera palabra (A): ")
b = input("Introduce la segunda palabra (B): ")
a, b = b, a
print("Después del intercambio:")
print("A =", a)
print("B =", b)
