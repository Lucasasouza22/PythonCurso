n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n
contagem = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contagem <= total:
        print('{}'.format(termo), end=' ')
        print(' -> ' if contagem < 10 else ' = ', end=' ')
        termo += r
        contagem += 1
    print('Pausa')
    mais = int(input('Voce deseja ver mais termos: '))
print('FIM')
print(total)
