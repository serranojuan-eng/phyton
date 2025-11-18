"""Ejercicio 12: Palabras únicas de una frase
Solicita una frase y muestra el conjunto de palabras únicas.
"""
def main():
    frase = input("Introduce una frase: ")
    palabras = set(frase.split())
    print(palabras)

if __name__ == '__main__':
    main()
