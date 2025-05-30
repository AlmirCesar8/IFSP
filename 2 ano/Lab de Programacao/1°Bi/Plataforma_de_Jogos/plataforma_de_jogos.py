from jogos_catalogados import catalogo_de_jogos
# Class PlataformaDeJogos
class PlataformaDeJogos:
    def __init__(self, nome_plataforma):
        self.nome_plataforma = nome_plataforma
        self.catalogo_de_jogos = catalogo_de_jogos
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
        jogador = self.buscar_jogador_por_id(id_jogador_comprador)
        jogo_catalogo = self.buscar_jogo_por_titulo(titulo_jogo_desejado)
        verificacao_biblioteca = False

        if jogador is not False and jogo_catalogo is not None:
            for jogo_biblioteca in jogador.biblioteca_de_jogos:
                if jogo_biblioteca.titulo.lower() == titulo_jogo_desejado.lower():
                    verificacao_biblioteca = True

            if not verificacao_biblioteca:
                if jogador.debitar_saldo(jogo_catalogo.preco) is not False:
                    jogador.adicionar_jogo_biblioteca(jogo_catalogo)
                    print("Compra realizada com sucesso.")
                else:
                    print("Sem saldo para compra. Adicione saldo à sua conta")
            else:
                print("Você já tem este jogo. Tente comprar outro.")
        else:
            print("Jogo/Jogador não encontrado. Tente outra vez.")
            
    def presentear_jogo(self, id_jogador_comprador, titulo_jogo_desejado, id_jogador_presenteado):
        self.id_jogador_comprador = id_jogador_comprador
        self.titulo_jogo_desejado = titulo_jogo_desejado
        self.id_jogador_presenteado = id_jogador_presenteado
        jogador_comprador = self.buscar_jogador_por_id(self.id_jogador_comprador)
        jogador_presenteado = self.buscar_jogador_por_id(self.id_jogador_presenteado)
        jogo = self.buscar_jogo_por_titulo(self.titulo_jogo_desejado)
        verificacao_biblioteca = False
        
        for jogo in jogador_presenteado.biblioteca_de_jogos:
            if jogo.titulo.lower() == titulo_jogo_desejado.lower():
                verificacao_biblioteca = True
        
        if jogador_comprador is not False and jogador_presenteado is not False and jogo is not None:
            if verificacao_biblioteca == False:
                if jogador_comprador.debitar_saldo(jogo.preco) is not False:
                    jogador_presenteado.adicionar_jogo_biblioteca(jogo)
                    print("Jogo presenteado com sucesso.")
                else:
                    print("Sem saldo para presentear. Adicione saldo à sua conta")
            else:
                print(f"{jogador_presenteado.nickname} já tem este jogo. Tente presentear outro.")
        else:
            print("Jogo/Jogador não encontrado. Tente outra vez.")

