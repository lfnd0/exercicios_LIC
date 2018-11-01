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