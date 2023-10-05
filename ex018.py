import math
a = float(input('Digite o angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O Seno de é {:.2f} \nO cosseno é {:.2f} \nA tangente é {:.2f}'.format(s, c, t))