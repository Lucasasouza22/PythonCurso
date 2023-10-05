'''produtos = ('lapis',3.50,'Caneta',5.00,'Mouse',25.80,'Impressora',580.99,'Computador',857.88)
print('========'*6)
print(' '*12,'Tabela de Preços')
print('========'*6)
produtosposi = 0
produtoposi = 1
while True:
    print(produtos[produtosposi],end='')
    print('{}R${:.2f}'.format('.'*37, produtos[produtoposi]))
    produtosposi += 2
    produtoposi += 2
    if produtoposi > 10:
        break
print('========'*6)'''
print('========'*6)
print(f'{"Tabela de Preços":^45}')
print('========'*6)
produtos = ('lapis',3.50,
            'Caneta',5.00,
            'Mouse',25.80,
            'Impressora',580.99,
            'Computador',857.88)
itens = len(produtos)
for pos in range(0, itens):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<39}',end='')
    elif pos % 2 == 1:
        print(f'R$ {produtos[pos]:>6.2f}')
print('========'*6)