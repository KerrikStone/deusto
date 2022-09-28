'''
Erik Coruña
26/09/2022
Genera 100 números aleatorios entre 1 y 1000
y guárdalos en una lista. Busca el número 37
dentro de él e indica en qué posición está (si no
está, indícalo).
'''
from random import randrange


l = []
for n in range(100):
	l.append(randrange(1, 1000))

if 37 in l:
	print(f'El número está en la posición {l.index(37)}')
else:
	print('El número 37 no está en la lista.')
