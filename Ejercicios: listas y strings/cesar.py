'''
Erik Coruña
29/09/2022
Recibe una frase y un desplazamiento y cifra la
frase con el algoritmo del Cesar (desplazar n
posiciones cada letra).
'''
import string


inp1 = input('Texto: ')
inp2 = int(input('Desplazamiento: '))

cifrado = ''
for n in range(len(inp1)):
    cifrado += string.ascii_lowercase[list(string.ascii_lowercase).index(inp1[n]) + inp2]

print(cifrado)
