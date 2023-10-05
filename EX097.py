def titulo(msg):
    conta = len(msg) + 4
    print(f'{"-" * conta}')
    print(f'  {msg}')
    print(f'{"-" * conta}')


titulo(str(input('Digite o titulo desejado: ')))