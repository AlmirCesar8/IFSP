a = int(input("Digite o um número: "))
maior = a
menor = a
for _ in range(4):
    a = int(input("Digite o um número: "))
    if (a > maior):
        maior = a
    if (a < menor):
        menor = a
print("Dentre esses números o menor é: ", menor)
print("Dentre esses números o maior é: ", maior)
