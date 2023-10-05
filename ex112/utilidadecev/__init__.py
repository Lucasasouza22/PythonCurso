def metade(k=0, s="R$"):
    calc = k / 2
    met = f'{s} {calc:.2f}'.replace('.', ',')
    return met


def dobro(k=0,s="R$"):
    calc = k * 2
    dob = f'{s} {calc:.2f}'.replace('.', ',')
    return dob


def aumento(k=0, txa=0, s="R$"):
    calc = k + (k * (txa / 100))
    sa = f'{s} {calc:.2f}'.replace('.', ',')
    return sa


def desconto(k=0, txd=0, s="R$"):
    calc = k - (k * (txd / 100))
    sd = f'{s} {calc:.2f}'.replace('.', ',')
    return sd


def sifrao(k=0, s="R$"):
    sif = f'{s} {k:.2f}'.replace('.', ',')
    return sif


def resumo(k=0, txa=0, txd=0, s='R$'):
    print(f'{"-=-" * 10}')
    print(f'{"Resumo de Valor":^30}')
    print(f'{"-=-" * 10}')
    print(f'{"Preço analisado":<15}{sifrao(k):>15}')
    print(f'{"Dobro do preço":<15}{dobro(k):>15}')
    print(f'{"Metade do preço":<15}{metade(k):>15}')
    print(f'{"Aumento de 20%":<15}{aumento(k):>15}')
    print(f'{"Desconto de 10%":<15}{desconto(k):>15}')
    print(f'{"-=-" * 10}')