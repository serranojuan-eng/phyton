"""Ejercicio 17: Contador de palabras
Solicita una frase y cuenta cuántas veces aparece cada palabra.
"""
from collections import Counter
def main():
    frase = input("Introduce una frase: ")
    words = frase.split()
    cnt = Counter(words)
    print(dict(cnt))

if __name__ == '__main__':
    main()
