class Pessoa:
    
    def __init__(self, nome, idade):
        self.name = nome
        self.idade = idade
        
    def dirigir(self, veiculo):
        print("Dirigindo um(a) {}".format(veiculo))
        
    def cantar(self):
        print("Lalala")
        
    def apresentar_idade(self):
        return self.idade
        