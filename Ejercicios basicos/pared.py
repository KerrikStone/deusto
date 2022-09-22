'''
Erik Coruña Rodríguez
15-09-2022
Define la altura y anchura de una pared, así como el número de ventanas (1 m²) y puertas (1.6 m²) y calcula la cantidad de litros de pintura necesarios (1 litro → 10 m²).
'''

x, y, ventanas, puertas = 3, 10, 2, 1
print(f'Una pared de {x} m de alto y {y} m de ancho con {ventanas} ventanas y {puertas} puerta necesita {(x * y - (ventanas + 1.6 * puertas)) / 10} litros de pintura.')
