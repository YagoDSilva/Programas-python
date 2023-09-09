class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf #"__"deixa a informação privada
        
    def correr(self):
        print("Estou correndo")
        
    def beber(self, bebida):
        if bebida == "cerveja":#condicional para exibição do documento
            self.__apresentar_documento()
        print("bebendo...")
        
    def __apresentar_documento(self):
        print(self.__cpf)
        
        
ronaldo = Pessoa("Ronaldo", 32, "83475jhfsk")
ronaldo.beber("cerveja")
#ronaldo.beber("coca-cola") #ativar para resultado bebendo