class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def atualizar_quantidade(self):
        valor = int(input("Digite a quantidade que deseja adicionar: "))
        self.quantidade += valor
        return self.quantidade
    def calcular_valor_total(self):
        return self.preco * self.quantidade
def exibir (Produto):
    print(f"Quantidade: {Produto.atualizar_quantidade()}\nValor total: {Produto.calcular_valor_total()}")
    
pao = Produto("Pão", 1.2, 11)
bolacha = Produto("Bolacha", 3.5, 4)

exibir(pao)
exibir(bolacha)