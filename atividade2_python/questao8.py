#____________________questao8____________________

lista = []
i = 0
tam = int(input("Digite o tamanho do conjunto: "))
for i in range(0, tam):
    n = int(input("Digite um número para compor o conjunto: "))
    lista.append(n)
while(i<len(lista) and lista[i]>=0):
    i = i + 1
if(i==len(lista)):
    print("No conjunto {}, não existe número negativo." .format(lista))
else:
    print("No conjunto {}, existe número negativo." .format(lista))