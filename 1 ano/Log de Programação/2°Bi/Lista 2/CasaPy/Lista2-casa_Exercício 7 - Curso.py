codigo = int(input("Insira o código de acesso do seu curso: "))
match codigo:
    case 1:
        print("Engenharia")
    case 2:
        print("Edificações")
    case 3:
        print("Sistemas elétricos")
    case 4:
        print("Turismo")
    case 5:
        print("Análise de Sistemas")
    case _:
        print("Código Inválido")