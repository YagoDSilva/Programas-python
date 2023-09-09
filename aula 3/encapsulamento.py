class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf #"__"deixa a informação privada
        
    def print_cpf(self):
        print(self.__cpf)
        
        
ronaldo = Pessoa("Ronaldo", 32, "83475jhfsk")
print(ronaldo.nome)
print(ronaldo.idade)
ronaldo.print_cpf#permite que o programa funcione propriamente.