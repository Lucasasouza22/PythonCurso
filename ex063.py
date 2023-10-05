print('#'*20)
print('SEQUENCIA FIBONACCI')
print('#'*20)
n = int(input('Você quer ver quantos termos da sequencia de Fibonacci: '))
total = 0
mais = n
cont = 1
anterior = 0
sequencia = 0
atual = 1
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(sequencia), end=' ')
        print('->' if cont <= total else ' = ', end=' ')
        anterior = atual
        atual = sequencia
        sequencia = anterior + atual
        cont += 1
    print('Pausa')
    mais = int(input('Você deseja ver quantos mais: '))
print('Fim')