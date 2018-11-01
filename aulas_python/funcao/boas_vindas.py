def boas_vindas(nome_usuario,idade):
    print('Ola, %s. Seja bem vindo' % nome_usuario)
    print('A sua idade e: %d' % idade)
    
print('Sistema inicializado')
a = raw_input('Digite seu nome: ')
i = int(input('Digite sua idade: '))
boas_vindas(a,i)
