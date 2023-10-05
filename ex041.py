from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você é MIRIM.')
elif 9 < idade <= 14:
    print('Você é INFANTIL.')
elif 14 < idade <= 19:
    print('Você é JUNIOR.')
elif 19 < idade <= 25:
    print('Você é SENIOR.')
elif 25 < idade:
    print('Você é MASTER.')