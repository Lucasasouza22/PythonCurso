def maior(*num):
    m = 0
    for c in num:
        for i, v in enumerate(c):
            if i == 0:
                m = v
            else:
                if v > m:
                    m = v
    print(f'O maior valor dentro de {num} é {m}.')


valores = []
resp = int(input('Deseja digitar quantos numeros: '))
for cont in range(0, resp):
    valores.append(int(input('Numero: ')))
maior(valores)