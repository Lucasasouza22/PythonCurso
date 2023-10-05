aluno = dict()
aluno['Nome'] = str(input('Nome: ')).upper().strip()
aluno['Media'] = float(input('Media: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 3 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for i, n in aluno.items():
    print(f' * {i} é igual {n}')

