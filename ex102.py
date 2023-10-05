def fatorial(n = 1):
    '''
    Calcula o fatorial de um numeroex113.
    :param n: É o numeroex113 que desejamos saber seu fator
    '''
    global f
    f = 1
    print(f'O fator de {n} é: ',end='')
    for c in range(n, 0, -1 ):
        f *= c
    print(f'= {f}')

def show(resp):
    if resp in 'S':
        print(f'O calculo é: ',end='')
        for c in range(n, 0, -1 ):
            print(f'{c}!',end='')
        print(f'= {f}')

n = int(input('Digite um numeroex113: '))
resp = str(input('Deseja ver a conta? [S/N]')).upper().strip()[0]
fatorial(n)
show(resp)