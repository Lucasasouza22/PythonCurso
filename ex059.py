from time import sleep
n1 = float(input('Primeiro numeroex113: '))
n2 = float(input('Segundo numeroex113: '))
opcao = 0
while opcao != 5:
    print('''Qual operação você deseja realizar:
        [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos numeros
        [5]Sair do programa''')
    opcao = int(input('Escolha uma operação: '))
    print('-==-'*6)
    if opcao == 1:
        soma = n1+n2
        print('{:.0f} + {:.0f} = {:.0f}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1*n2
        print('{:.0f} x {:.0f} = {:.0f}'.format(n1, n2, mult))
    elif opcao == 3:
        lista = [n1,n2]
        maior = max(lista)
        print('O maior numeroex113 é {:.0f}'.format(maior))
    elif opcao == 4:
        print('\033[1:31:40mVamos lá novamente.\033[m')
        print('Carregando...')
        sleep(3)
        n1 = float(input('Primeiro numeroex113: '))
        n2 = float(input('Segundo numeroex113: '))
    elif opcao == 5:
        print('Até breve!')
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção invalida! Tente Novamente')
        print('Carregando...')
        sleep(3)
    print('-==-' * 6)
print('\033[0:31:40mPrograma finalizado\33[m')