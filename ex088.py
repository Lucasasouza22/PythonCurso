from random import randint
from time import sleep
quantidade = int(input(f'Você deseja obter quantos jogos: '))
jogo = []
princi = []
tot = 0
while True:
    cont = 0
    while True:
        computador = randint(1, 60)
        if computador not in jogo:
            jogo.append(computador)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    princi.append(jogo[:])
    jogo.clear()
    tot += 1
    if tot == quantidade:
        break
print('-=-'*30)
print(f'Você pediu {quantidade} jogos!')
print('-=-'*30)
print('Gerando...')
sleep(3)
pos = 0
while pos < len(princi):
    for c in range(0, quantidade):
        print(f'Os valores da {c+1}º são: {princi[pos]} ')
        sleep(3)
        pos += 1
print('Fim')