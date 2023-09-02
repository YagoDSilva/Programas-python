def f():
    b = float(input("Escreva um número"))

    def f1():
        nonlocal b
        b = b ** b
        print("f1 b={}".format(b))
 
    def f2():
        global b
        b = b ** b
        print("f2 b={}".format(b))
 
    f1()
    f2()

b = 10
f()