valores = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    if cont == 0 or n > valores[-1]:
        valores.append(n)
        print('Valor adicionado no final da fila.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'valor adicionado na {pos}º posição!')
                break
            pos +=1
    cont += 1
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja ver mais algum valor [S/N]? ')).upper().strip()[0]
    if mais == 'N':
        break
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('5 está presente!')
else:
    print('5 naõ está presente!')