lista = [0,2, 5, 3, 5, 4, 6, 8,10,2]

i = 0
while(i<len(lista) and lista[i]>=0):
    i = i+1
    
if(i==len(lista)):
    print('nao existe negativo')
else:
    print('negativo na posicao %d: %d' % (i,lista[i]))
    
