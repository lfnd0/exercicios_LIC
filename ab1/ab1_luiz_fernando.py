#____________________questao1____________________

lista = [10, 9, 14, 28, 31, 7, 42, 33, 18, 23]
pr = 100000
ma = lista[0]
me = lista[0]
for i in lista:
    if (i > ma):
        ma = i
    elif (i < me):
        me = i
print ("Os vencedores com maior pontuação foram: {} e {}. E receberão 50.000 reais cada um." .format(ma, me))

#____________________questao2____________________

A = [3.50, 3.70, 3.75, 3.40, 3.85, 3.20, 3.25, 3.60]
B = [2.70, 2.20, 2.35, 1.95, 2.45, 2.70, 2.30, 2.80]
cal = 0
for i in range(len(A)):
    cal = (B[i] / A [i])
    if (cal>0.7):
        print("Abasteça com gasolina.")
    else:
        print("Abasteça com alcool.")
