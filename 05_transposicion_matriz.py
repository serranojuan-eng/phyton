"""Ejercicio 5: Transposición de una matriz
Pide dimensiones y la matriz; devuelve su transpuesta.
"""
def read_matrix(rows, cols):
    M = []
    for i in range(rows):
        row = [x for x in input(f"Fila {i+1} (separada por espacios): ").split()]
        if len(row) != cols:
            raise ValueError("Número de columnas incorrecto.")
        M.append(row)
    return M

def main():
    try:
        rows = int(input("Número de filas: "))
        cols = int(input("Número de columnas: "))
        M = read_matrix(rows, cols)
        T = [[M[i][j] for i in range(rows)] for j in range(cols)]
        print("Transpuesta:")
        print(T)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
