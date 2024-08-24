a = float(input("Insira a medida do primeiro lado: "))
b = float(input("Insira a medida do segundo lado: "))
c = float(input("Insira a medida do terceiro lado: "))
if (a < b + c) and (b < a + c) and (c < b + a):
    if (a == b) and (c == a):
        print("É um triângulo equilátero")
    else:
        if (a != b) and (b != c):
            print("É um triângulo escaleno")
        else:
            print("É um triângulo isóceles")
else:
    print("Esses valores não são válidos para um triângulo")
