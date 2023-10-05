t1 = float(input('Valor do primeiro lado: '))
t2 = float(input('Valor do segundo lado: '))
t3 = float(input('Valor do terceiro lado: '))
if t1 == t2 == t3:
    print('EQUILÁTERO')
elif t1 == t2 != t3 or t1 != t2 == t3 or t1 != t3 == t2:
    print('ISÓSCELES')
elif t1 != t2 != t3:
    print('ESCALENO')
if t1 < (t2+t3) and t2 < (t1+t3) and t3 < (t2+t3):
    print('Forma um triangulo!')
else:
    print('As 3 retas não podem formar um triangulo.')