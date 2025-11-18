aprobados = 0
reprobados = 0
suma = 0
cantidad = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(cantidad):
    codigo = input(f"Ingrese el código del estudiante {i+1}: ")
    nota = float(input("Ingrese la nota definitiva: "))
    suma += nota
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

promedio = suma / cantidad
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio del grupo:", promedio)
