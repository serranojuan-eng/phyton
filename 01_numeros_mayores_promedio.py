"""Ejercicio 1: Números mayores que el promedio
Solicita al usuario una lista de números (separados por espacios) y muestra cuáles son mayores que el promedio.
Ejemplo de entrada: 10 5 8 3 9
"""
def main():
    s = input("Introduce números separados por espacios: ").strip()
    nums = [float(x) for x in s.split() if x]
    if not nums:
        print("No se ingresaron números.")
        return
    avg = sum(nums)/len(nums)
    mayores = [x for x in nums if x > avg]
    print(f"Promedio: {avg}")
    print("Mayores que el promedio:", mayores)

if __name__ == '__main__':
    main()
