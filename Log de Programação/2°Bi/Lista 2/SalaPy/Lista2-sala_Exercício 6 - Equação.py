import math
A = float(input("Insira A: "))
B = float(input("Insira B: "))
C = float(input("Insira C: "))
if (A == 0):
    print("Essa equação não é do 2° grau!")
else:
    D = (pow(B,2)) - 4 * A * C
    if (D < 0):
        print("Não há raízes reais para essa equação")
    else:
        x1 = (- B + math.sqrt(D)) / (2 * A) 
        x2 = (- B - math.sqrt(D)) / (2 * A)
        print("As raízes dessa equação são {:.2f} e {:.2f}".format(x1, x2))
