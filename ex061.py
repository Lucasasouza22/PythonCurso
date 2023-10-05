n = int(input('Primeiro termo: '))
r = int(input('Qual é a razão: '))
t = n
contagem = 0
print('As 10 primeiras PAs de {} com a razão {} = '.format(n, r), end=' ')
while contagem < 10:
    print('{}'.format(t), end=' ')
    print(' -> ' if contagem < 10 else 'Fim', end=' ')
    t += r
    contagem += 1
