#!/usr/bin/env python3

meses = [['Enero', 31, 'Invierno'],
       ['Febrero', 28, 'Invierno'],
       ['Marzo', 31, 'Primavera'],
       ['Abril', 30, 'Primavera'],
       ['Mayo', 31, 'Primavera'],
       ['Junio', 30, 'Verano'],
       ['Julio', 31, 'Verano'],
       ['Agosto', 31, 'Verano'],
       ['Septiembre', 30, 'Otono'],
       ['Octubre', 31, 'Otono'],
       ['Noviembre', 30, 'Otono'],
       ['Diciembre', 31, 'Invierno']]

# PRIMER EJERCICIO
def mes_del_año(mes):
    return f"{meses[mes - 1][0]}: {meses[mes - 1][1]} días -> {meses[mes - 1][2]}, {'no hay cambio de estación' if meses[mes - 1][2] == meses[mes - 2][2] else 'cambio de estación'}"

print(mes_del_año(4))

# SEGUNDO EJERCICIO
def numeros():
    lista = []
    for n in range(10):
        inp = input('Introduce un número: ')
        lista.append(int(inp))
    while True:
        inp = input('Qué número desea buscar: ')
        if int(inp) in lista:
            print('El dato está en la lista.')
        elif int(inp) == 0:
            print('Salir.')
            break
        else:
            print('El dato no está en la lista.')

numeros()

# TERCER EJERCICIO
def empaquetar_lista(lista = [1, 2, 1, 3, 5, 1, 1, 3, 3]):
    lista2 = []
    count = 0
    for i in range(len(lista)):
        count += 1
        if len(lista) > (i + 1):
            if lista[i] != lista[i + 1]:
                lista2.append((lista[i], count))
                count = 0
        else:
            lista2.append((lista[i], count))
    return lista2

print(empaquetar_lista())
