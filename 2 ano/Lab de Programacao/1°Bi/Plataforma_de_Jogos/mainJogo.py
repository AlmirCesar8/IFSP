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
    op = int(input("\nEscolha uma das opções: \n1 - Exibir perfir\n2 - Adicionar saldo\n3 - Comprar jogo\n4 - Criar jogo\n5 - Presentear com jogo\n6 - Trocar de conta\n7 - Jogar\n8 - Sair\n"))
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
            print("\nÓtimo, nada melhor que criar novos jogos.")
            nome_jogo = str(input("Digite o nome do jogo: "))
            genero = str(input("Digite o gênero do jogo: "))
            classificacao_etaria = str(input("Digite a classificação etária do jogo: "))
            preco_jogo = float(input("Digite o preço do jogo: "))
            jogo = Jogo(nome_jogo, genero, classificacao_etaria, preco_jogo)
            plataforma.adicionar_jogo_catalogo(jogo)
        case 5:
            while True:
                print("\nÓtimo, nada melhor que presentear novos jogos a pessoas queridas.")
                op = int(input("Escolha uma das opções: \n1 - Presentear jogo\n2 - Pesquisar jogo\n3 - Jogos do catálogo\n4 - Voltar\n"))
                match op:
                    case 1:
                        nome_jogo = str(input("Digite o nome do jogo que você deseja presentear: "))
                        id_jogador_presenteado = int(input("Digite o ID do jogador que receberá o jogo: "))
                        plataforma.presentear_jogo(jogador1.id_jogador, nome_jogo, id_jogador_presenteado)
                    case 2:
                        nome_jogo = str(input("Digite o nome do jogo que você deseja comprar: "))
                        busca_jogo = plataforma.buscar_jogo_por_titulo(nome_jogo)
                        if busca_jogo is not None:
                            busca_jogo.exibir_detalhes()
                            op = str(input("Deseja comprar este jogo? (s/n): ")).lower()
                            if op == "s":
                                id_jogador_presenteado = int(input("Digite o ID do jogador que receberá o jogo: "))
                                plataforma.presentear_jogo(jogador1.id_jogador, nome_jogo, id_jogador_presenteado)
                            else:
                                print("Operação cancelada.")
                        else:
                            print("Jogo não encontrado, procure outra vez.")
                    case 3:
                        plataforma.listar_jogos_catalogo()
                    case 4:
                        break
                    case _:
                        print("Opção inválida, tente outra vez")
        case 6:
            print("\nÓtimo, nada melhor que trocar de conta.")
            nickname = input("Digite o seu nickname: ")
            id_jogador = int(input("Digite o seu ID: "))
            jogador1 = Jogador(nickname, id_jogador)
            plataforma.adicionar_jogador(jogador1)
        case 7:
            while True:
                print("\nÓtimo, nada melhor que jogar novos jogos.")
                print("Escolha um dos jogos disponíveis:")
                for jogo in jogador1.biblioteca_de_jogos:
                    print(jogo.titulo)
                nome_jogo = input("\nDigite o nome do jogo que você deseja jogar: ")
                jogador1.jogar(nome_jogo)
                op = input("\nDeseja jogar novamente jogo? (s/n): ").lower()
                if op == "s":
                    continue
                else:
                    break
            
        case 8:    
            break
        case _:
            print("Opção inválida, tente outra vez")

print("\nEncerrando programa...\nObrigado por usá-lo")