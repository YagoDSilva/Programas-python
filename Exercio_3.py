#condicional de turno

turno = input("Digite em que turno vocês estuda\ndigite 'M' para Matutino, V para Vespertino ou N para noturno:  ").upper()

if(turno == "M"):
    print("Bom Dia")
    
elif(turno == "V"):
    print("Boa Tarde")
    
elif(turno == "N"):
    print("Boa noite")
    
else:
    print("Valor inválido")