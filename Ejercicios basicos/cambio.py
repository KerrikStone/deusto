'''
Erik Coruña Rodríguez
20-09-2022
Define el coste de una compra y el dinero que se ha pagado para devolver los cambios en monedas de 2 €, 1 €, 50 c., 20 c., 10 c., 5 c. y 1c.
'''

coste = 18.78
pagado = 20
devolver = round(pagado - coste, 2)

devolver_2 = devolver // 2
devolver = round(devolver - devolver_2 * 2, 2)
devolver_1 = devolver // 1
devolver = round(devolver - devolver_1, 2)
devolver_50 = devolver // 0.5
devolver = round(devolver - devolver_50 * 0.5, 2)
devolver_20 = devolver // 0.2
devolver = round(devolver - devolver_20 * 0.2, 2)
devolver_10 = devolver // 0.1
devolver = round(devolver - devolver_10 * 0.1, 2)
devolver_05 = devolver // 0.05
devolver = round(devolver - devolver_05 * 0.05, 2)
devolver_02 = devolver // 0.02
devolver = round(devolver - devolver_02 * 0.02, 2)
devolver_01 = devolver // 0.01
devolver = round(devolver - devolver_01 * 0.01, 2)
print(f'{devolver_2} monedas de 2€\n{devolver_1} monedas de 1€\n{devolver_50} monedas de 50c\n{devolver_20} monedas de 20c\n{devolver_10} monedas de 10c\n{devolver_05} monedas de 5c\n{devolver_02} monedas de 2c\n{devolver_01} monedas de 1c')
