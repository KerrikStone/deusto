'''
Erik Coruña
28/09/2022
Crea una lista. Solicita un entero por teclado, y almacénalo en
la lista solo si es >= que el anterior número almacenado (para
el primer número, que sea >=0). Repite el anterior paso hasta
rellenar la lista con 10 enteros. Muestra el contenido de la lista.
'''
l = [0]
while True:
    inp = int(input(f'Escribe un número entero (>= {l[-1]}): '))

    if inp >= l[-1]:
        l.append(inp)

        print(f'El contenido del array es: {l}')
