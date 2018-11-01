nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota: "))
conceito = "E"
if nota >= 9:
    conceito = "A"
elif nota >= 8:
    conceito = "B"
elif nota >= 7:
    conceito = "C"
elif nota >= 6:
    conceito = "D"
else:
    conceito = "E"
print("O aluno {} obteve o conceito {}".format(nome, conceito))