'''
Erik Coruña
02/10/2022
Recibe una frase y una clave numérica y cifra
la frase con el algoritmo de Vigenere (si la clave
es abc, desplazar a posiciones la 1a letra, b posiciones la 2a, c posiciones la 3a, a posiciones la 4a y así sucesivamente).
'''
import string


inp1 = input('Texto: ').lower()
inp2 = input('Desplazamiento: ')
inp2 = (inp2 * (len(inp1) // len(inp2) + 1))[:len(inp1)]

cifrado = ''
# zip: actua como cremallera y hace el bucle con las dos listas a la vez.
for character, shift in zip(inp1, inp2):
    if character == ' ':
        cifrado += character
    else:
        cifrado += string.ascii_uppercase[(string.ascii_lowercase.index(character) + int(shift)) % len(string.ascii_lowercase)]

print(cifrado)
