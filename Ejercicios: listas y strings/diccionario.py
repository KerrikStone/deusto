'''
Erik Coruña
28/09/2022
Recibe dos palabras y di cuál de ellas está
antes en un diccionario.
'''
inp1 = input('Primera palabra: ')
inp2 = input('Segunda palabra: ')

l = [inp1, inp2]
l.sort()
print(f'{l[0]} está antes que {l[1]} en un diccionario.')
