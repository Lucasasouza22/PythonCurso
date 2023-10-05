'''import random
cont = menor = maior = 0
while True:
    print('Os valores sorteados foram:',end=' ')
    for c in range(1,11):
        computador = random.randint(1,10)
        print('{}'.format(computador), end=' ')
        cont += 1
        if cont == 1:
            menor = computador
            maior = computador
        else:
            if computador < menor:
                menor = computador
            if computador > maior:
                maior = computador
    if cont == 10:
        break
print(f'\nO maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}')'''
import random
import math
from random import randint
n = (random.randint(0,10), random.randint(0,10), random.randint(0,10),
     random.randint(0,10), random.randint(0,10),)
ordem = sorted(n)
print(f'O computador sorteouos seguintes numeros: {ordem}')
print(f'O menor numero {min(ordem)}')
print(f'O maior numero {max(ordem)}')
