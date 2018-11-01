def existe(lista, valor):
    i = 0
    while(i<len(lista) and lista[i]!=valor):
        i = i+1
    if(i==len(lista)):
        return False
    else:
        return True
    
def copia(lista):
    lista_copia = [lista[0]]
    for i in range(1,len(lista)):
        print('analisando elemento %d'%lista[i])
        busca = existe(lista_copia,lista[i])
        if(busca==False):
            print('\telemento nao existe na copia => adicione!')
            lista_copia.append(lista[i])
        else:
            print('\telemento ja existe na copia')
    return lista_copia

lista = [2, 3, 8, 5, 3, 4, 5, 7, 2, 4] 
print(copia(lista))
