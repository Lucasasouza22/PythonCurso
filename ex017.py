#import math
from math import hypot
Co = float(input('Digite o cateto oposto: '))
Ca = float(input('Digite o cateto adjacente: '))
Hi = hypot(Co,Ca)
print('Hipotenusa: {}'.format(Hi))
print('Cateto Oposto: {}'.format(Co))
print('Cateto Adjacente: {}'.format(Ca))