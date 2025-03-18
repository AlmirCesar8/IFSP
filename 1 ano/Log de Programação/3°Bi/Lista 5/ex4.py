import math
def fatorial(n):
    return(math.factorial(n))
n = int(input("Digite o número para o fatorial: "))
if (n>=0):
    print(fatorial(n))
else:
    print("Digite um número inteiro positivo")