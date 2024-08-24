m = float(input('Digite seu peso, (em Kg): '))
h = float(input('Digite sua altura, (em m): '))
imc = (m / (h ** 2))
print('Seu IMC é igual a {:.2f}'.format(imc))
