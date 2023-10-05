soma = 0
conta = 0
paress = 0
paresc = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        conta = conta + 1
print('\nA soma dos {} numeros impares de 1 ate 500 é {}.'.format(conta,soma))
for s in range(1, 501):
    if s % 150 == 0:
        paress = paress + s
        paresc = paresc + 1
print('\nA soma dos {} numeros pares de 1 ate 500 é {}.'.format(paresc,paress))
