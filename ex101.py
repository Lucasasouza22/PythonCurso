from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade < 18:
        return print(f'Você tem {idade} anos. O voto não é obrigatorio.')
    if idade < 65:
        return print(f'Voce tem {idade} anos. O voto é obrigatorio.')
    else:
        return print(f'Você tem {idade} anos. O voto é opcional!')


ano = int(input('Digite seu ano de nascimento: '))
voto(ano)