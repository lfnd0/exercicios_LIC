lista = [930,930,1150,1430,2140,2570,2580,3250,3420,4350]
saldo = 10000

i = 0
while(i<len(lista) and saldo >= lista[i]):
    print('funcionario %d recebe %.2f' % (i,lista[i]))
    saldo = saldo - lista[i]
    i = i+1
    print(saldo)    
    