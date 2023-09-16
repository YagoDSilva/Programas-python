Tabuada = 1

Menu = input("Escolha a função que deseja usar\n1.Soma\n2.Subtração\n3.multiplicação\n4.Divisão\n5.Tabuada\n6.Sair\n")


    
class Numeros():
    Num1 = float(input("Insira o primeiro número: "))
    Num2 = float(input("Insira o segundo número: "))

class operacoes():
        
    def Som():
        Num1 = Numeros.Num1
        Num2 = Numeros.Num2
        float(Num1)
        float(Num2)
        Soma = Num1 + Num2
        print (f"{Num1:.2f} + "f"{Num2:.2f} = "f"{Soma:.2f}")
        
    def Sub():
        Num1()
        Num2()
        
    def Tab():
        Número = float(input("Digite o número que quer multiplicar: "))
        Multi = float(input("Quantas vezes deseja multiplicar esse número? "))

        while (Tabuada <= Multi):
            Contas = float(Tabuada * Número)
            print(f"{Tabuada:.2f} * {Número:.2f} = {Contas:.2f}")
            Tabuada = Tabuada + 1    
    


    

