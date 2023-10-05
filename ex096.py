def titulo(msg):
    print(f'{"-=-" * 10}')
    print(f'{msg:^30}')
    print(f'{"-=-" * 10}')
def area(largura, comprimento):
    m = largura * comprimento
    print(f'A area total de Largura {largura}m x Comprimento {comprimento}m é {m}m².')


titulo('CONTROLE DE TERRENOS')
largura = float(input('Largura: '))
comprimento = float(input('Compriento: '))
area(largura,comprimento)
