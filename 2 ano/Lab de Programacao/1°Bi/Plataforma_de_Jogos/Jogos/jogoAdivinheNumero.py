from jogo import Jogo
class JogoAdivinheNumero(Jogo):
    def __init__(self, titulo, genero, classificacao_etaria, preco):
        super().__init__(titulo, genero, classificacao_etaria, preco)
        self.tentativas = 0
        self.dificuldade = None
        self.numeroSecreto = None
        
    def sortear_numero(self):
        import random
        if self.dificuldade == 1:
            return random.randint(1, 10)
        elif self.dificuldade == 2:
            return random.randint(1, 100)
        elif self.dificuldade == 3:
            return random.randint(1, 1000)

    def jogar(self):
        print("-----------Bem-vindo ao Adivinhe o Número-----------")
        print("O número secreto será sorteado entre 1 e 10 (Fácil), 1 e 100 (Médio) ou 1 e 1000 (Difícil).")
        while True:
            try:
                self.dificuldade = int(input("Escolha a dificuldade (1 - Fácil, 2 - Médio, 3 - Difícil): "))
                if self.dificuldade not in [1, 2, 3]:
                    print("Dificuldade inválida. Definindo dificuldade Fácil (1).")
                    self.dificuldade = 1
                break
            except ValueError:
                print("Por favor, digite um número válido para a dificuldade.\n")
        self.numeroSecreto = self.sortear_numero()
        while True:
            try:
                self.numeroTentativa = int(input("Digite o número: "))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
            
            self.tentativas += 1
            if (self.numeroSecreto == self.numeroTentativa):
                print(f"Parabéns, você acertou o número secreto em {self.tentativas} tentativas!")
                print(f"O número secreto era {self.numeroSecreto}")
                break
            elif(self.numeroSecreto < self.numeroTentativa):
                print("Número incorreto")
                print("O número é menor")
            else: 
                print("Número incorreto")
                print("O número é maior")
