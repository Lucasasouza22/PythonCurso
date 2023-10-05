n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media >= 7:
    print('Sua media foi {}.'.format(media))
    print('Aprovado!')
elif media >= 5 and media <= 6.9:
    print('Sua media foi {}.'.format(media))
    print('Recuperação!')
elif media <= 5:
    print('Sua media foi {}.'.format(media))
    print('Reprovado!')