#!/usr/bin/env python3
from pasajero import Pasajero
from maleta import Maleta


pasajeros = []

def checkin_online(pasajeros: list[Pasajero]):
    for nombre, apellido in [('Pasajero1', 'Apellido1'),
              ('Pasajero2', 'Apellido2'),
              ('Pasajero3', 'Apellido3'),
              ('Pasajero4', 'Apellido4'),
              ('Pasajero5', 'Apellido5')]:
        pasajeros.append(Pasajero(nombre, apellido))

def volumen_cabina(pasajeros: list[Pasajero]) -> float:
    volumen_total_cabina = 0
    for pasajero in pasajeros:
        for maleta in pasajero.cabina:
            volumen_total_cabina += maleta.altura * maleta.anchura * maleta.largura
    return float(volumen_total_cabina)

def annadir_maletas(pregunta: str) -> list[Maleta]:
    maletas = []
    while True:
        if input(pregunta) == 's':
            print('Añadiendo nueva maleta...\n')
            codigo = input('Código: ')
            altura = input('Altura: ')
            anchura = input('Anchura: ')
            largura = input('Largura: ')
            peso = input('Peso: ')
            maletas.append(Maleta(codigo, float(altura), float(anchura), float(largura), float(peso)))
        else:
            break
    return maletas

def checkin_aeropuerto(pasajeros: list[Pasajero]):
    while True:
        if input('¿Quieres añadir un pasajero? (s/n): ') == 's':
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            talla = input('Talla (0-5): ')
            menu = input('Menú (normal / vegetariano / celiaco): ')
            if volumen_cabina(pasajeros) < 120000:
                cabina = annadir_maletas('¿Quieres añadir equipaje de cabina? (s/n): ')
            else:
                print('Sobrepasada la capacidad de maletas en cabina.')
                cabina = []
            facturado = annadir_maletas('¿Quieres añadir equipaje facturado? (s/n): ')
            pasajeros.append(Pasajero(nombre, apellido, talla, menu, cabina, facturado))
            print('Pasajero añadido.')
        else:
            break


tallas_peso = {
    0: 0,
    1: 20,
    2: 40,
    3: 60,
    4: 80,
    5: 100
}

def candidato_overbooking(pasajeros: list[Pasajero]) -> Pasajero:
    pesos_pasajeros = [tallas_peso[p.talla] + p.get_peso_total() for p in pasajeros]
    return pasajeros[pesos_pasajeros.index(max(pesos_pasajeros))]

def resumen_embarque(pasajeros: list[Pasajero]):
    print('Resumen del embarque:')
    print(f'{len(pasajeros)} pasajeros embarcados')
    menus_normales = len([p for p in pasajeros if p.menu == 'normal'])
    print(f'{menus_normales} menús normales')
    menus_vegetarianos = len([p for p in pasajeros if p.menu == 'vegetariano'])
    print(f'{menus_vegetarianos} menús vegetarianos')
    menus_celiacos = len([p for p in pasajeros if p.menu == 'celiaco'])
    print(f'{menus_celiacos} menús celiacos')
    peso_equipaje = sum([p.get_peso_total() for p in pasajeros])
    print(f'{peso_equipaje} kg de equipaje')
    peso_pasajeros = sum([tallas_peso[p.talla] for p in pasajeros])
    print(f'{peso_pasajeros} kg de pasajeros')

if __name__ ==  '__main__':
    print('DeustoAir: de Bilbao al cielo.\n\nCargando pasajeros online...\n')
    checkin_online(pasajeros)
    print(volumen_cabina(pasajeros))
    print('Registrando pasajeros en el aeropuerto...\n')
    checkin_aeropuerto(pasajeros)
    print('El mejor candidato para proponerle una compensación por overbooking es')
    print(candidato_overbooking(pasajeros))
    resumen_embarque(pasajeros)
