i = int(input("Digite a idade: "))
o = input("Digite a ocupação: ")
p = 20
if (i > 18 and i < 60):
    if o == "estudante":
        p = 12
    elif o == "professor":
        p = 15
    else:
        p = 20
else:
    p = 10
print("O valor a ser pago é: R$ ", p, ".00")