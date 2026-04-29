a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))
print()

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

if a >= b + c:
    print("NAO FORMA TRIANGULO")
    exit()

else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif (a == b != c) or (a == c != b) or (b == c != a):
    print("TRIANGULO ISOCELES")
