def calculo_salario(qtd_horas,val_hora):
    if(qtd_horas<=40):
        sal = qtd_horas*val_hora
    else:
        extra = qtd_horas - 40
        sal = 40*val_hora + extra*(1.5*val_hora)
    print('salario = %.2f' % sal)
    
valor_hora = int(input('digite valor da hora: '))
horas = 45  
calculo_salario(horas,valor_hora)
