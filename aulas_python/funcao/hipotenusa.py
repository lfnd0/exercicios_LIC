from math import sqrt

def hipo(c1,c2):
    if(c1>0 & c2>0):
        h = sqrt(c1**2+c2**2)
        print('hipotenusa = %.2f' % h)
    else:
        print('valores invalidos!')
    
cateto1 = int(input('Digite cateto1: '))
cateto2 = int(input('Digite cateto2: '))
hipo(cateto1, cateto2)
