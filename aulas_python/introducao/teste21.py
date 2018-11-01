x = int(input("Digite um número: ")) 
y = int(input("Digite outro número: "))
if x > y:
    x = x + 2
    print("O número {} é maior que {}!".format(x , y))
elif y < x:
    y = y + 2
    print("O número {} é maior que {}!".format(y, x))
    else:
        print("Os dois números são iguais!")