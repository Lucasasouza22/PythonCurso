def notas(*resp, sit=False):
    '''
    Sua função é calcular a quantidade de notas declaradas e calcular soma, media, total de notas e a situação do aluno.
    :param resp: Notas para serem calculadas
    :param sit: Expectativa referente as notas declaradas em resp.
    :return: Dicionario com varias informações referente as resp declaradas.
    '''
    soma = 0
    for n in resp:
        soma += n
    total = len(resp)
    media = soma / total
    pos = maior = menor = 0
    while pos < len(resp):
        if pos == 0:
            maior = resp[pos]
            menor = resp[pos]
        else:
            if resp[pos] > maior:
                maior = resp[pos]
            if resp[pos] < menor:
                menor = resp[pos]
        pos += 1
    geral['TOTAL'] = total
    geral['MEDIA'] = media
    geral['MAIOR'] = maior
    geral['MENOR'] = menor
    if sit:
        if media < 3:
            sit = 'RUIM'
        elif media < 6:
            sit = 'DIFICIL'
        else:
            sit = 'BOA'
        geral['SITUAÇÂO'] = sit


geral = dict()
resp = notas(4, 7, 1, 10, 0, 1, 3, sit=True)

