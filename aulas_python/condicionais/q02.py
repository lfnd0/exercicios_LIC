n = int(input('digite numero: '))

if(n==0 or n==1):
    print('fib = %d' % n)
else:
    a = 0
    b = 1
    fib = 0
    for i in range(1,n):
        fib = a + b
        a = b
        b = fib
        print('====')
        print(a)
        print(b)
        print(fib)
    print('fib = %d' %fib)
    #print('fib = {}'.format(fib))
    #outra possibilidade
    