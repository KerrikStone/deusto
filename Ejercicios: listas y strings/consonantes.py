'''
Erik Coruña
26/09/2022
Solicita una frase y muestra el número de
consonantes.
'''
consonantes = 0
frase = input('Introduce una frase: ')
for n in range(len(frase)):
	if frase[n].lower() in ('qwrtypsdfghjklñzxcvbnm'):
		consonantes += 1
print(f'Consonantes: {consonantes}')
