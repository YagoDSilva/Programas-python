Tabuada = 1
print("Lembrando que vírgula é representada por ponto")
print("Multi usará somente os digitos antes do vírgula")
Número = float(input("Digite o número que quer multiplicar: "))
Multi = float(input("Quantas vezes deseja multiplicar esse número? "))

while (Tabuada <= Multi):
    Contas = float(Tabuada * Número)
    print(f"{Tabuada:.2f} * {Número:.2f} = {Contas:.2f}")
    Tabuada = Tabuada + 1    