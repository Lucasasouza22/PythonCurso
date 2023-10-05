dados = list()
while True:
    mais = ' '
    nome = str(input('Nome: ')).upper().strip()
    nota1 = float(input(f'1º nota: '))
    nota2 = float(input(f'2º nota: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    while mais not in 'SN':
        mais = str(input('Deseja adicionar mais alunos [S/N]: ')).upper().strip()[0]
    if mais == 'N':
        break
print('-=-'*20)
print(f'{"Nº":<5}{"Nome":<7}{"Media":>10}')
print('-=-'*20)
for c, n in enumerate(dados):
    print(f'{c:<5}{n[0]:<7}{n[2]:>10}')
while True:
    print('-=-' * 20)
    notas = int(input('Deseja ver a nota de qual aluno?[999] Encerra!: '))
    if notas == 999:
        break
    if notas <= len(dados) - 1:
        print(f'O aluno {dados[notas][0]} tirou as seguintes notas {dados[notas][1]}.')
print('FIM')