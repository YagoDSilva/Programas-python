class Calculadora:
    
    def calcular(self, op, num1, num2):
        if op == "+":
            return self.__adicionar(num1, num2)
        elif op == "-":
            return self.__subtrair(num1, num2)
        else:
            print("Operação Inválida")
            
    def __adicionar(self, num1, num2):
        return num1 + num2
    
    def __subtrair(self, num1, num2):
        return num1 - num2
op = input("Digite o operador: ")
Num1 = float(input("Num1: "))
Num2 = float(input("Num2: "))
calculadora = Calculadora()
resultado = calculadora.calcular(op, Num1, Num2)
print(resultado)