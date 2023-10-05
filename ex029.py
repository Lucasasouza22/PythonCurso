va = int(input('Informe a velocidade atual do veiculo: '))
m = (va-80)*7
if va > 80:
    print('Sua velocidade atua é de {}Km/h, você ultrapassou o limite maximo de velocidade para essa via que é de 80km/h. \nPor conta disso você será multado em R$ 7,00 por Km acima do limite permitido. \nO valor da sua multa é R$ {:.2f}.'.format(va,m))
if va <=79:
    print('A sua velocidade atual é {}Km/h e está dentro do limite de 80Km/h permitido para a via.'.format(va))
if va == 80:
    print('Atenção! A sua velocidade atual é {}Km/h e está dentro do limite maximo de 80Km/h permitido para a via.'.format(va))