from random import randint
computador = randint(0,10)
print('Adivinha o numeroex113 que eu escolhi entre 0 e 10.')
acertou = False
palpite = 0
while not acertou:
    usuario = int(input('Qual é o seu palpite: '))
    palpite += 1
    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('É um puco maior. Tente novamente.')
        elif usuario > computador:
            print('É um pouco menor. Tenta novamente.')
print('FIM')
print('O computador escolheu {} igual a você.'.format(computador))
print('A quantidade de palpite necessarias para você acertar foi {}.'.format(palpite))
