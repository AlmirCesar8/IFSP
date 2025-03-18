class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir_informaçoes(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")

#teste

joao = Pessoa("João", 47)
robert = Pessoa("Roberto", 26)

joao.exibir_informaçoes()
robert.exibir_informaçoes()