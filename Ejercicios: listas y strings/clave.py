'''
Erik Coruña
27/09/2022
Recibe una longitud por teclado y genera una
contraseña alfabética de esa longitud.
'''
from random import randrange


inp = int(input('Longitud de la clave que quieres generar: '))

c = ''
for n in range(inp):
	c += str(randrange(9))

print(f'Contraseña = {c}')
