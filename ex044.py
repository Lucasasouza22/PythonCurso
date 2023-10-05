preco = float(input('Qual é o preço do produto? R$ '))
pagamento = input('Qual é a forma de pagamento: \n[1] Dinheiro \n[2} Cheque à vista \n[3] À vista cartão \n[4] 2x no cartão de credito \n[5] 3x ou mais \nSua opção: ')
if pagamento == '1':
    valor = preco - (preco * 10 / 100)
    print('Valor a ser pago R${:.2f}'.format(valor))
elif pagamento == '2':
    valor = preco - (preco * 10 / 100)
    print('Valor a ser pago R${}'.format(valor))
elif pagamento == '3':
    valor = preco - (preco * 5 / 100)
    print('Valor a ser pago R${}'.format(valor))
elif pagamento == '4':
    print('Valor a ser pago R${}'.format(preco))
elif pagamento == '5':
    valor = preco + (preco * 20 / 100)
    parcelamento = int(input('Quantas vezes? '))
    parcelas = valor / parcelamento
    print('Valor a ser pago R${:.2f} dividido em {}x de R${:.2f}'.format(valor, parcelamento, parcelas))