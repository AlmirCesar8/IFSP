def pares(n):
    if (n % 2 == 0):
        return(True)
    else:
        return(False)
n = float(input("Digite um número para a verificação: "))
print(pares(n))