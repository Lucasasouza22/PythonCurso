menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('{}º Quantos Kg você pesa? Kg '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso {}kg'.format(menor))
print('O maior peso {}kg'.format(maior))