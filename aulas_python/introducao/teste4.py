import math

a = float (input("Digite o valor de a: "))
b = float (input("Digite o valor de b: "))
c = float (input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A equação possui uma única raiz: ",raiz1)

else:
    if delta < 0:
        print("A equação não possui raízes dentro do conjunto dos números reais, ou seja Δ < 0.")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a )
        raiz2 = (-b - math.sqrt(delta)) / (2 * a )
        print("x' é: ",raiz1)
        print("x'' é: ",raiz2)