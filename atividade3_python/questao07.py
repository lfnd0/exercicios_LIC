def cont_carac(pal, carac):
	cont_carac = 0
	for i in range(len(pal)):
		if (pal[i] == carac):
			cont_carac = cont_carac + 1
	print("A quantidade de caracteres {}, na palavra {}: {}." .format(carac, pal, cont_carac))
pal = str(input("Digite uma palavra: "))
carac = str(input("Digite um caractere: "))
cont_carac(pal, carac)