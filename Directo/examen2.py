#!/usr/bin/env python3


usuarios = [{'id': '@user1', 'nombre': 'Nombre-1', 'pais': 'Pais-1', 'fecha': [21, 3, 2006]},
            {'id': '@user2', 'nombre': 'Nombre-2', 'pais': 'Pais-1', 'fecha': [6, 10, 2010]},
            {'id': '@user3', 'nombre': 'Nombre-3', 'pais': 'Pais-2', 'fecha': [1, 9, 2016]},
            {'id': '@user4', 'nombre': 'Nombre-4', 'pais': 'Pais-1', 'fecha': [3, 2, 2004]}]

# PRIMER EJERCICIO
def mostrar_usuario(usuario):
    return f"ID: {usuarios[usuario]['id']}; Nombre: {usuarios[usuario]['nombre']}; Antigüedad: {2022 - usuarios[usuario]['fecha'][2]} años."

print(mostrar_usuario(0))

# SEGUNDO EJERCICIO
def usuarios_por_pais(lista):
    pais_1 = 0
    pais_2 = 0
    for i in range(len(lista)):
        if usuarios[i]['pais'] == 'Pais-1':
            pais_1 += 1
        else:
            pais_2 += 1
    return {'Pais-1': pais_1, 'Pais-2': pais_2}

print(usuarios_por_pais(usuarios))

# TERCER EJERCICIO
def año_usuario_mas_antiguo(lista):
    antiguo = 2022
    for x in lista:
        if x['fecha'][2] < antiguo:
            antiguo = x['fecha'][2]
    return antiguo

print(año_usuario_mas_antiguo(usuarios))

# CUARTO EJERCICIO
def cargar_fichero(lista):
    for i in range(len(usuarios)):
        txt = open('fichero.csv', 'r').readline()
        txt = txt.replace('\n', '')
        lista.append(txt.replace(';', ' '))
    return lista

print(cargar_fichero(list()))
