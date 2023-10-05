text = '-==-==-==-'*4
cont = 0
n = (int(input('Digite um numeroex113: ')), int(input('Digite um numeroex113: ')), int(input('Digite um numeroex113: ')), int(input('Digite um numeroex113: ')))
print(f'Você escolheu os seguintes numeroex113: {(n)}')
if 9 in n:
    print(f'O numeroex113 9 aparece {n.count(9)}x')
else:
    print('O numeroex113 9 não apareceu.')
if 3 in n:
    print(f'O numeroex113 3 aparceu na posição {n.index(3)+1}')
else:
    print('O numeroex113 3 não apareceu nehuma vez.')
print(f'Os valores pares digitados foram:',end=' ')
for numero in n:
    if numero % 2 == 0:
        print(numero, end=' ')
print(f'\n{text} FIM {text}')