'''
Pedir cinco sueldos, agregarlos a una lista e imprimir:
promedio, sueldo más alto y sueldo más bajo
'''

import os
os.system("cls")

pedirsueldo = []
contad = 0

while contad < 5:
    tem = float(input("Dame el sueldo " + str(contad + 1) + ": "))
    pedirsueldo.append(tem)
    contad += 1


suelmay = max(pedirsueldo)
suelmen = min(pedirsueldo)
promsueld = sum(pedirsueldo) / len(pedirsueldo)

print("El sueldo mayor es:", suelmay)
print("El sueldo menor es:", suelmen)
print("El promedio de los sueldos es:", promsueld)
