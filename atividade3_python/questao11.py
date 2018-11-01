def verifica_cpf(cpf):
    parte1 = cpf[0:9]
    soma1 = 0
    recebe1 = 10
    parte2 = cpf[0:10]
    soma2 = 0
    recebe2 = 11
    if(len(cpf) == 11 and cpf.isdigit() == True):
        for i in parte1:
            soma1 = soma1 + (int(i)*recebe1)
            recebe1 = recebe1 - 1
        soma1 = soma1*10
        soma1 = soma1 % 11
        if(soma1 == 10):
            soma1 = 0
        if(soma1 == int(cpf[9])):
            for i in parte2:
                soma2 = soma2 + (int(i)*recebe2)
                recebe2 = recebe2 - 1
            soma2 = soma2*10
            soma2 = soma2 % 11
            if(soma2 == 10):
                soma2 = 0
            if(soma2 == int(cpf[10])):
                print("CPF válido!")
            else:
                print("CPF inválido!")
        else:
                print("CPF inválido!")
    else:
        print("CPF inválido!")
cpf = (input("Digite o CPF, somente os números: "))
verifica_cpf(cpf)