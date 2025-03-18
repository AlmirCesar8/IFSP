nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))

if 0<salario<=400:
    print(nome, '15%', salario, salario + salario*0.15)
elif 401<salario<=700:
    print(nome, '12%', salario, salario + salario*0.12)
elif 701<salario<=1000:
    print(nome, '10%', salario, salario + salario*0.1)
elif 1001<salario<=1800:
    print(nome, '7%', salario, salario + salario*0.07)
elif 1801<salario<=2500:
    print(nome, '4%', salario, salario + salario*0.04)
elif salario>2500:
    print(nome, 'sem aumento', salario)
else:
    print('Salário inválido')