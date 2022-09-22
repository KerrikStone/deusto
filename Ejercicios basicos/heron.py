'''
Erik Coruña Rodríguez
20-09-2022
Define la longitud de los lados a, b y c de un triángulo y calcula su área usando la fórmula de Herón.
'''

import math


a, b, c = 11, 13, 17
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f'Un triángulo con lados de {a}, {b} y {c} m tiene {area} m2.')
