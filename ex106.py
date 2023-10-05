c = ('\033[m', #0 = sem cor
     '\033[0;31m', #1 = vermelho letras, sem fundo
     '\033[0;42m', #2 = verde cor de fundo, letras pretas
     '\033[0;43m', #3 = amararelo cor de fundo, letras pretas
     '\033[0;45m', #4 = roxo cor de fundo, letras pretas
     '\033[0;46m', #5 = azul cor de fundo, letras pretas
     )


def linha(msg, cor=0):
    q = len(msg)+4
    print(c[cor])
    print(f'{"-" * q}')
    print(f'  {msg.upper()}')
    print(f'{"-" * q}')
    print(c[0])



def biblioteca(funcao):
    from time import sleep
    linha('Carregando...',cor=1)
    sleep(2)
    linha(pesq, cor=3)
    print(c[5])
    help(funcao)
    print(c[0])



while True:
    linha('SISTEMA DE AJUDA PYHELP', cor=2)
    pesq = str(input('Biblioteca ou função? [FIM encerra o programa!] > '))
    if pesq.upper() in 'FIM':
        linha('ATÉ A PROXIMA! OBRIGADO!', cor=4)
        break
    biblioteca(pesq)

