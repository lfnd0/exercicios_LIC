#____________________questao1____________________

n = int(input("Digite o número para calcular seu fatorial: "))
fat = 1
i = 1
while(i <= n):
    fat = fat * i
    i = i + 1
print("O valor do fatorial é: %d." %fat)


#____________________questao2____________________

n = int(input("Digite o número para calcular seu valor de acordo com a Sequência de Fibonacci: "))
fib = 0
a = 1
b = 0
i = 1
while (i<=n):
    fib = a + b
    a = b
    b = fib
    i = i + 1
print("O valor conforme a sequência de Fibonacci é: %d." %fib)


#____________________questao3____________________
lista = []
count = 0
n = 0
tam = int(input("Digite a quantidade de números que esse conjunto terá: "))
for n in range(0, tam):
    n = int(input("Digite um número que irá compor esse conjunto: "))
    lista.append(n)
print("No conjunto {}." .format(lista))
for n in lista:
    if(n<0):
        count = count + 1
print("A quantidade de número(s) negativo(s) é %d." %count)


#____________________questao4____________________

lista = []
tam = int(input("Digite a quantidade de números que esse conjunto terá: "))
n = 0
soma = 0
media = 0
for n in range(0,tam):
    n = int(input("Digite um número para compor o conjunto: "))
    lista.append(n)
    soma = soma + n
    media = soma/tam
print("Esse conjunto possui a média {}." .format(media))
for n in lista:
    if(n < media):
        print("O número %d está abaixo da média desse conjunto." %n)


#____________________questao5____________________

lista = []
count = 0
n1 = 0
tam = int(input("Digite a quantidade de números que irá compor o conjunto: "))
n2 = int(input("Digite o valor de n: "))
for i in range(0, tam):
    n1 = int(input("Digite um número para compor o conjunto: "))
    lista.append(n1)
    if(n1 > n2):
        count = count + 1
print("No conjunto: {}. Existe(m) {} número(s) maior(es) que {}." .format(lista, count, n2))


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
    n = int(input("Digite um número para compor o conjunto B: "))
    listaB.append(n)
for i in range(0, tam):
    euc = euc + ((listaA[i] - listaB[i])**2)
    result = euc ** (1/2)
print("A distância euclidiana entre os conjuntos A e B é de %.2f." %result)


#____________________questao8____________________

lista = []
n = 0
tam = int(input("Digite o tamanho do conjunto: "))
for i in range(0, tam):
    n = int(input("Digite um número para compor o conjunto: "))
    lista.append(n)
for n in lista:
    if(n<0):
        print("No conjunto {}, existe número negativo." .format(lista))


#____________________questao9____________________

lista = []
n1 = 0
tam = int(input("Digite a quantidade de números que irá compor o conjunto: "))
n2 = int(input("Digite o valor de n: "))
for i in range(0, tam):
    n1 = int(input("Digite um número para compor o conjunto: "))
    lista.append(n1)
print("No conjunto {}." .format(lista))
if(n1 > n2):
    print("Existe(m) número(s) maior(es) que {}." .format(n2))
else:
    print("Não existe número maior que {}." .format(n2))


#____________________questao10____________________

lista = []
tam = int(input("Digite a quantidade de números que esse conjunto terá: "))
n = 0
soma = 0
media = 0
for n in range(0,tam):
    n = int(input("Digite um número para compor o conjunto: "))
    lista.append(n)
    soma = soma + n
    media = soma/tam
print("Esse conjunto possui a média {}." .format(media))
for n in lista:
    if(n < media):
        print("O número %d está abaixo da média desse conjunto." %n)


#____________________questao11____________________

lista = []
n1 = 0
prx = 0
dif = 0
tam = int(input("Digite o tamanho do conjunto: "))
n2 = int(input("Digite um valor para n: "))
for i in range(0,tam):
    n1 = int(input("Digite um número para o conjunto: "))
    lista.append(n1)
    if(i == 0):
        dif = abs(n2-n1) 
    elif(abs(n2-n1) < dif):
        dif = abs(n2-n1)
        prx = n1
print("No conjunto {}, o número mais próximo de {} é {}!".format(lista, n2, prx))


#____________________questao12____________________

lista = []
count = 0
n1 = 0
tam = int(input("Digite a quantidade de números que irão compor o conjunto: "))
n2 = int(input("Digite o valor de n: "))
for i in range(0, tam):
    n1 = int(input("Digite um número para compor o conjunto: "))
    lista.append(n1)
    if(n1 > n2):
        count = count + 1
print("No conjunto: {}. Existe(m) {} número(s) maior(es) que {}." .format(lista, count, n2))

#____________________questao13____________________

pal = input("Digite uma palavra: ")
inv = pal[::-1]
print("O inverso da palavra digitada é:", inv)


#____________________questao14____________________

pal = str(input("Digite uma palavra: "))
car = str(input("Digite a letra que você deseja contar na palavra: "))
count = 0
for i in pal:
    if(i == car):
        count = count + 1
print("Na palava {}, a letra {} aparece {} vez(es)." .format(pal, car, count))


#____________________questao15____________________

pal = str(input("Digite uma palavra: "))
count = 0
for i in pal:
    if(i == 'a'):
        count = count + 1
    if(i == 'e'):
        count = count + 1
    if(i == 'i'):
        count = count + 1
    if(i == 'o'):
        count = count + 1
    if(i == 'u'):
        count = count + 1
print("A palavra: {}, possui {} vogal(is)." .format(pal, count))


#____________________questao16____________________
lista = []
n3 = 0
tam = int(input("Digite o tamanho do conjunto: "))
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
for i in range(0,tam):
    n3 = int(input("Digite um número para a composição do conjunto: "))
    lista.append(n3)
    i = 0
while i < tam and (lista[i] != n1 or lista[i+1] != n2):
    i = i + 1
if (i == tam):
    print("Os números {} e {} não ocorrem em sequência no conjunto.".format(n1, n2))
else:
    print("O números {} e {} ocorrem em sequência no conjunto.".format(n1, n2))


#____________________questao17____________________

lista = []
ma = 0
mi = 0
amp = 0
n = 0
tam = int(input("Digite a quantidade de números que irá compor o conjunto: "))
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