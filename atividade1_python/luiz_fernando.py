#____________________questao1____________________

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
if(A>B):
    print("A é maior que B.")
else:
    print("B é maior que A.")


#____________________questao2____________________

idade = int(input("Digite sua idade: "))
if(idade<14):
    print ("Você é criança.")
elif(idade>=14 and idade<=17):
    print("Você é adolescente.")
elif(idade>=18 and idade<=59):
    print("Você é adulto.")
else:
    print("Você é idoso.")


#____________________questao3____________________

pal1 = input("Digite a 1º palavra: ")
pal2 = input("Digite a 2º palavra: ")
pal3 = input("Digite a 3º palavra: ")
if(pal1<=pal2<=pal3):
    print(pal1, pal2, pal3)
elif(pal1<=pal3<=pal2):
    print(pal1, pal3, pal2)
elif(pal2<=pal1<=pal3):
    print(pal2, pal1, pal3)
elif(pal2<=pal3<=pal1):
    print(pal2, pal3, pal1)
elif(pal3<=pal1<=pal2):
    print(pal3, pal1, pal2)
else:
    print(pal3, pal2, pal1)


#____________________questao4____________________

corretor = input("Digite o nome do corretor: ")
valor = float(input("Digite o valor vendido: "))
comissao = 0
if(valor>50000):
    comissao = valor*(12/100)
    print("O corretor {} receberá {} reais de comissão por suas vendas.".format(corretor, comissao))
elif(valor>=30000) and (valor<=50000):
    comissao  = valor*(9.5/100)
    print("O corretor {} receberá {} reais de comissão por suas vendas.".format(corretor, comissao))
else:
    comissao = valor*(7/100)
    print("O corretor {} receberá {} reais de comissão por suas vendas.".format(corretor, comissao))

    
#____________________questao5____________________

dia_nas = int(input("Digite o dia do seu nascimento: "))
mes_nas = int(input("Digite o mês do seu nascimento: "))
ano_nas = int(input("Digite o ano do seu nascimento (com quatro dígitos): "))
dia_at = int(input("Digite o dia atual: "))
mes_at = int(input("Digite o mês atual: "))
ano_at = int(input("Digite o ano atual (com quatro dígitos): "))
soma = ((ano_at - ano_nas)*360) + abs(((mes_at - mes_nas)*30)) + abs((dia_at - dia_nas))
print("Você viveu em torno de: {} dias! Vida longa e próspera para você!".format(soma))


#____________________questao6____________________

A = int(input("Digite o valor do lado A: "))
B = int(input("Digite o valor do lado B: "))
C = int(input("Digite o valor do lado C: "))
if((A<B+C) and (B<A+C) and (C<A+B)):
    print("A figura é um triângulo.")
    if(A==B and A==C and C==B):
        print("Do tipo equilátero.")
    elif(A!=B and A!=C and C!=B):
        print("Do tipo escaleno.")
    else:
        print("Do tipo isósceles.")
else:
    print("A figura não é um triângulo.")


#____________________questao7____________________

valor = int(input("Digite o valor que você deseja sacar: "))
notas1 = 0
notas2 = 0
notas5 = 0
notas10 = 0
notas20 = 0
notas50 = 0
notas100 = 0
if(valor>=100):
    notas100 = (valor//100)
    valor = (valor%100)
if(valor>=50):
    notas50 = (valor//50)
    valor = (valor%50)
if(valor>=20):
    notas20 = (valor//20)
    valor = (valor%20)
if(valor>=10):
    notas10 = (valor//10)
    valor = (valor%10)
if(valor>=5):
    notas5 = (valor//5)
    valor = (valor%5)
if(valor>=1):
    notas1 = (valor//1)
    valor = (valor%1)
print("Você sacou {} nota(s) de 100 reais, {} nota(s) de 50 reais, {} nota(s) de 20 reais, {} nota(s) de 10 reais, {} nota(s) de 5 reais e {} nota(s) de 1 real.".format(notas100, notas50, notas20, notas10, notas5, notas1))