cores = {'roxo':'\033[35m','verde':'\033[32m','finalizador':'\033[m','vermelho':'\033[31m'}
print('--==--'*40)
print('Bem vindo ao simulador do Bradesco come o seu cu')
print('--==--'*40)
nome = input('Qual é o seu nome? ').strip().upper()
print('Sejá bem vindo, {}{}{}!'.format(cores['verde'],nome, cores['finalizador']))
salario = float(input('Qual é o valor do seu salario? R$ '))
p = salario * 0.3
casa = float(input('Qual é o valor da casa que você deseja financiar? R$ '))
ano = int(input('Em quantos anos você deseja pagar esse imovel?'))
finan = float(casa / (ano * 12))
print('{} é a parcela maxima que você pode pagar!'.format(p))
print('{:.2f} é o valor da parcela do seu financiamento.'.format(finan))
if p <= finan:
    print('{}Infelizmente o banco não podera aprovar seu financiamento Sr(a){}{}.'.format(cores['vermelho'],nome, cores['finalizador']))
elif p > finan:
    print('{}Parabés{} {}{}{}!{}Sua proposta foi aceita.{}'.format(cores['verde'],cores['finalizador'],cores['vermelho'],nome, cores['finalizador'],cores['verde'],cores['finalizador']))
