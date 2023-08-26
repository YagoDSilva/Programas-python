print("Isso é um triângulo")

LadoA = float(input("Digite o lado A:  "))
LadoB = float(input("Digite o lado B:  "))
LadoC = float(input("Digite o lado C:  "))

if(LadoA + LadoB > LadoC and (LadoA + LadoC > LadoB) and (LadoB + LadoC > LadoA)):
    
    if (LadoA == LadoB) and (LadoB == LadoC):
        print("É um triângulo Equilátero")
        
    elif(LadoA == LadoB) or (LadoA == LadoC) or (LadoB == LadoC):
        print("É um triângulo triângulo isóceles")
        
    elif(LadoA != LadoB) or (LadoA != LadoC) or (LadoC != LadoB):
        print("É um triângulo escaleno")
        
else:
    print("Não é um triângulo")
