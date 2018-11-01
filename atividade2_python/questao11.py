#____________________questao11____________________

lista = []
n1 = 0
prx = 0
dif = 0
tam = int(input("Digite o tamanho do conjunto: "))
n2 = int(input("Digite o um valor para n: "))
for i in range(0,tam):
    n1 = int(input("Digite um número para o conjunto: "))
    lista.append(n1)
    if(i == 0):
        dif = abs(n2-n1) 
    elif(abs(n2-n1) < dif):
        dif = abs(n2-n1)
        prx = n1
print("No conjunto {}, o número mais próximo de {} é {}!".format(lista, n2, prx))