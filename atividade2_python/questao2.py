#____________________questao2____________________

n = int(input("Digite o número para calcular seu valor de acordo com a sequência de Fibonacci: "))
fib = 0
a = 1
b = 0
i = 1
while (i<=n):
    fib = a + b
    a = b
    b = fib
    i = i + 1
print("O valor conforme a sequência de Fibonacci é: %d." %fib)