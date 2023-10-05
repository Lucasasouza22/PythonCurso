from beesnew.biblioteca.interface import *

def leiaarquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print(f'ERRO! Não foi possivel abrir o arquivo.')
    else:
        cabecalho('Produtos cadastrados')
    finally:
        a.close()



def criaarquivo(arq):
    try:
        a = open(arq, 'wt+')
    except:
        print(f'Não foi possivel criar o arquivo!')
    else:
        print(f'Arquivo criado com sucesso!')


def existearquivo(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        print('Falha na leitura do arquivo')
        return False
    else:
        return True