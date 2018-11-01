#____________________questao7____________________

listaA = []
listaB = []
n = 0
euc = 0
result = 0
tam = int(input("Digite o tamanho para os conjunto A e B: "))
for i in range(0, tam):
    n = int(input("Digite um número para compor o conjunto A: "))
    listaA.append(n)
for i in range(0, tam):
    n = int(input("Digite um número para compor o conunto B: "))
    listaB.append(n)
for i in range(0, tam):
    euc = euc + ((listaA[i] - listaB[i])**2)
    result = euc ** (1/2)
print("A distância euclidiana entre os conjuntos A e B é de %.2f." %result)