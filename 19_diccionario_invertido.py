"""Ejercicio 19: Diccionario invertido
Lee un diccionario simple en formato clave:valor separados por comas y lo invierte.
Ejemplo entrada: a:1,b:2,c:3
"""
def main():
    s = input("Introduce pares clave:valor separados por comas: ").strip()
    if not s:
        print("{}")
        return
    pairs = [p.strip() for p in s.split(',') if p.strip()]
    d = {}
    for pair in pairs:
        if ':' in pair:
            k, v = [x.strip() for x in pair.split(':',1)]
            d[k] = v
    inv = {v:k for k,v in d.items()}
    print(inv)

if __name__ == '__main__':
    main()
