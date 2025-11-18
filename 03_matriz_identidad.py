"""Ejercicio 3: Matriz identidad
Solicita un entero n y muestra la matriz identidad n x n.
"""
def main():
    try:
        n = int(input("Introduce n (entero positivo): "))
    except:
        print("Entrada inválida.")
        return
    if n <= 0:
        print("n debe ser mayor que 0.")
        return
    for i in range(n):
        row = [1 if i==j else 0 for j in range(n)]
        print(row)

if __name__ == '__main__':
    main()
