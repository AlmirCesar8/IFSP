import math
def equacao(a,b,c):
    d = ((b ** 2) - (4 * a * c))
    if (d < 0):
        return("Essa equação não possui raízes reais")
    x1 = ((-b + math.sqrt(d))/ (2 * a))
    x2 = ((-b - math.sqrt(d))/ (2 * a))
    return (x1, x2)
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
if (a == 0):
    print("Isso não é uma equação do 2º grau")
else:
    print(equacao(a,b,c))
