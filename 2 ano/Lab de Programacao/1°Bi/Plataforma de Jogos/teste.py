from jogo import Jogo
from jogador import Jogador
from plataforma_de_jogos import PlataformaDeJogos

# Exemplo de uso do sistema de plataforma de jogos

plataforma = PlataformaDeJogos("GameBlin")

# Criando jogos
jogo1 = Jogo("The Legend of Zelda", "Aventura", "10+", 59.99)
jogo2 = Jogo("Super Mario Bros", "Plataforma", "E", 49.99)
jogo3 = Jogo("Call of Duty", "Tiro", "18+", 79.99)

plataforma.adicionar_jogo_catalogo(jogo1)
plataforma.adicionar_jogo_catalogo(jogo2)
plataforma.adicionar_jogo_catalogo(jogo3)

# Criando jogadores
jogador1 = Jogador("PlayerOne", 1)
jogador2 = Jogador("PlayerTwo", 2)

jogador1.adicionar_saldo(100.00)
jogador2.adicionar_saldo(30.00)

plataforma.adicionar_jogador(jogador1)
plataforma.adicionar_jogador(jogador2)

#Testes

plataforma.listar_jogos_catalogo()

plataforma.realizar_compra(jogador1.id_jogador, "Call of Duty")
jogador1.exibir_perfil()
plataforma.realizar_compra(jogador1.id_jogador, "Call of Duty")

plataforma.realizar_compra(jogador2.id_jogador, "Super Mario Bros")
jogador2.adicionar_saldo(100)
plataforma.realizar_compra(jogador2.id_jogador, "Super Mario Bros")
jogador2.exibir_perfil()