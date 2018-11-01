#solucao 1
n = int(input('digite numero: '))

fat = 1
for i in range(n,1,-1):
    fat = fat*i
    
print('o fatorial de %d e %d' % (n,fat))

"""
#solucao 2
n = int(input('digite numero: '))

if(n==0):
    print('fatorial = 1')
else:
    for i in range(1,n):
        n = n*i
    print('fatorial = %d' %n)
"""
