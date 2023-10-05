from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('O computador escolheu {}.'.format(itens[computador]))