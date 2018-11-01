#____________________questao15____________________

pal = str(input("Digite uma palavra: "))
count = 0
for i in pal:
    if(i == 'a'):
        count = count + 1
    if(i == 'e'):
        count = count + 1
    if(i == 'i'):
        count = count + 1
    if(i == 'o'):
        count = count + 1
    if(i == 'u'):
        count = count + 1
print("A palavra: {}, possui {} vogal(is)." .format(pal, count))