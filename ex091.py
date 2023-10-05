from random import randint
from time import sleep
dado = dict()
sort = []
maior = menor = 0
for c in range(1,5):
    computador = randint(1, 6)
    dado[f'{c}º Jogador'] = computador
    sort.append(computador)
    sort.sort()
    if c == 1:
        maior = computador
    elif computador > maior:
        maior = computador
    elif computador == maior:
        maior = 'DUPLICADO! Ninguem ganhou!'
    print(f'O dado sorteou para o {c}º jogador o numero {computador}!')
    sleep(2)
print(f'O vencedor foi {maior}')

#from operator import itemgetter
#dado = sorted(dado.items(), key=itemgetter(1), reverse=True)