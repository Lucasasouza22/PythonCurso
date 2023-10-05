def resumo(k=0, a=0, d=0, s='R$'):
    sif = f'{s} {k:.2f}'.replace('.',',')
    aum = k + (k * (a / 100))
    sa = f'{s} {aum:.2f}'.replace('.',',')
    desc = k - (k * (d / 100))
    sd = f'{s} {desc:.2f}'.replace('.', ',')
    metade = k / 2
    met = f'{s} {metade:.2f}'.replace('.', ',')
    dobro = k * 2
    dob = f'{s} {dobro:.2f}'.replace('.', ',')
    print(f'{"-=-" * 10}')
    print(f'{"Resumo de Valor":^30}')
    print(f'{"-=-" * 10}')
    print(f'{"Preço analisado":<15}{sif:>15}')
    print(f'{"Dobro do preço":<15}{dob:>15}')
    print(f'{"Metade do preço":<15}{met:>15}')
    print(f'{"Aumento de 20%":<15}{sa:>15}')
    print(f'{"Desconto de 10%":<15}{sd:>15}')
    print(f'{"-=-" * 10}')
