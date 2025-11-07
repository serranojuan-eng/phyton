# Ejercicio 14: Convertir centímetros a yardas, metros, pies y pulgadas
cm = float(input("Introduce la longitud en centímetros: "))
metros = cm / 100
pulgadas = cm / 2.54
pies = pulgadas / 12
yardas = pies / 3
print("Metros:", metros)
print("Pulgadas:", pulgadas)
print("Pies:", pies)
print("Yardas:", yardas)
