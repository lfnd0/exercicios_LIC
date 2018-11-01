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