print('====='*7)
valores = list()
vmenor = vmaior = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        vmaior = valores[c]
        vmenor = valores[c]
    else:
        if valores[c] > vmaior:
            vmaior = valores[c]
        if valores[c] < vmenor:
            vmenor = valores[c]
print(f'Você digitou os valores {valores}!')
print(f'O maior numero digitado foi o {vmaior} nas posições: ',end='')
for c, v in enumerate(valores):
    if v == vmaior:
        print(f'{c}...',end=' ')
print()
print(f'O menor numero é o {vmenor} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == vmenor:
        print(f'{c}...',end=' ')