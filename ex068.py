import random
print('=='*12)
print('VAMOS JOGAR PAR OU IMPAR')
print('=='*12)
cont = computadorn = soma = resultado = 0
escolhapc = ' '
par = 'P'
impar = 'I'
while True:
    cont += 1
    computadorn = random.randint(0, 10)
    n = int(input('Digite um valor: '))
    v = ' '
    while v not in 'PI':
        v = str(input('Voce quer par ou impar [P/I]: ')).upper().strip()[0]
    if v == 'P':
        escolhapc = impar
    else:
        escolhapc = par
    soma = (computadorn + n) % 2
    print(f'\033[1:31:40mO computdor escolheu {computadorn}.\033[m')
    if soma != 0:
        print(f'\033[1:30:42m{impar}mpar ganhou!.\033[m')
        if par == v:
            break
    else:
        print(f'\033[1:30:42m{par}ar ganhou!\033[m')
        if impar == v:
            break
print(f'Você Perdeu na {cont}ª rodada!')

