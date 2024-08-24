n = int(input("Digite um número menor ou igual a 50: "))
if (n<=50):
    cont = n
    while (cont <= 250):
        print(cont)
        cont *= 3
else:
    print("Este número é maior que 50")