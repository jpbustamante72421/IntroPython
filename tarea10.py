'''
Realizar un programa que le pida al ususario un numero 
y el programa debera imprimir la piramide de asteriscos segun el numero capturado
'''
import os
os.system("cls")
print("|°PIRAMIDE°|")
numsoli=int(input("Ingrese el número que desee: "))

for x in range (1,numsoli+1):
    print("*" * x)