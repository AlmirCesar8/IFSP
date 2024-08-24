n1 = float(input("Digite sua 1° nota: "))
n2 = float(input("Digite sua 2° nota: "))
n3 = float(input("Digite sua 3° nota: "))
M = (n1 + n2 + n3)/3
if (M >= 6.0):
    print("Você foi aprovado, sua nota foi {:.2f}".format(M))
else:
    print("Você não foi aprovado, sua média foi {:.2f}".format(M))