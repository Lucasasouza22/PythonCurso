par = []
impar = []
while True:
    n = int(input('Digite um numeroex113: '))
    while True:
        cal = n % 2
        if cal == 0:
            par.append(n)
            break
        else:
            impar.append(n)
            break
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja digitar outro numeroex113 [S/N]: ')).upper().strip()[0]
    if mais == 'N':
        break
print(f'Lista par: {par}!')
print(f'Lista impar: {impar}!')
print(f'A soma das duas listas gera: {par+impar}')

