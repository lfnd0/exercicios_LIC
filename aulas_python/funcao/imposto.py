from cmath import sqrt
from _ast import Num

#calculo imposto renda
def calculoIR(nome,salario):
    if(salario<=1500):
        ir = 0
    else:
        ir = salario*0.15
    print('%s - %.2f'%(nome,ir))

func = ['Ana','Pedro', 'Joao','Carlos']
sal =[937,1560,2430,5000]

for i in range(0,len(func)):
    calculoIR(func[i],sal[i])
