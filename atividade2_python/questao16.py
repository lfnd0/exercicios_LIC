#____________________questao16____________________
lista = []
n3 = 0
tam = int(input("Digite o tamanho do conjunto: "))
n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
for i in range(0,tam):
    n3 = int(input("Digite um número para composição do conjunto: "))
    lista.append(n3)
    i = 0
while i < tam and (lista[i] != n1 or lista[i+1] != n2):
    i = i + 1
if (i == tam):
    print("Os números {} e {} não ocorrem em sequência no conjunto!".format(n1, n2))
else:
    print("O números {} e {} ocorrem em sequência no conjunto!".format(n1, n2))