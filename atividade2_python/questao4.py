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