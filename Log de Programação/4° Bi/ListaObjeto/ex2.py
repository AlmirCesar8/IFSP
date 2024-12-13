class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir_detalhes(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\n")
 
c1 = Carro("Ferrari", "R45", "2000")
c2 = Carro("Toyota", "234745", "2024")

c1.exibir_detalhes()
c2.exibir_detalhes()