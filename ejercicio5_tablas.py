tabla = int(input("¿Qué tabla desea repasar? (1 a 20): "))
correctas = 0
for i in range(1, 11):
    resp = int(input(f"{tabla} x {i} = "))
    if resp == tabla * i:
        print("¡Correcto!")
        correctas += 1
    else:
        print(f"Incorrecto. Correcto: {tabla*i}")
print("Aciertos:", correctas)
