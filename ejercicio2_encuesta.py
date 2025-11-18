android = ios = 0
print("Encuesta Android vs iOS")
while True:
    codigo = input("Digite su código (o 'fin' para terminar): ")
    if codigo.lower() == "fin":
        break
    eleccion = input("Elija plataforma (android/ios): ").lower()
    if eleccion == "android":
        android += 1
    elif eleccion == "ios":
        ios += 1
    else:
        print("Opción inválida, no se contará.")
print(f"Android: {android} votos")
print(f"iOS: {ios} votos")
