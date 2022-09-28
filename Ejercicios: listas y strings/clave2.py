'''
Erik Coruña
26/09/2022
Recibe una longitud por teclado y genera una
contraseña alfabética de esa longitud.
'''
import string
import random


inp = int(input('Longitud que quieres para la contraseña: '))

c = ''
for n in range(inp):
	c += random.choice(string.ascii_lowercase)

print(f'Contraseña = {c}')
