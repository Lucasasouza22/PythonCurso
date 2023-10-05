n = int(input('Digite um numeroex113: '))
print('-=-'*10)
cont = 0
for c in range(1 , n+1):
    primo = n / c
    if n % c == 0 and n % 1 == 0:
        cont = cont + 1
        print('{:2} / {:2} = {:.0f}'.format(n, c, primo))
print('-=-'*10)
if cont == 2:
    print('{} é um numeroex113 primo! O numeroex113 de divisores é {}.'.format(n, cont))
elif cont >= 3:
    print('{} não é primo! Ele tem {} divisores.'.format(n, cont))

