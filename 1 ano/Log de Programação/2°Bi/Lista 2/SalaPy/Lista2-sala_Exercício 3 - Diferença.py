x = float(input("Insira um número: "))
y = float(input("Insira um outro número: "))
if (x > y):
    d = x - y
    print("A diferença entre esses números é:{:.2f}".format(d))
else:
    d = y - x
    print("A diferença entre esses números é: {:.2f}".format(d))
