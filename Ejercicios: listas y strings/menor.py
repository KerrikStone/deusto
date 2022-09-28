'''
Erik Coruña
26/09/2022
Genera 100 números aleatorios entre 1 y 1000
y guárdalos en una lista. Busca y muestra el
menor de todos ellos e indica en qué posición
está.
'''
from random import randrange


l = []
for n in range(100):
	l.append(randrange(1, 1000))

print(f'El menor número es {min(l)} y está en la posición {l.index(min(l))}')
