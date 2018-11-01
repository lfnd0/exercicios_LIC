def max_num(lista):
    maior = 0
    for num in lista:
        if num>maior:
            maior = num
    return maior

def min_num(lista):
    menor = lista[0]
    for num in lista:
        if num<menor:
            menor = num
    return menor

def calc_notas(lista_notas):
    maior_nota = max_num(lista_notas)
    menor_nota = min_num(lista_notas)
    print(maior_nota)
    print(menor_nota)

    nova_lista = []
    for nota in lista_notas:
        nova_lista.append(((nota - menor_nota)/(maior_nota - menor_nota))*10)
    return nova_lista

def calc_notas2(lista_notas):
    maior_nota = max_num(lista_notas)

    nova_lista = []
    for nota in lista_notas:
        nova_lista.append(round((nota/maior_nota)*10,2))
    return nova_lista
    

print(calc_notas2([8.0,7.0,5.5,9.0,8.6,4.3,4.0,6.0]))








































































  
    
    
    
    
    
    
    
    
    
    
    













