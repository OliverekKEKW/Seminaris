def vypocet(a,b,c):
    try:
        obvod = a + b + c
    except ValueError:
        raise ValueError('Nečíselný vstup.')
    if a < 0 or b < 0 or c < 0:
        raise ValueError('Zadaná záporná hodnota.')
    if a + b < c:
        raise ValueError('Nerovnosť voči strane c.')
    if b + c < a:
        raise ValueError('Nerovnosť voči strane a.')
    if a + c < b:
        raise ValueError('Nerovnosť voči strane b.')
    return obvod
a = float(input("Zadaj stranu a "))
b = float(input("Zadaj stranu b "))
c = float(input("Zadaj stranu c "))

try:
    print(f'Výsledný poplatok za : {vypocet(a,b,c)}m je {vypocet(a,b,c)}€')
except ValueError as chyba:
    print(chyba)
