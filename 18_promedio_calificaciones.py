"""Ejercicio 18: Promedio de calificaciones
Ingresa pares Nombre:nota hasta 'fin' y calcula el promedio general.
"""
def main():
    notas = {}
    while True:
        entrada = input("Nombre: nota (o 'fin' para terminar): ").strip()
        if entrada.lower() == 'fin':
            break
        if ':' in entrada:
            nombre, nota = [p.strip() for p in entrada.split(':',1)]
            try:
                notas[nombre] = float(nota)
            except:
                print("Nota inválida.")
        else:
            print("Formato inválido. Use Nombre: nota")
    if notas:
        promedio = sum(notas.values())/len(notas)
        print("Promedio general:", promedio)
    else:
        print("No hay notas.")

if __name__ == '__main__':
    main()
