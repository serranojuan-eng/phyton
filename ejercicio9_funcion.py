n = int(input("Ingrese valor máximo de x: "))
for x in range(0, n+1, 2):
    print(f"x={x}, f(x)={x**3 + x**2 - 5}")
