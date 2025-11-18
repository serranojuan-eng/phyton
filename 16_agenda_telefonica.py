"""Ejercicio 16: Agenda telefónica
Solicita pares nombre - teléfono hasta que el usuario escriba 'fin'.
"""
def main():
    agenda = {}
    while True:
        entrada = input("Nombre - Teléfono (o 'fin' para terminar): ").strip()
        if entrada.lower() == 'fin':
            break
        if '-' in entrada:
            nombre, telefono = [p.strip() for p in entrada.split('-',1)]
        else:
            parts = entrada.split()
            if len(parts) >= 2:
                nombre = parts[0]
                telefono = parts[1]
            else:
                print("Formato inválido.")
                continue
        agenda[nombre] = telefono
    print(agenda)

if __name__ == '__main__':
    main()
