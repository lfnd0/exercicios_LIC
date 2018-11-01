#____________________questao6____________________

lista = []
ma = 0
mi = 0
amp = 0
n = 0
tam = int(input("Digite a quantidade de números que irão compor o conjunto: "))
for i in range(0, tam):
    n = int(input("Digite um valor para compor o conjunto: "))
    lista.append(n)
    if(i == 0):
        ma = n
        mi = n
    elif(n > ma):
        ma = n
    else:
        mi = n
amp = ma - mi
print("A amplitude do conjunto {} é: {}." .format(lista, amp))