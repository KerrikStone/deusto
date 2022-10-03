'''
Erik Coruña
03/10/2022
Muestra una posible jugada en el Euromillones
(5 números del 1 al 50 no repetidos y 2
números del 1 al 11 no repetidos).
'''
from random import randrange


nums = []
stars = []
for n in range(5):
    ran = randrange(1, 50)
    if ran in nums:
        repeat = True
        while repeat:
            ran = randrange(1, 50)
            if ran not in nums:
                repeat = False
    nums.append(str(ran))

for n in range(2):
    ran = randrange(1, 11)
    if ran in stars:
        repeat = True
        while repeat:
            ran = randrange(1, 11)
            if ran not in stars:
                repeat = False
    stars.append(str(ran))

print('Prueba con esta combinación:', ', '.join(nums), ', estrellas:', ', '.join(stars))
