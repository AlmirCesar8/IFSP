n1 = float(input("Digite sua 1° nota: "))
n2 = float(input("Digite sua 2° nota: "))
M = (n1 + n2)/2
if (M >= 6.0):
    print("Você foi aprovado, sua nota foi {:.2f}".format(M))
else:
    e = float(input("Digite sua nota no exame: "))
    nm = (M + e)/2
    if (nm >= 5.0):
        print("Você foi aprovado em exame, sua nota foi {:.2f}".format(nm))
    else:
        print("Você não foi aprovado, sua nota após o exame foi {:.2f}".format(nm))
