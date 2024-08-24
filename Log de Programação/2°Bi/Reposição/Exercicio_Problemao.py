x = "_"
f1 = f2 = f3 = f4 = f5 = 0
c = p = i = m = maior = menor = 0 
#13 variaveis

while x != "N" and x != "n":

    n = float(input("Digite um número: "))
    x = input("Deseja continuar (S/N)? ")

    m += n #guardando para a media
    c += 1 #contador

    if (c == 1):
        maior = menor = n #primeira verificação

    if n > maior: 
        maior = n #maior
    if n < menor:
        menor = n #menor

    if n % 2 == 0: 
        p += 1 #par 
    else:
        i += 1 #impar

    if n<0:
        f1 += 1
    elif 0 <= n < 15:
        f2 += 1
    elif 15 <= n < 100:
        f3 += 1
    elif 100 <= n < 100:
        f4 += 1
    else:
        f5 += 1

print('A média aritimétrica entre esses números é: {:.2f}'.format(m/c))
print('O maior número entre esses é:', maior)
print('O menor número entre esses é:', menor)
print('O total de números pares foi:', p)
print('O total de números ímpares foi:', i)
print('O total de elementos na faixa 1 foi:', f1)
print('O total de elementos na faixa 2 foi:', f2)
print('O total de elementos na faixa 3 foi:', f3)
print('O total de elementos na faixa 4 foi:', f4)
print('O total de elementos na faixa 5 foi:', f5)