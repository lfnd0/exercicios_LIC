lista = [0,2, 5, 3, 5, 4, 6, 8,10,2]
n = int(input('digite n: '))

cont = 0
for i in lista:
    if i>n:
        cont = cont + 1
print(cont)