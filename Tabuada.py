Tabuada = 1

Menu = float(input("Escolha a função que deseja usar\n1.Soma\n2.Subtração\n3.multiplicação\n4.Divisão\n5.Tabuada\n6.Sair\n"))


    
class Numeros():
    def Num1(self, Num1) -> float: 
        Num1 = float(input("Insira o primeiro número: "))
    def Num2(self, num2) -> float: 
        num2 = float(input("Insira o segundo número: "))



    
class operacoes():
        
    def Som():
        Num1 = float(input("Digite o primeiro número: "))
        Num2 = float(input("Digite o segundo número: "))
        Soma = Num1 + Num2
        print (f"{Num1:.2f} + "f"{Num2:.2f} = "f"{Soma:.2f}")
        
    def Sub():
        Num1 = float(input("Digite o primeiro número: "))
        Num2 = float(input("Digite o segundo número: "))
        Subs = Num1 - Num2
        print (f"{Num1:.2f} + "f"{Num2:.2f} = "f"{Subs:.2f}")
        
    def Tab():
        Número = float(input("Digite o número que quer multiplicar: "))
        Multi = float(input("Quantas vezes deseja multiplicar esse número? "))

        while (Tabuada <= Multi):
            Contas = float(Tabuada * Número)
            print(f"{Tabuada:.2f} * {Número:.2f} = {Contas:.2f}")
            Tabuada = Tabuada + 1    
    

if (Menu == 1):
    operacoes.Som()
    
    

