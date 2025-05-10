from jogo import Jogo
from jogador import Jogador
from plataforma_de_jogos import PlataformaDeJogos

print("\n-------------Bem-vindo à Plataforma de Jogos!-------------")
print("Faça login para continuar.\n")
nickname = input("Digite o seu nickname: ")
id_jogador = int(input("Digite o seu ID: "))
jogador1 = Jogador(nickname, id_jogador)

plataforma = PlataformaDeJogos("GameBlin")
plataforma.adicionar_jogador(jogador1)

while True:
    op = int(input("\nEscolha uma das opções: \n1 - Exibir perfir\n2 - Adicionar saldo\n3 - Comprar jogo\n4 - Criar jogo\n5 - Presentear com jogo\n6 - Sair\n"))
    match op:
        case 1:
            jogador1.exibir_perfil()
        case 2:
            valor = float(input("Digite o valor a ser adicionado: "))
            jogador1.adicionar_saldo(valor)
            print(f"Saldo atualizado: R${jogador1.saldo_carteira:.2f}")
        case 3:
            print("\nÓtimo, nada melhor que comprar novos jogos.")
            while True:
                op = int(input("Escolha uma das opções: \n1 - Comprar jogo\n2 - Pesquisar jogo\n3 - Jogos do catálogo\n4 - Voltar\n"))
                match op:
                    case 1:
                        nome_jogo = str(input("Digite o nome do jogo que você deseja comprar: "))
                        plataforma.realizar_compra(jogador1.id_jogador, nome_jogo)
                    case 2:
                        nome_jogo = str(input("Digite o nome do jogo que você deseja comprar: "))
                        busca_jogo = plataforma.buscar_jogo_por_titulo(nome_jogo)
                        if busca_jogo is not None:
                            busca_jogo.exibir_detalhes()
                            op = str(input("Deseja comprar este jogo? (s/n): ")).lower()
                            if op == "s":
                                plataforma.realizar_compra(jogador1.id_jogador, nome_jogo)
                            else:
                                print("Compra cancelada.")
                        else:
                            print("Jogo não encontrado, procure outra vez.")
                    case 3:
                        plataforma.listar_jogos_catalogo()
                    case 4:
                        break
                    case _:
                        print("Opção inválida, tente outra vez")
        case 4:
            pass
        case 5:
            pass
        case 6:
            break
        case _:
            print("Opção inválida, tente outra vez")

print("\nEncerrando programa...\nObrigado por usá-lo")