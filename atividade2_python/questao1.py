#____________________questao1____________________

n = int(input("Digite o número para fazer o fatorial: "))
fat = 1
i = 1
while(i <= n):
    fat = fat * i
    i = i + 1
print("O valor do fatorial é: %d." %fat)