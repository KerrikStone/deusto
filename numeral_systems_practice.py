from random import randrange
from sys import platform

import os


# Limpiar la consola de comandos (terminal o cmd)
if platform == 'win32':
    os.system('CLS')
elif platform in ['linux', 'linux2', 'darwin']:
    os.system('clear')


def num_system_practice(from_num_system, from_num_system_fn, to_num_system, to_num_system_fn, to_base_fn):
    """
    from_num_system: string representation of the numerical system to convert from.
    from_num_system_fn: function to convert a number to from_num_system.
    to_num_system: string representation of the numerical system to convert to.
    to_num_system_fn: function to convert a number to to_num_system.
    to_base_fn: function to convert from to_num_system to integer.
    """
    num = randrange(200)
    inp = input(f'Introduce el número {from_num_system} {from_num_system_fn(num)} en {to_num_system} (x para volver): ')
    if inp == 'x':
        return False
    if to_base_fn(inp) == num:
        print('Bien hecho!\n')
    else:
        print(f'Mal hecho! (Resultado correcto: {to_num_system_fn(num)})\n')
    return True

numerical_systems = {
    'bd': ('binario', lambda x: bin(x).replace('0b', ''), 'decimal', int, int),
    'db': ('decimal', int, 'binario', lambda x: bin(x).replace('0b', ''), lambda x: int(x, base=2)),
    'od': ('octal', lambda x: oct(x).replace('0o', ''), 'decimal', int, int),
    'do': ('decimal', int, 'octal', lambda x: oct(x).replace('0o', ''), lambda x: int(x, base=8)),
    'hd': ('hexadecimal', lambda x: hex(x).replace('0x', ''), 'decimal', int, int),
    'dh': ('decimal', int, 'hexadecimal', lambda x: hex(x).replace('0x', ''), lambda x: int(x, base=16)),
    'bcdd': ('bcd', lambda x: ' '.join([('000' + bin(int(d))[2:])[-4:] for d in str(x)]), 'decimal', int, int),
    'dbcd': ('decimal', int, 'bcd', lambda x: ' '.join([('000' + bin(int(d))[2:])[-4:] for d in str(x)]),
        lambda x: int(''.join([str(int(x[y:y+4], 2)) for y in range(0, len(x), 5)])))
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
        '- BCD -> Decimal (bcdd)\n'
        '- Decimal -> BCD (dbcd)\n'
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
