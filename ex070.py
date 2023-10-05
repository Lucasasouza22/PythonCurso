'''produto = valor = soma = valor_1000 = quantidade = menorvalor = produtobarato = 0
while True:
    produto = str(input('Digite o nome do produto: ')).upper().strip()
    valor = float(input('Valor: R$ '))
    quantidade += 1
    if quantidade == 1:
        menorvalor = valor
        produtobarato = produto
    else:
        if valor < menorvalor:
            menorvalor = valor
            produtobarato = produto
    soma += valor
    if valor >= 1000:
        valor_1000 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra é R${soma:.2f}')
print(f'{valor_1000:.0f} produtos custa mais de R$ 1.000,00 por unidade.')
print(f'{produtobarato} é o produto mais barato e custa R${menorvalor:.2f}')
print('=-='*5,' FIM ','=-='*5)'''
