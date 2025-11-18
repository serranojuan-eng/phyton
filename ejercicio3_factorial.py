n = int(input("Ingrese un número entero: "))
if n < 0:
    print("No existe factorial de números negativos.")
else:
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f"{n}! = {f}")
