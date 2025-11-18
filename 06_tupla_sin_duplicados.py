"""Ejercicio 6: Conversión de lista a tupla sin duplicados
Solicita elementos separados por comas o espacios y devuelve una tupla sin duplicados (preserva orden).
"""
def main():
    s = input("Introduce elementos separados por comas o espacios: ").replace(',', ' ')
    items = [x for x in s.split() if x]
    seen = []
    for it in items:
        if it not in seen:
            seen.append(it)
    print(tuple(seen))

if __name__ == '__main__':
    main()
