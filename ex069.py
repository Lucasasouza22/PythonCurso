cont = sexom = mulher_18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo[F/M]: ')).upper().strip()[0]
    mais = ' '
    while mais not in 'SN':
        mais = str(input('\033[4:30:41mDeseja continuar [S/N]: \033[m')).upper().strip()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        sexom += 1
    if sexo == 'F' and idade < 18:
        mulher_18 += 1
    if mais == 'N':
        break
print('**==**'*10)
print('RESULTADOS')
print('**==**'*10)
print(f'Mulheres menores de 18 anos é {mulher_18}.')
print(f'Quantidade de pessoas do sexo masculino {sexom}')
print(f'Quantidade de pessoas maiores de 18 anos é {cont}')