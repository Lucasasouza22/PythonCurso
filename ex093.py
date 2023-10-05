'''jogador = { }
jogador['Nome'] = str(input('Nome: ')).upper().strip()
jogador['Partida'] = 0
jogador['Gols'] = 0
while True:
    print('Para finalizar digite P!')
    partida = str(input('Estava em campo? [S/N]: ')).upper().strip()[0]
    if partida == 'S':
        jogador['Partida'] += 1
        jogador['Gols'] += int(input('Gols marcados nessa partida: '))
    if partida == 'P':
        break
print('-=-'*10)
print(f'{"Informações do jodador:":^30}')
print('-=-'*10)
for i, v in jogador.items():
    print(f' - {i} : {v}')
print('-=-'*10)'''
dados = dict()
gol = []
dados['Nome'] = str(input('Nome: ')).upper().strip()
while True:
    mais = ' '
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
    if partidas != 0:
        for c in range(1, partidas+1):
            gol.append(int(input(f'Quantos gols ele marcou na {c}º partida: ')))
        dados['Gols'] = gol.copy()
        dados['Total de gols'] = 0
        for c in gol:
            dados['Total de gols'] += c
    mais = str(input('Digite F para finzalizar!')).upper().strip()[0]
    if mais == 'F':
        break
print('-=-'*10)
print(dados)
print('-=-'*10)
for i, v in dados.items():
    print(f'O campo {i} tem o valor {v}.')
print('-=-'*10)
print(f'O jodador {dados["Nome"]} jogou {partidas} partidas.')
pos = 0
while pos < len(gol):
    for c in range(0, partidas):
        print(f' => Na {c+1}º partida,fez {gol[pos]} ')
        pos += 1
print(f'Fez um total de {dados["Total de gols"]} gols.')