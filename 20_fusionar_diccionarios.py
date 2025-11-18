"""Ejercicio 20: Fusionar diccionarios
Lee dos diccionarios en formato clave:valor separados por comas. Si hay claves repetidas, el segundo sobrescribe.
"""
def parse_dict(s):
    d = {}
    for pair in [p.strip() for p in s.split(',') if p.strip()]:
        if ':' in pair:
            k, v = [x.strip() for x in pair.split(':',1)]
            d[k] = v
    return d

def main():
    A = parse_dict(input("Diccionario A (a:1,b:2): "))
    B = parse_dict(input("Diccionario B (b:10,c:3): "))
    # Python 3.9+ supports |
    try:
        C = A | B
    except:
        C = A.copy(); C.update(B)
    print(C)

if __name__ == '__main__':
    main()
