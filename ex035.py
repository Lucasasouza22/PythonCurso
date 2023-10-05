l1 = float(input('Digite o valor da primeira reta: '))
l2 = float(input('Digite o valor da segunda reta: '))
l3 = float(input('Digite o valor da terceira reta: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('As 3 retas podem formar um triangulo.')
else:
    print('As 3 retas não podem formar um triangulo.')