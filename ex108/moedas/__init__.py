def aumenta20(k):
    p = k * 0.2
    k = p + k
    return k

def desconta10(k):
    p = k * 0.1
    k -= p
    return k

def metade(k):
    k /= 2
    return k

def dobro(k):
    k *= 2
    return k

def sifrao(k):
    res = str(input('Em qual moeda você deseja receber o valor [R = Real] [E = Euro] [D = Dolar]: ')).upper().strip()[0]
    if res == 'R':
        return 'R$'
    if res == 'E':
        return '€'
    if res == 'D':
        return '$'