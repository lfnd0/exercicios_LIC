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