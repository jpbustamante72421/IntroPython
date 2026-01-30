'''
Crear un programa que permita realizar la multiplicacion de A*B
sin utilizar multiplicaciones, deberas utilizar el ciclo while y
pedir dos numeros.
'''

import os
os.system("cls")

print("|°MULTIPLICACR AxB°|")

numeroA=int(input("Ingrese el pimer número: "))
numeroB=int(input("Ingrese el segundo número: "))

comilla=''
operacion=0

while numeroB > 0:
    operacion=operacion+numeroA
    numeroB=numeroB-1
    comilla=comilla+'{}+'.format(numeroA)
print("El resultado es:{}={}".format(comilla,operacion))