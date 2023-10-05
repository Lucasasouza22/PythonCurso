'''import math
cont = 0
soma = 0
n = 0
mais = 1
lista = []
while mais != 'N':
    n = int(input('Digite um numeroex113: '))
    mais = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    lista.append(n)
    soma += n
    cont += 1
print('O conjunto de numeros que você digitou foi: {}'.format(lista))
menor = min(lista)
maior = max(lista)
soma_lista = sum(lista)
numero_elementos = len(lista)
media = soma_lista / numero_elementos
print('A media dos valores vale {}.'.format(media))
print('O menor valor vale {}.'.format(menor))
print('O maior valor vale {}.'.format(maior))
print('Finalizado')'''

