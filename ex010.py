n1 = float(input('Digite o valor que voce tem em sua carteira em R$:'))
n2 = float(input('Digite o valor do dolar atualizado:'))
print('Você consegue comprar hoje ${:.2f} com a cotação atual do dolar de {}.'.format(n1/n2, n2))