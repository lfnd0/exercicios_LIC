lista = [10,2, 5, 100, 5, 4, 6, 8,10,2]

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero>maior:
        maior = numero
    elif numero < menor:
        menor = numero
        
#print(maior)
print(max(lista))
print(min(lista))
print('Amplitude = %d' %(maior-menor))
