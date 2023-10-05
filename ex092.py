from datetime import date
funcionario = dict()
funcionario['Nome'] = str(input('Nome: ')).upper().strip()
ano = int(input('Ano de nascimento: '))
funcionario['Idade'] = date.today().year - ano
ctps = int(input('Digite o numeroex113 da sua CTPS. [0] para desempregado: '))
if ctps != 0:
    funcionario['Nº Ctps'] = ctps
    contratacao = int(input('Ano de contratação: '))
    funcionario['Contratação'] = contratacao
    funcionario['Salario'] = float(input('Digite o valor do seu salario: R$ '))
    contribuicao = (date.today().year - contratacao)
    funcionario['Tempo de contribuição'] = contribuicao
    aposentadoria = 35 - contribuicao
    idadeaposentadoria = aposentadoria + (date.today().year - ano)
    funcionario['Idade de quando se aposentar'] = idadeaposentadoria
    anoadaposentadoria = date.today().year + aposentadoria
    funcionario['Ano da aposentadoria'] = anoadaposentadoria
print('-=-'*10)
print(f'{"Dados cadastrados com SUCESSO!":^20}')
print('-=-'*10)
for i, n in funcionario.items():
    print(f' - {i} : {n}')
print('-=-'*10)
print(f'{"Volte Sempre!":^30}')
print('-=-'*10)