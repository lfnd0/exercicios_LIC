def maior(lista):
    max = lista[0]
    for i in range(len(lista)):
        if lista[i]>max:
            max = lista[i]
    return max

lista = [2,5,6,4,7,8]
print(maior(lista))
