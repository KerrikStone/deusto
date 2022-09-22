'''
Erik Coruña Rodríguez
20-09-2022
Define la velocidad inicial y el ángulo de salto de una persona y la gravedad para devolver la longitud que recorrería en ese planeta.
'''

import math


velocidad, angulo, gravedad = 4, 45, 1.633
longitud = (velocidad ** 2) * math.sin(2*math.radians(angulo)) / gravedad
print(f'Una persona que salte con un ángulo de {angulo}º a {velocidad} m/s en un planeta con g = {gravedad} m/s2 recorrería {longitud} m.')
