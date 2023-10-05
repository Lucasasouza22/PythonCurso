from time import sleep
def contador(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(f'{c}',end=' ')
        sleep(0.05)
    print('FIM')


print('Contagem de 1 ate 10 de 1 em 1: ',end=' ')
contador(1, 11, 1)
print('Contagem de 10 ate 0 de 2 em 2: ',end=' ')
contador(inicio=10, fim=-1, passo=-2)
print('Agora é a sua vez de personalizar a contagem.')
iniciop = int(input('Inicio:'))
fimp = int(input('Fim:'))
passop = int(input('Passo:'))
print(f'Contagem de {iniciop} ate {fimp} de {passop} em {passop}: ',end=' ')
if iniciop < fimp:
    contador(inicio=iniciop,fim=fimp+1,passo=passop)
else:
    contador(inicio=iniciop, fim=fimp - 1, passo=(passop*-1))