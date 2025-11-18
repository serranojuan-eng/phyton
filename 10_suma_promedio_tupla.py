"""Ejercicio 10: Suma y promedio con tuplas
Lee una tupla de números (separados por espacios) y calcula suma y promedio.
"""
def main():
    nums = [float(x) for x in input("Introduce números separados por espacios: ").split()]
    if not nums:
        print("No hay números.")
        return
    print("Suma =", sum(nums))
    print("Promedio =", sum(nums)/len(nums))

if __name__ == '__main__':
    main()
