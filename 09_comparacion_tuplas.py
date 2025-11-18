"""Ejercicio 9: Comparación de tuplas
Lee dos tuplas de enteros (separadas por espacios) y determina cuál es mayor.
"""
def read_tuple(prompt):
    return tuple(int(x) for x in input(prompt).split())

def main():
    t1 = read_tuple("Tupla 1: ")
    t2 = read_tuple("Tupla 2: ")
    if t1 > t2:
        print("La primera tupla es mayor.")
    elif t1 < t2:
        print("La segunda tupla es mayor.")
    else:
        print("Ambas tuplas son iguales.")

if __name__ == '__main__':
    main()
