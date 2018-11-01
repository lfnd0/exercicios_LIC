n = int(input("Digite um n: "))
if ((n < 100) & (n > 10)) & ((n % 2 == 0) | (n % 3 == 0)) & (n % 5 == 0):
    print("Codição satisfeita!")
else:
    print("Codição não satisfeita!")