#Class Jogo
class Jogo:

    def __init__(self, titulo, genero, classificacao_etaria, preco):
        self.titulo = titulo
        self.genero = genero
        self.classificacao_etaria = classificacao_etaria
        self.preco = preco

    def exibir_detalhes(self):
        print(f"\nTítulo: {self.titulo}\nGênero: {self.genero}\nClassificacao Etaria: {self.classificacao_etaria}\nPreço: {self.preco}")