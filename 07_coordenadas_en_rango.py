"""Ejercicio 7: Coordenadas dentro de un rango
Lee una coordenada x y y y un rango min y max y verifica si están dentro.
"""
def main():
    x = float(input("x: "))
    y = float(input("y: "))
    minimo = float(input("Rango mínimo: "))
    maximo = float(input("Rango máximo: "))
    if minimo <= x <= maximo and minimo <= y <= maximo:
        print("Dentro del rango")
    else:
        print("Fuera del rango")

if __name__ == '__main__':
    main()
