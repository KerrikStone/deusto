'''
Erik Coruña Rodríguez
16-09-2022
Define un número de segundos y devuelve su equivalencia en horas, minutos y segundos.
'''

s = 8000
horas = s // 3600
minutos = (s % 3600) // 60
segundos = s - (horas * 3600 + minutos * 60)
print(f'{s} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.')
