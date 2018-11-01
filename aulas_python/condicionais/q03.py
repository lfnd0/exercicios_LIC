'''lista = [0,-1,2,3,-2,1,5,-4,10,-3]

cont = 0

for num in lista:
    if num<0:
        cont = cont + 1
print('o numero de negativos e %d' % cont)'''

lista = []
continuar = True

while(continuar == True):
    n = int(input('digite valor: (0 para sair)'))
    if(n!=0):
        lista.append(n)
    else:
        continuar = False
        
print (lista)

cont = 0
for num in lista:
    if num<0:
        cont = cont + 1
print('o numero de negativos e %d % cont)