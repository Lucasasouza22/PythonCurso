from random import randint
from time import sleep
numeros = list()

def sorteia(n):
    print(f'Sorteando os numeros: ',end='')
    for c in range(0, n):
        sleep(0.08)
        sort = int(randint(1,10))
        print(f'[{sort}]', end=' ')
        numeros.append(sort)
    print('Fim')

def somapar(k):
    soma = 0
    cont = 0
    print(f'{"-=-" * 20}')
    for c in k:
        if c % 2 == 0:
            soma += c
            cont += 1
    print(f'Foram sorteados {cont} numeros pares. A soma de todos eles vale {soma}')

sorteia(5)
somapar(numeros)

