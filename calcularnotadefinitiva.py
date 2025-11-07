# Calcular la nota definitiva de un estudiante

# Entrada de datos
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))

# Proceso: Calcular la media aritmética
nota_definitiva = (nota1 + nota2 + nota3 + nota4) / 4

# Salida de datos

print(f"\nLa nota definitiva del estudiante es: {nota_definitiva:.2f}")
