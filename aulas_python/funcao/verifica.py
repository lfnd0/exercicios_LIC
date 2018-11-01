def verifica(lista, valor):
    i = 0
    while(i<len(lista) and lista[i]!=valor):
        i = i+1
    if(i==len(lista)):
        print('nao existe')
    else:
        print('achou')
        
def verifica2(lista, valor):
    existe = False
    for i in lista:
        if(i == valor):
            existe = True
    if(existe == True):
        print('existe')
    else:
        print('nao existe')

verifica2([2,5,6,4,7,8], 4)
