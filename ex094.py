dados = dict()
lista = list()
media = []
pos = int(input('Deseja fazer o cadastro de quantas pessoas: '))
for c in range(1, pos+1):
    dados['nome'] = str(input('Nome: ')).upper().strip()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'FM':
            break
        print('ERRO! por favor digite somente M ou F!')
    dados['idade'] = int(input('Idade: '))
    media.append(dados['idade'])
    lista.append(dados.copy())
    dados.clear()
    print('-=-'*10)
print(f'Foram adicionados {pos} pessoas.')
print('-=-'*10)
posicao = 0
while posicao < pos:
    somaidade = 0
    for c in media:
        somaidade += c
        posicao +=1
mediageral = somaidade /pos
print(f'A media de idade é {mediageral:.2f}!')
print('-=-'*10)
print(f'{"Relação de mulheres":^30}')
print('-=-'*10)
posi = 0
print('Relação de mulheres: ',end='')
while posi < len(lista):
    if lista[posi]['sexo'] == 'F':
        print(f'[{lista[posi]["nome"]}]',end=' ')
    posi += 1
print()
print('-=-'*10)
print(f'Relação de pessoas com idade acima da media que é {mediageral:.2f}:')
print('-=-'*10)
posi = 0
while posi < len(lista):
    if lista[posi]['idade'] > mediageral:
        print(lista[posi])
    posi += 1
print('-=-'*10)