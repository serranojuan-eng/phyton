"""Ejercicio 8: Empaquetar y desempaquetar datos
Lee nombre, edad, país y muestra cada uno usando desempaquetado.
"""
def main():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    pais = input("País: ")
    datos = (nombre, edad, pais)
    n, e, p = datos
    print("Nombre:", n)
    print("Edad:", e)
    print("País:", p)

if __name__ == '__main__':
    main()
