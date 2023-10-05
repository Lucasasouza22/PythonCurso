somaidade = 0
mediaidade = 0
homemvelho = ''
maioridadehomem = 0
meninasmenorque20 = 0
for c in range(1, 5):
    print('------- {}ª-------'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemvelho = nome
    if sexo == 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if idade < 20 and sexo in 'Ff':
        meninasmenorque20 += 1
media = somaidade / c
print('A quantidade de meninas menores que 20 anos é {}'.format(meninasmenorque20))
print('A media de idade do grupo é de {} anos'.format(media))
if maioridadehomem > 0:
    print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem, homemvelho))