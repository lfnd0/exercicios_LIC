#____________________questao9____________________

lista = []
n1 = 0
tam = int(input("Digite a quantidade de números que irão compor o conjunto: "))
n2 = int(input("Digite o valor de n: "))
for i in range(0, tam):
    n1 = int(input("Digite um número para compor o conjunto: "))
    lista.append(n1)
print("No conjunto {}." .format(lista))
if(n1 > n2):
    print("Existe(m) número(s) maior(es) que {}." .format(n2))
else:
    print("Não existe número maior que {}." .format(n2))