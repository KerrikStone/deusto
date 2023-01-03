#!/usr/bin/env python3
from random import randrange


asignaturas = []
estudiantes = []


def asignatura_str(asignatura: dict) -> str:
    return f"{asignatura['id']};{asignatura['nombre']}, {asignatura['nota']}, {asignatura['convocatorias']}"


def cargar_asignaturas(asignaturas: list[dict]):
    with open('asignaturas.csv', 'r') as f:
        for linea in f:
            id_, nombre = linea.strip().split(';')
            asignaturas.append({'id': id_, 'nombre': nombre})


def crear_estudiantes(asignaturas: list[dict], estudiantes: list[dict]) -> list[dict]:
    asignaturas_id = [a['id'] for a in asignaturas]
    while True:
        nombre_estudiante = input('¿Cuál es el nombre del estudiante? ')
        poblacion = input('¿Dónde vive el estudiante? ')
        asignaturas_del_estudiante = []
        print('Posibles asignaturas')
        for idx in range(len(asignaturas)):
            print(f"{asignaturas[idx]['id']}: {asignaturas[idx]['nombre']}")
        while True:
            eleccion = input(f"Elige entre las {len(asignaturas)} asignaturas "
                             f"la que quieras añadir ({'/'.join(asignaturas_id)}): ")
            ids_asignatura_estudiante = [a['id'] for a in asignaturas_del_estudiante]
            if eleccion not in ids_asignatura_estudiante:
                nombre = [a['nombre'] for a in asignaturas if eleccion == a['id']]
                nota = input('¿Cuál es la nota del estudiante? ')
                convocatoria = input('¿Cuál es el número de convocatoria? ')
                asignaturas_del_estudiante.append({
                    'id': eleccion,
                    'nombre': nombre[0],
                    'nota': float(nota),
                    'convocatorias': int(convocatoria)})
            else:
                print('Esa asignatura ya la tiene asignada este estudiante.')
            if input('¿Quieres añadir más asignaturas? (s/n): ') != 's':
                break
        estudiantes.append({'id': siguiente_id(estudiantes),
                            'usuario': nombre_estudiante,
                            'poblacion': poblacion,
                            'asignaturas': asignaturas_del_estudiante})
        if input('¿Quieres añadir más estudiantes? (s/n): ') != 's':
            break
    return estudiantes


def siguiente_id(estudiantes: list[dict]) -> int:
    if len(estudiantes) == 0:
        return 1
    return max([e['id'] for e in estudiantes]) + 1


def estudiantes_matriculados(asignatura_id: str, estudiantes: list[dict]) -> int:
    return len([e for e in estudiantes if e['asignaturas'][0]['id'] == asignatura_id])


def asignatura_con_mas_suspensos(estudiantes: list[dict]) -> str:
    asignaturas_suspendidas = {}
    for estudiante in estudiantes:
        for asignatura in estudiante['asignaturas']:
            if asignatura['nota'] < 5:
                if asignatura['nombre'] in asignaturas_suspendidas:
                    asignaturas_suspendidas[asignatura['nombre']] += 1
                else:
                    asignaturas_suspendidas[asignatura['nombre']] = 1
    return sorted(asignaturas_suspendidas.items(), key=lambda x: x[1])[-1][0]


def numero_estudiantes_poblacion(estudiantes: list[dict]) -> dict:
    diccionario_final = {}
    for e in estudiantes:
        if e['poblacion'] in diccionario_final:
            diccionario_final[e['poblacion']] += 1
        else:
            diccionario_final[e['poblacion']] = 1
    return diccionario_final


if __name__ == '__main__':
    asignatura = {'id': 'FI123',
                  'nombre': 'Programación I',
                  'nota': 7,
                  'convocatorias': 1}
    estudiantes = [{'id': 1, 'usuario': 'Erik', 'poblacion': 'Barakaldo', 'asignaturas': [{'id': 'FI001', 'nombre': 'Programación I', 'nota': 1.0, 'convocatorias': 1}, {'id': 'FI002', 'nombre': 'Electrónica digital', 'nota': 3.0, 'convocatorias': 1}]}, {'id': 2, 'usuario': 'Carlos', 'poblacion': 'Bilbao', 'asignaturas': [{'id': 'FI001', 'nombre': 'Programación I', 'nota': 10.0, 'convocatorias': 1}, {'id': 'FI002', 'nombre': 'Electrónica digital', 'nota': 3.0, 'convocatorias': 1}]}]
    print(asignatura_str(asignatura))
    print(asignatura_con_mas_suspensos(estudiantes))
    cargar_asignaturas(asignaturas)
    print(asignaturas)
    print(crear_estudiantes(asignaturas, estudiantes))
    print(estudiantes_matriculados('FI001', estudiantes))
    print(numero_estudiantes_poblacion(estudiantes))
