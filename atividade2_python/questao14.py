#____________________questao14____________________

pal = str(input("Digite uma palavra: "))
car = str(input("Digite a letra que você deseja contar na palavra: "))
count = 0
for i in pal:
    if(i == car):
        count = count + 1
print("Na palava {}, a letra {} aparece {} vez(es)." .format(pal, car, count))