'''
Erik Coruña
29/09/2022
Recibe una frase y un desplazamiento y cifra la
frase con el algoritmo del Cesar (desplazar n
posiciones cada letra).
'''
import string


inp1 = input('Texto: ').lower()
inp2 = int(input('Desplazamiento: '))

cifrado = ''
for n in range(len(inp1)):
    if inp1[n] == ' ':
        cifrado += ' '
    else:
        cifrado += string.ascii_uppercase[(string.ascii_lowercase.index(inp1[n]) + inp2) % len(string.ascii_lowercase)]

print(cifrado)
