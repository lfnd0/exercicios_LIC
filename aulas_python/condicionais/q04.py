lista = [0,2, 5, 3, 5, 4, 6, 8,10,2]

#calculando a media

soma = 0
media = float
for i in lista:
    soma = soma + i
media = soma/len(lista)

print(media)

for i in lista:
    if i < media:
        print(i)