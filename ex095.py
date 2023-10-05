jogador = dict()
principal = []
gols = list()
while True:
    resposta = ' '
    gols.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome:')).strip().upper()
    jogador['partidas'] = int(input('   Quantas partidas ele jogou:'))
    for c in range(1, jogador['partidas']+1):
        gols.append(int(input(f'        Quantos gols na {c}º partida:')))
    jogador['gols'] = gols.copy()
    jogador['Total Gols'] = sum(gols)
    principal.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar [S/N]:')).upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if resposta in 'N':
        break
print('-=-'*19)
print(f'{"COD":<4}', end=' ')
for k in jogador.keys():
    print(f'{str(k).upper():<15}', end='')
print()
for enun, v in enumerate(principal):
    print(f'{enun:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=-'*19)
while True:
    dados = ' '
    dados = int(input('Mostrar dados de qual jogador? (999) para finalizar! '))
    if dados == 999:
        break
    if dados >= len(principal):
        print(f'ERRO! O codigo {dados} não existe!')
    for i, v in enumerate(principal):
        if dados == i:
            print('-=-' * 19)
            print(f'                Jogador {principal[dados]["nome"]}')
            print('-=-' * 19)
            print(f'COD = {i}')
            for i, v in v.items():
                print(f'{i} = {v}')
            print(f'{"-=-"*5}Gols por jogo{"-=-"*5}')
            for i, d in enumerate(principal[dados]["gols"]):
                print(f'No jogo {i+1} fez {d} gols.')
            print('-=-' * 19)
            break
print('Volte Sempre!')



