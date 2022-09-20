from random import randrange
from sys import platform

import os


# Limpiar la consola de comandos (terminal o cmd)
if platform == 'win32':
    os.system('CLS')
elif platform in ['linux', 'linux2', 'darwin']:
    os.system('clear')


def num_system_practice(from_num_system, from_num_system_fn, to_num_system, to_num_system_fn, to_base):
    num = randrange(200)
    inp = input(f'Introduce el número {from_num_system} {from_num_system_fn(num)} en {to_num_system} (x para volver): ')
    if inp == 'x':
        return False
    if int(inp, base=to_base) == num:
        print('Bien hecho!\n')
    else:
        print(f'Mal hecho! (Resultado correcto: {to_num_system_fn(num)})\n')
    return True


numerical_systems = {
    'bd': ('binario', lambda x: bin(x).replace('0b', ''), 'decimal', int, 10),
    'db': ('decimal', int, 'binario', lambda x: bin(x).replace('0b', ''), 2),
    'od': ('octal', lambda x: oct(x).replace('0o', ''), 'decimal', int, 10),
    'do': ('decimal', int, 'octal', lambda x: oct(x).replace('0o', ''), 8),
    'hd': ('hexadecimal', lambda x: hex(x).replace('0x', ''), 'decimal', int, 10),
    'dh': ('decimal', int, 'hexadecimal', lambda x: hex(x).replace('0x', ''), 16)
}

while True:
    user_input = input(
        'Elige la conversión que quieras practicar:\n'
        '- Binario -> Decimal (bd)\n'
        '- Decimal -> Binario (db)\n'
        '- Octal -> Decimal (od)\n'
        '- Decimal -> Octal (do)\n'
        '- Hexadecimal -> Decimal (hd)\n'
        '- Decimal -> Hexadecimal (dh)\n'
        '¡Escribe las iniciales que están entre parentesis para seleccionar el modo que quieras!'
        'Ej.: bd (x para salir del programa)\n'
        )
    if user_input == 'x':
        break
    elif user_input in numerical_systems.keys():
        while True:
            ret = num_system_practice(*numerical_systems[user_input])
            if not ret:
                break
    else:
        print('Esas siglas no están definidas en el programa.\n')
