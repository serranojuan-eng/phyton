n = int(input("Ingrese un número entero: "))
if n <= 0:
    print("El número no es positivo")
else:
    cifras = len(str(n))
    suma = sum(int(d) for d in str(n))
    print("Cantidad de cifras:", cifras)
    print("Suma de cifras:", suma)
