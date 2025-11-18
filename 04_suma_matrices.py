"""Ejercicio 4: Suma de dos matrices
Pide dimensiones y luego las matrices fila por fila (valores separados por espacios).
"""
def read_matrix(rows, cols, name="M"):
    print(f"Introduce {rows} filas de la matriz {name}, cada fila con {cols} valores separados por espacios:")
    M = []
    for i in range(rows):
        row = [float(x) for x in input(f"Fila {i+1}: ").split()]
        if len(row) != cols:
            raise ValueError("Número de columnas incorrecto.")
        M.append(row)
    return M

def main():
    try:
        rows = int(input("Número de filas: "))
        cols = int(input("Número de columnas: "))
        A = read_matrix(rows, cols, "A")
        B = read_matrix(rows, cols, "B")
        C = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
        print("Resultado:")
        print(C)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
