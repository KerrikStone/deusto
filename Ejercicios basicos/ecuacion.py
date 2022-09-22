'''
Erik Coruña Rodríguez
20-09-2022
Define a, b y c en una ecuación de segundo grado y calcula sus raíces.
'''

import math


a, b, c = 1, -5, 6
x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print(f'Raices de {a}x2 + {b}x + {c} = 0:\n{x1}\n{x2}')
