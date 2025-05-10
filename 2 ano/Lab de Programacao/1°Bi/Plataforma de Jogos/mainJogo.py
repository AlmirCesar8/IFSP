from jogo import Jogo
from jogador import Jogador
from plataforma_de_jogos import PlataformaDeJogos

print("\n-------------Bem-vindo à Plataforma de Jogos!-------------")
print("Faça login para continuar.\n")
nickname = input("Digite o seu nickname: ")
id_jogador = int(input("Digite o seu ID: "))
jogador1 = Jogador(nickname, id_jogador)

plataforma = PlataformaDeJogos("GameBlin")
while True:
    op = int(input("\nEscolha uma das opções: \n1 - Exibir perfir\n2 - Adicionar saldo\n3 - Comprar jogo\n4 - Sair\n"))
    match op:
        case 1:
            jogador1.exibir_perfil()
        case 2:
            valor = float(input("Digite o valor a ser adicionado: "))
            jogador1.adicionar_saldo(valor)
            print(f"Saldo atualizado: R${jogador1.saldo_carteira:.2f}")
        case 3:
            pass
        case 4:
            break
        case _:
            print("Opção inválida, tente outra vez")
            continue

print("\nEncerrando programa...\nObrigado por usá-lo")