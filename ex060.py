'''n = int(input('Digite um numeroex113: '))
c = n
f = 1
print('Calculando o fator de {}! = '.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f)'''


'''n = int(input('Digite um numeroex113: '))
f = 1
print('Calculando o fatorial de {}! = '.format(n), end=' ')
for c in range(n , 0, -1):
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
print(f)'''

from math import factorial
n = int(input('Digite um numeroex113: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))