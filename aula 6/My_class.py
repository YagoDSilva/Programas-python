class MinhaClasse:
    
    estatico = "Batata"
    
    def __init__(self, estado):
        self.estado = estado
        

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)


obj1.estatico = "Programador"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)