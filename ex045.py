import random
from time import sleep
print('='*10,'SEU JOKENPÔ','='*10)
print('Você vai querer: \nPEDRA \nPAPEL \nTESOURA')
jog1 = str(input('Sua opção: ')).strip().upper()
lista = ['PEDRA','PAPEL','TESOURA']
maquina = random.choice(lista)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('='*30)
print('Maquina escolheu {}'.format(maquina))
print('Jogador escolheu {}'.format(jog1))
print('='*30)
if jog1 == 'PEDRA' and maquina == 'TESOURA':
    print('Você venceu! {} ganha de {}.'.format(jog1, maquina))
elif jog1 == 'PEDRA' and maquina == 'PAPEL':
    print('Você perdeu! {} perde de {}.'.format(jog1, maquina))
elif jog1 == 'PAPEL' and maquina == 'TESOURA':
    print('Você perdeu! {} perde de {}.'.format(jog1, maquina))
elif jog1 == 'PAPEL' and maquina == 'PEDRA':
    print('Você venceu! {} ganha de {}.'.format(jog1, maquina))
elif jog1 == 'TESOURA' and maquina == 'PEDRA':
    print('Você perdeu! {} perde de {}.'.format(jog1, maquina))
elif jog1 == 'TESOURA' and maquina == 'PAPEL':
    print('Você venceu! {} ganha de {}.'.format(jog1, maquina))
else:
    print('Ninguem ganhou!')