"""Ejercicio 14: Diferencia simétrica
Lee dos conjuntos y muestra los elementos exclusivos (simétrica).
"""
def read_set(prompt):
    return set(input(prompt).split())

def main():
    A = read_set("Conjunto A (elementos separados por espacios): ")
    B = read_set("Conjunto B (elementos separados por espacios): ")
    print(A ^ B)

if __name__ == '__main__':
    main()
