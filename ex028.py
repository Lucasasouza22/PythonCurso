import random
from time import sleep
import emoji
print(30*'-=--=-')
print(emoji.emojize('Vou pensar em um numeroex113 de 0 até 5. Tente adivinhar :cloud:'))
print(30*'-=--=-')
base = str('012345')
lista = list(base)
adivinhar = str(input('Em qual numeroex113 eu pensei? '))
escolha = random.choice(lista)
print('PROCESSANDO')
sleep(3)
print('O numeroex113 escolido por mim foi: {}'.format(escolha))
if adivinhar == escolha:
    print('Você acertou. Parabens!')
else:
    print('Não foi desta vez! Tente novamente.')