from datetime import date
contagemm = 0
contagemmm = 0
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {}º pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        contagemm += +1
        print('{} é maior de idade. Tem atualmente {} anos.'.format(ano, idade))
    else:
        contagemmm += +1
        print('{} é menor de idade. Tem atualmente {} anos.'.format(ano, idade))
print('{} é o numeroex113 total de pessoas maiores de idade.'.format(contagemm))
print('{} é o numeroex113 total de pessoas menores de idade.'.format(contagemmm))