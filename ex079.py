valores = []
while True:
    n = int(input('Digite um numeroex113: '))
    if n not in valores:
        valores.append(n)
        print('Numero adicionado!')
    else:
        print('Numero duplicado. Não vou adicionar.')
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if mais in 'N':
        break
print(f'Você digitou os seguintes valores {sorted(valores)}')
for c, v in enumerate(valores):
    print(f'{v} foi digitado na posição {c}º!')