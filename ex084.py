geral = []
dados = list()
peso = menorpeso = 0
nome = menornome =  ' '
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: kg ')))
    geral.append(dados[:])
    dados.clear()
    pos = 0
    while pos < len(geral):
        if pos == 0:
            nome = geral[pos][0]
            peso = geral[pos][1]
            menornome = geral[pos][0]
            menorpeso = geral[pos][1]
        else:
            if geral[pos][1] > peso:
                peso = geral[pos][1]
                nome = geral[pos][0]
            elif geral[pos][1] < menorpeso:
                menorpeso = geral[pos][1]
                menornome = geral[pos][0]
        pos += 1
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if mais == 'N':
        break
print(f'Foram cadastradas {len(geral):.0f} pessoas.')
print(f'Relação de pessoas com o maior peso que é {peso}Kg: ', end='')
posi = 0
while posi < len(geral):
    if geral[posi][1] == peso:
        print(f'{geral[posi][0]}...',end=' ')
    posi += 1
cont = 0
print()
print(f'Relação de pessoas com o menor peso que é {menorpeso}Kg: ', end='')
while cont < len(geral):
    if geral[cont][1] == menorpeso:
        print(f'{geral[cont][0]}...',end=' ')
    cont += 1



