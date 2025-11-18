"""Ejercicio 15: Subconjunto y superconjunto
Determina si A es subconjunto de B y si B es superconjunto de A.
"""
def main():
    A = set(input("A (elementos separados por espacios): ").split())
    B = set(input("B (elementos separados por espacios): ").split())
    if A.issubset(B):
        print("A es subconjunto de B")
    else:
        print("A no es subconjunto de B")
    if B.issuperset(A):
        print("B es superconjunto de A")
    else:
        print("B no es superconjunto de A")

if __name__ == '__main__':
    main()
