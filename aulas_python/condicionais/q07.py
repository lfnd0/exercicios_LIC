from math import sqrt

A = [2, 0, 1, 3, 4]
B = [4, 1, 3, 2, 6]
    
soma = 0    
for i in range(len(A)):
    soma = soma + (A[i]-B[i])**2

print('Distancia Euclidiana = %.3f' % sqrt(soma))