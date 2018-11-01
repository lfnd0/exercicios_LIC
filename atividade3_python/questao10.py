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