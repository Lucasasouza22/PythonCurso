'''km = float(input('Digite quantos Km é para chegar até o seu destino: '))
km1 = float(input('Digite quantos Km é a volta para o ponto de partida inicial: '))
carro = float(input('Você vai alugar carro? Digite 0 para não ou a quantidade de dias: '))
diariac = int(input('Diaria do veiculo R$ '))
aluguelc = (carro * diariac)
litro = float(input('Digite o valor do litro de combustivel R$ '))
consumov = float(input('Consumo de combustivel do veiculo por Km? '))
combustivel = (litro * ((km + km1)/consumov))
print('Você vai rodar {}Km e vai gastar R${:.2f} de combustivel'.format((km+km1),combustivel))
if carro == 0:
    print('Você não terá custos com aluguel de veiculo!')
else:
    print('A diaria do carro custa R${}. Você gastara R${} de diarias com aluguel de veiculo.'.format(diariac,aluguelc))
print('O total de gastos  será R$ {:.2f}'.format(aluguelc+combustivel))'''
