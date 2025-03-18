class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        self.__saldo += valor
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo Insuficiente")
    def exibir_saldo(self):
        print(f"Seu saldo atual é: {self.__saldo}")
        
c1 = ContaBancaria("Alberto", 1000)
c1.depositar(4000)
c1.sacar(10000)
c1.exibir_saldo()