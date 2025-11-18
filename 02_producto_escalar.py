"""Ejercicio 2: Producto escalar de dos listas
Pide dos listas de igual tamaño (elementos separados por espacios) y calcula el producto escalar.
"""
def main():
    a = [float(x) for x in input("Lista A (separada por espacios): ").split()]
    b = [float(x) for x in input("Lista B (separada por espacios): ").split()]
    if len(a) != len(b):
        print("Las listas deben tener la misma longitud.")
        return
    prod = sum(x*y for x,y in zip(a,b))
    print("Producto escalar =", prod)

if __name__ == '__main__':
    main()
