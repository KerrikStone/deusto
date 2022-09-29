'''
Erik Coruña
28/09/2022
Crea una lista con los 100 primeros números naturales. Solicita
un número y búscalo en la lista haciendo el mínimo número de
búsquedas.
'''
n = 0
n2 = 100
p = 50
inp1 = int(input('Escribe un número natural del 1 al 100: '))
while True:
    inp2 = input(f'({n}-{n2}) Está en la posición {p}? ')
    if inp2.lower() == 'no, es mayor':
        n = p
        p += (n2 - p) // 2
    elif inp2.lower() == 'no, es menor':
        n2 = p
        p -= (p - n) // 2
    else:
        print(f'El número está en la posición {p}.')
        break
