import math
op = "_"
while (op != "S" and op != "s"):
    op = input('Escolha uma das operação:\n"+" - Soma\n"-" - Subtração\n"*" - Multiplicação\n"/" - Divisão\n"^" - Potenciação\n"**" - Radiciação\n"%" - Porcentagem\n"#" - Resto de divisão\n"S" - Sair\n')
    if (op == "S" or op == "s"):
        print("Encerrando programa...\nObrigado por usá-lo")
        break

    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    match op:
        case "+" :
            print(a + b)
        case "-" :
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            if (b != 0):
                print(a / b)
            else:
                print("Não é possível efetuar uma divisão por 0, por favor insira outro número")
        case "^":
            print(pow(a,b))
        case "**":
            if a>=0:
                if b == 2:
                    print(math.sqrt(a))
                elif b > 2:
                    print(a ** (1/b))
                else:
                    print ("O indíce deve ser um número maior que 1, por favor insira outro número")
            else:
                if b % 2 == 0:
                    print("Não é possível efetuar raiz de indíce par e radicando negativo, por favor insira outro número")
                else:
                    print(-((-a) ** (1/b)))
        case "%":
            print(a * (b/100))
        case "#":
            print(a % b)
        case _ :
            print("Operação inválida, insira uma das disponíveis")
