lista = [10,9,14,28,31,7,42,33,7,18,23,7,42]
premio = 100

#passo1 - encontrar maior e menor
maior = lista[0]
menor = lista[0]

for bilhete in lista:
    if(bilhete>maior):
        maior = bilhete
    elif(bilhete<menor):
        menor = bilhete
print(maior)
print(menor)

#passo2 - encontrar e contar os premiados
count = 0
for i in range(0,len(lista)):
    if(lista[i]==maior or lista[i]==menor):
        print('o bilhete %d foi premiado'%i)
        count += 1 
print(count)

#passo 3 - calcular premio
print('premio para cada ganhador = {:.2f}'.format(premio/count))




