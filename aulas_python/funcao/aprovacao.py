def aprovacao(lista):
    ab1 = (lista[0]+lista[1])/2
    ab2 = (lista[2]+lista[3])/2
    
    if(ab1>=7 and ab2>=7):
        print('aprovado')
    elif(ab1<=ab2):
        print('reposicao da ab1')
    else:
        print('reposicao da ab2')
    
lista = [3, 3, 2, 2]
aprovacao(lista)
