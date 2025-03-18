class Animal:
    def emitir_som(self):
        pass
class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au")
class Gato(Animal):
    def emitir_som(self):
        print("Miau")
        
cachorro = Cachorro()
gato = Gato()

cachorro.emitir_som()
gato.emitir_som()