'''
Erik Coruña
26/09/2022
Genera 100 números aleatorios entre 1 y 1000
y guárdalos en una lista. Calcula el rango de
amplitud que tienen los números de la
lista (mayor-menor).
'''
from random import randrange


l = []
for n in range(100):
	l.append(randrange(1, 1000))

print(f'Rango: {max(l) - min(l)} ({min(l)}-{max()})')
