#____________________questao5____________________

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