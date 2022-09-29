'''
Erik Coruña
29/09/2022
Crea una lista con 10 números enteros desordenada y ordénala
por el método de la burbuja.
'''
def bubbleSort(lista):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(lista) - 1):
            if lista[i] > lista [i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambio = True


lista = [12, 5, 6, 1, 22, 3, 8, 9, 11, 10]
bubbleSort(lista)
print(lista)
