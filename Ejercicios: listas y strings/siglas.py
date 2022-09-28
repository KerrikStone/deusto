'''
Erik Coruña
26/09/2022
Solicita una frase y muestra el acrónimo
(siglas) correspondiente.
'''
frase = input('Introduce el nombre de una empresa: ')
frase = frase.split(' ')
siglas = ''
for s in range(len(frase)):
	siglas += frase[s][0]
print(siglas.upper())
