gasolina = [3.5,3.7,3.75,3.40,3.85,3.20]
alcool = [2.7,2.2,2.35,1.95,2.45,2.70,2.3,2.80]

if(len(gasolina)<len(alcool)):
    tam = len(gasolina)
else:
    tam = len(alcool)

for i in range(tam):
    if(alcool[i]/gasolina[i]>0.7):
        print('posto %d - gasolina' %i)
    else:
        print('posto %d - alcool' %i)