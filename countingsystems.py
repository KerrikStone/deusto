from random import randrange
import os


# Limpiar la consola de comandos (terminal o cmd)
os.system('CLS')
os.system('clear')

# Binario -> Decimal
def binary_to_decimal():
    result1 = randrange(200)
    num1 = bin(result1).replace('0b', '')
    input1 = input(f'Introduce el número {num1} en decimal: ')
    if int(input1) == result1:
        print('Bien hecho!\n')
    else:
        print(f'Mal hecho! (Resultado: {result1})\n')
    binary_to_decimal()

# Decimal -> Binario
def decimal_to_binary():
    num2 = randrange(200)
    result2 = bin(num2).replace('0b', '')
    input2 = input(f'Introduce el número {num2} en binario: ')
    if input2 == result2:
        print('Bien hecho!\n')
    else:
        print(f'Mal hecho! (Resultado: {result2})\n')
    decimal_to_binary()

# Octal -> Decimal
def octal_to_decimal():
    result3 = randrange(200)
    num3 = oct(result3).replace('0o', '')
    input3 = input(f'Introduce el número {num3} en decimal: ')
    if int(input3) == result3:
        print('Bien hecho!\n')
    else:
        print(f'Mal hecho! (Resultado: {result3})\n')
    octal_to_decimal()

# Decimal -> Octal
def decimal_to_octal():
    num4 = randrange(200)
    result4 = oct(num4).replace('0o', '')
    input4 = input(f'Introduce el número {num4} en octal: ')
    if int(input4) == result4:
        print('Bien hecho!\n')
    else:
        print(f'Mal hecho! (Resultado: {result4})\n')
    decimal_to_octal()

# Hexadecimal -> Decimal
def hex_to_decimal():
    result5 = randrange(200)
    num5 = hex(result5).replace('0x', '')
    input5 = input(f'Introduce el número {num5} en decimal: ')
    if int(input5) == result5:
        print('Bien hecho!\n')
    else:
        print(f'Mal hecho! (Resultado: {result5})\n')
    hex_to_decimal()

# Decimal -> Hexadecimal
def decimal_to_hex():
    num6 = randrange(200)
    result6 = oct(num6).replace('0o', '')
    input6 = input(f'Introduce el número {num6} en hexadecimal: ')
    if int(input6) == result6:
        print('Bien hecho!\n')
    else:
        print(f'Mal hecho! (Resultado: {result6})\n')
    decimal_to_hex()

user_input = input('Elige la conversión que quieras practicar:\n- Binario -> Decimal (bd)\n- Decimal -> Binario (db)\n- Octal -> Decimal (od)\n- Decimal -> Octal (do)\n- Hexadecimal -> Decimal (hd)\n- Decimal -> Hexadecimal (dh)\n¡Escribe las iniciales entre parentesis para seleccionar el modo que quieras! Ej.: bd (Ctrl + c para salir del programa)\n')
if user_input == 'bd':
    binary_to_decimal()
elif user_input == 'db':
    decimal_to_binary()
elif user_input == 'od':
    octal_to_decimal()
elif user_input == 'do':
    decimal_to_octal()
elif user_input == 'hd':
    hex_to_decimal()
elif user_input == 'dh':
    decimal_to_hex()
else:
    print('Esas siglas no están definidas en el programa.')
