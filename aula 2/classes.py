class MinhaClasse:
    
    def __init__(self, att):
        self.meu_atributo = "Olá mundo"
        self.meu_atributo2 = att    
    def meu_metodo(self):
        print('Estou no metodo!')
    
    def meu_metodo2(self, num, mult):
        return num * mult
    
objeto = MinhaClasse()
result = objeto.meu_metodo2(3, 2)
print(result)
att = objeto.meu_metodo
print(att)