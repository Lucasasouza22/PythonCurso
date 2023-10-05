from time import sleep
soma = 0
n = 0
contagem = 0
print('='*20)
print('     SOMA TUDO')
print('='*20)
print('Encerre a operação digitando: 999')
while n != 999:
    n = int(input('Digite um numeroex113: '))
    soma += n
    contagem += 1
print('\033[1:33:44mCALCULANDO...\033[m')
sleep(3)
print('A soma dos seus {} valores digitados é {}.'.format(contagem-1, soma-999))
print('Fim')
