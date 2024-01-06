from threading import Event
delay = 1
b = 0
c = 0
while(c <=9):
    while(b <=9):
        Event().wait(delay)
        b = b+1
        print(b)
    while(b > 9):  # Adicionar And para C menor igual 9
        Event().wait(delay)
        b = b-9
        c = c+1
        print(f"c ={c}")
        print(b)
        
        # Adicionar while igual o anterior mas sem print (b)
    
    
