"""Ejercicio 13: Intersección de números pares
Lee dos listas y muestra los números pares comunes.
"""
def pares_from_list(lst):
    return {int(x) for x in lst if int(x)%2==0}

def main():
    A = input("Lista A (separada por espacios): ").split()
    B = input("Lista B (separada por espacios): ").split()
    pa = pares_from_list(A)
    pb = pares_from_list(B)
    print(pa & pb)

if __name__ == '__main__':
    main()
