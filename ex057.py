sexo = str(input('Qual é o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos! Qual é o seu sexo [M/F]: ')).upper().strip()[0]
print('Sua opção sexual escolida foi a {}.'.format(sexo))
print('FIM')
