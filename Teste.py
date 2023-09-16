def menu():
    Menu = float(input("Escolha a função que deseja usar\n1.Soma\n2.Subtração\n3.multiplicação\n4.Divisão\n5.Tabuada\n6.Sair\n"))
    
class Operacoes:
    @staticmethod
    def Soma():
        Num1 = float(input("Digite o primeiro número: "))
        Num2 = float(input("Digite o segundo número: "))
        Soma = Num1 + Num2
        print(f"{Num1:.2f} + {Num2:.2f} = {Soma:.2f}")

    @staticmethod
    def Subtracao():
        Num1 = float(input("Digite o primeiro número: "))
        Num2 = float(input("Digite o segundo número: "))
        Subtracao = Num1 - Num2
        print(f"{Num1:.2f} - {Num2:.2f} = {Subtracao:.2f}")

    @staticmethod
    def Multiplicacao():
        Num1 = float(input("Digite o primeiro número: "))
        Num2 = float(input("Digite o segundo número: "))
        Multiplicacao = Num1 * Num2
        print(f"{Num1:.2f} * {Num2:.2f} = {Multiplicacao:.2f}")

    @staticmethod
    def Divisao():
        Num1 = float(input("Digite o primeiro número: "))
        Num2 = float(input("Digite o segundo número: "))
        if Num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            Divisao = Num1 / Num2
            print(f"{Num1:.2f} / {Num2:.2f} = {Divisao:.2f}")

def Tabuada():
    Numero = float(input("Digite o número que deseja multiplicar: "))
    Multi = int(input("Quantas vezes deseja multiplicar esse número? "))

    for Tabuada in range(1, Multi + 1):
        Contas = Numero * Tabuada
        print(f"{Numero:.2f} * {Tabuada} = {Contas:.2f}")

while True:
    print("\nMenu:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Tabuada")
    print("6. Sair")

    escolha = int(input("Escolha a função que deseja usar: "))

    if escolha == 1:
        Operacoes.Soma()
    elif escolha == 2:
        Operacoes.Subtracao()
    elif escolha == 3:
        Operacoes.Multiplicacao()
    elif escolha == 4:
        Operacoes.Divisao()
    elif escolha == 5:
        Tabuada()
    elif escolha == 6:
        print("Saindo do programa.")
        break
    else:
        print("Escolha inválida. Tente novamente.")