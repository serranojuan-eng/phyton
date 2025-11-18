n = int(input("Ingrese un número entero positivo: "))
cifras = len(str(n))
suma = sum(int(d)**cifras for d in str(n))
if suma == n:
    print(f"{n} es un número de Armstrong")
else:
    print(f"{n} NO es un número de Armstrong")
