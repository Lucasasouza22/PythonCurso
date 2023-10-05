palavras = ('Amor',
            'Odio',
            'Livre',
            'Sempre')
for pos in palavras:
    print(f'\n{pos} tem as seguintes vogais:',end=' ')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\nFIM')

