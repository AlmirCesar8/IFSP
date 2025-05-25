from jogo import Jogo
class JogoForca(Jogo):
    def __init__(self, titulo, genero, classificacao_etaria, preco):
        super().__init__(titulo, genero, classificacao_etaria, preco)
        self.listaPalavras = ["cachorro", "abelha", "gato", "elefante", "girafa", "tigre", "macaco", "cavalo", "zebra", "pinguim"]
        self.vida = 6
        self.palavraSelecionada = self.listaPalavras[self.escolhaPalavra()]
        self.acumulador = []
        self.letrasTestadas = []
        for i in range(len(self.palavraSelecionada)):
            self.acumulador.append("_")

    def escolhaPalavra(self):
        import random
        return random.randint(0,len(self.listaPalavras)-1)

    def desmenbrarPalavra(self):
        return list(self.listaPalavras[self.escolhaPalavra()])

    def verificarLetra(self, letra):
        self.letra = letra.lower()
        if self.letra in self.letrasTestadas:
            print(f"Você já testou a letra '{self.letra}'. Tente outra.")
            return
        self.letrasTestadas.append(self.letra)

        if self.letra in self.palavraSelecionada:
            for index, char in enumerate(self.palavraSelecionada):
                if char == letra:
                    self.acumulador[index] = letra
            print(f"Correto! A letra '{letra}' está na palavra.\nVoce ainda tem {self.vida} vidas\nPalavra: {self.acumulador}\nLetras testadas: {self.letrasTestadas}\n")
        else: 
            self.vida -= 1
            print(f"Errado, '{self.letra}' não está na palavra. \nVoce ainda tem {self.vida} vidas\n{self.acumulador}\n{self.letrasTestadas}\n")
    def jogar(self):
        print("-----------Bem-vindo ao Jogo da Forca-----------")
        print(f"A palavra selecionada tem {len(self.palavraSelecionada)} letras")
        print(f"Você tem {self.vida} vidas para adivinhar a palavra.")
        
        while True:
            if not "_" in self.acumulador:
                print(f"Parabéns, você ganhou\nA palavra era '{self.palavraSelecionada}'\nSobraram {self.vida} vidas")
                break
            if self.vida == 0:
                print(f"Suas tentativas se esgotaram\nA palavra era {self.palavraSelecionada}")
                break

            letra = input("Digite uma letra: ")
            if len(letra) != 1 or not letra.isalpha():
                print("Digite apenas UMA letra válida.")
                continue
            self.verificarLetra(letra)


