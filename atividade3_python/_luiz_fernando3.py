#_________________________questao07_________________________

def cont_carac(pal, carac):
	cont_carac = 0
	for i in range(len(pal)):
		if (pal[i] == carac):
			cont_carac = cont_carac + 1
	print("A quantidade de caracteres {}, na palavra {}: {}." .format(carac, pal, cont_carac))
pal = str(input("Digite uma palavra: "))
carac = str(input("Digite um caractere: "))
cont_carac(pal, carac)


#_________________________questao08_________________________

def cont_carac(pal, carac):
	quant = 0
	for i in range(len(pal)):
		if(pal[i] == carac):
			quant = quant + 1
	return quant

def pal_permuta(pal1, pal2):
	if((len(pal1)) != len(pal2)):
		print("Não é permutação.")
	else:
		cont = 0
		for i in range(len(pal1)):
			quant = cont_carac(pal1, pal1[i])
			quant2 = cont_carac(pal2, pal2[i])
			if(quant == quant2):
				cont = cont + 1
		if(cont == len(pal1)):
				print("É permutação.")
		else:
			print("Não é permutação.")
pal1 = str(input("Digite a 1º palavra: "))
pal2 = str(input("Digite a 2º palavra: "))
pal_permuta(pal1, pal2)


#_________________________questao09_________________________

def encaixe(A, B):
	if (len(A) < len(B)):
		print("Não encaixa.")
	else:
		tam = len(A) - len(B)
		verifica = A[tam:]
		if(verifica == B):
			print("Encaixa.")
		else:
			print("Não encaixa.")
A = str(input("Digite a A palavra: "))
B = str(input("Digite a B palavra: "))
encaixe(A, B)


#_________________________questao10_________________________

def encaixe(A, B):
	if (len(A) < len(B)):
		print("Não é segmento.")
	else:
		if(B in A):
			print("É segmento.")
		else:
			print("Não é segmento.")
A = str(input("Digite a A palavra: "))
B = str(input("Digite a B palavra: "))
encaixe(A, B)


#_________________________questao11_________________________

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