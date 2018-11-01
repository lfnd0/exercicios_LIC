lista = [0,2, 5, 3, 5, 4, 6, 8,10,2]
n = 11

prox = lista[0]
i = 1
print('ok1')
while(i<len(lista) and lista[i]!=n):
    if(abs(n-lista[i])<abs(n-prox)):
        prox = lista[i]
    i = i + 1
print('ok2')
if(i<len(lista)):
    prox = lista[i]
print('ok3')
print('o mais proximo e: %d' % prox)
print('ok4')
    