'''
def linha(n):
    print(f'{"-=-"*10}')

def ficha(jogador, show=False):
    dados = dict()
    gols = list()
    dados['nome'] = jogador
    partidas = int(input('Quantas partidas jogou: '))
    for c in range(0, partidas):
        gols.append(int(input('Gols marcados: ')))
    dados['gols'] = gols
    geral.append(dados)
    if show:
        linha(1)
        print(f'{"COD":^4}', end='')
        for k in dados.keys():
            print(f'{str(k).upper():^15}', end='')
        print()
        pos = 0
        while pos < len(geral):
            print(f'{pos:^4}',end='')
            pos += 1
        for v in geral:
            for d in v.values():
                print(f'{str(d):^15}', end='')





geral = list()
jogador = str(input('Nome: ')).upper().strip()
ficha(jogador, True)'''

'''def ficha(jogador, show=False):

    jogador = dict()
    jogador['nome'] = str(input('Nome: ')).upper()
    if jogador['nome'] in ' ':
        jogador['nome'] = '<desconhecido>'
    gols = input('Numero de gols: ')
    if gols.isnumeric():
        jogador['gols'] = int(gols)
    else:
        jogador['gols'] = 0
    print(f'O jogador {jogador["nome"]} fez {jogador["gols"]} gols.')


jogador = ' '
ficha(jogador)'''


def ficha(jogador='<desconhecido>',gols=0):
    jogador = input('Nome: ')
    if jogador.isalpha():
        jogador = str(jogador).upper()
    else:
        jogador = '<desconhecido>'
    gols = input('Numero de gols: ')
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gols.')


ficha()
