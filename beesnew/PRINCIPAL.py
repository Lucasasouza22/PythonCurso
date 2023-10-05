from beesnew.biblioteca.interface import *
from beesnew.biblioteca.dados import *
arq = 'produtosnortebeer'
existearquivo(arq)

cabecalho(f'{"NORTE BEER"}')
resp = menu(['Listar produtos','Cadastrar prodruto','Sair do sistema'])


'''while True:
    try:
        if resp == 1:
            cabecalho('Opção 1')'''
