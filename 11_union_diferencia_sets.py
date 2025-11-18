"""Ejercicio 11: Unión y diferencia entre conjuntos
Lee dos listas de números y muestra unión y diferencia (A - B).
"""
def read_set(prompt):
    return set(int(x) for x in input(prompt).split())

def main():
    A = read_set("Elementos de A (separados por espacios): ")
    B = read_set("Elementos de B (separados por espacios): ")
    print("Union:", A | B)
    print("Diferencia A - B:", A - B)

if __name__ == '__main__':
    main()
