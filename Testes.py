Tabuada = 1
print("Lembrando que vírgula é representada por ponto")
Número = float(input("Digite o número que quer multiplicar: "))
Bah = Multi = float(input("Quantas vezes deseja multiplicar esse número? "))
if(Multi == int):
    while (Tabuada <= Multi):
        Contas = float(Tabuada * Número)
        print(f"{Tabuada:.2f} * {Número:.2f} = {Contas:.2f}")
        Tabuada = Tabuada + 1
        
else:
    print("Digite um número inteiro")
    input (Bah)
    