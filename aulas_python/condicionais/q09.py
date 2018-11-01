lista = [0,2, 5, 3, 5, 4, 6, 8,10,2]
n = int(input('digite n: '))

i = 0
while(i<len(lista) and lista[i]<=n):
    i = i+1
if(i==len(lista)):
    print('nao existe')
else:
    print('existe na posicao %d = %d' % (i,lista[i]))
    