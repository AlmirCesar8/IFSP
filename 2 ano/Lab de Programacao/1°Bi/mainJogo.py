class Jogo:

    def __init__(self, titulo, genero, classificacao_etaria, preco):
        self.titulo = titulo
        self.genero = genero
        self.classificacao_etaria = classificacao_etaria
        self.preco = preco

    def exibir_detalhes(self):
        print(f"\nTítulo: {self.titulo}\nGênero: {self.genero}\nClassificacao Etaria: {self.classificacao_etaria}\nPreço: {self.preco}")

class Jogador:

    def __init__(self, nickname, id_jogador):
        self.nickname = nickname
        self.id_jogador =id_jogador
        self.biblioteca_de_jogos = []
        self.saldo_carteira = 0.0

    def exibir_perfil(self):
        print(f"\nNickname: {self.nickname}\nID do jogador: { self.id_jogador}\nSaldo da carteira: R${self.saldo_carteira:.2f}\nBiblioteca de Jogos:")
        for jogo in self.biblioteca_de_jogos:
            jogo.exibir_detalhes()

    def adicionar_jogo_biblioteca(self, jogo):
        self.biblioteca_de_jogos.append(jogo)

    def adicionar_saldo(self, valor):
        self.valor = valor
        self.saldo_carteira += self.valor        

    def debitar_saldo(self, debito):
        self.debito = debito

        if self.debito <= self.saldo_carteira:
            self.saldo_carteira -= self.debito
            return True
        else:
            return False

class PlataformaDeJogos:
    def __init__(self, nome_plataforma):
        self.nome_plataforma = nome_plataforma
        self.catalogo_de_jogos = []
        self.jogadores_cadastrados = []

    def adicionar_jogo_catalogo(self, novo_jogo):
        self.catalogo_de_jogos.append(novo_jogo)

    def adicionar_jogador(self, novo_jogador):
        self.jogadores_cadastrados.append(novo_jogador)

    def buscar_jogo_por_titulo(self, titulo):
        for jogo in self.catalogo_de_jogos:
            if jogo.titulo.lower() == titulo.lower():
                return jogo
        return None    

    def buscar_jogador_por_id(self, id):
        for jogador in self.jogadores_cadastrados:
            if jogador.id_jogador == id:
                return jogador
        return False
    
    def listar_jogos_catalogo(self):
        for jogo in self.catalogo_de_jogos:
            jogo.exibir_detalhes()
            print()

    def realizar_compra(self, id_jogador_comprador, titulo_jogo_desejado):
        self.id_jogador_comprador = id_jogador_comprador
        self.titulo_jogo_desejado = titulo_jogo_desejado
        jogador = self.buscar_jogador_por_id(self.id_jogador_comprador)
        jogo = self.buscar_jogo_por_titulo(self.titulo_jogo_desejado)
        verificacao_biblioteca = False

        for jogo in jogador.biblioteca_de_jogos:
            if jogo.titulo.lower() == titulo_jogo_desejado.lower():
                verificacao_biblioteca = True
        
        if jogador is not None and jogo is not False:
            if verificacao_biblioteca == False:
                if jogador.debitar_saldo(jogo.preco) is not False:
                    jogador.adicionar_jogo_biblioteca(jogo)
                    print("Compra realizada com sucesso")
                else:
                    print("Sem saldo para compra")
            else:
                print("Você já tem este jogo. Tente comprar outro")
        else:
            print("Jogo/Jogador não encontrado. Tente outra vez")

            
# Criando uma instância da plataforma
plataforma = PlataformaDeJogos("GameBlin")
# Criando algumas instâncias de Jogo
jogo1 = Jogo("The Legend of Zelda", "Aventura", "10+", 59.99)
jogo2 = Jogo("Super Mario Bros", "Plataforma", "E", 49.99)
jogo3 = Jogo("Call of Duty", "Tiro", "18+", 79.99)
# Adicionando jogos ao catálogo da plataforma
plataforma.adicionar_jogo_catalogo(jogo1)
plataforma.adicionar_jogo_catalogo(jogo2)
plataforma.adicionar_jogo_catalogo(jogo3)
# Criando algumas instâncias de Jogador
jogador1 = Jogador("PlayerOne", 1)
jogador2 = Jogador("PlayerTwo", 2)
# Adicionando saldo inicial a alguns jogadores
jogador1.adicionar_saldo(100.00)  # PlayerOne tem R$100,00
jogador2.adicionar_saldo(30.00)    # PlayerTwo tem R$30,00
#
plataforma.adicionar_jogador(jogador1)
plataforma.adicionar_jogador(jogador2)

plataforma.listar_jogos_catalogo()

plataforma.realizar_compra(jogador1.id_jogador, "Call of Duty")
jogador1.exibir_perfil()
plataforma.realizar_compra(jogador1.id_jogador, "Call of Duty")

plataforma.realizar_compra(jogador2.id_jogador, "Super Mario Bros")
jogador2.adicionar_saldo(100)
plataforma.realizar_compra(jogador2.id_jogador, "Super Mario Bros")
jogador2.exibir_perfil()