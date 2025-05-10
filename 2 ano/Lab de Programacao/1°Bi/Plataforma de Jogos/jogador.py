# Class Jogador:
class Jogador:

    def __init__(self, nickname, id_jogador):
        self.nickname = nickname
        self.id_jogador =id_jogador
        self.biblioteca_de_jogos = []
        self.saldo_carteira = 0.0

    def exibir_perfil(self):
        print(f"\nNickname: {self.nickname}\nID do jogador: { self.id_jogador}\nSaldo da carteira: R${self.saldo_carteira:.2f}")
        if not self.biblioteca_de_jogos:
            print("Biblioteca de jogos vazia")
        else:
            print("Biblioteca de Jogos:")
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
    
