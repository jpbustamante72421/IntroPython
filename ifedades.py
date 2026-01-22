import math,os

os.system("cls")

print("|-----Comparacion de Edades-----|")
edad1=int(input("Ingrese la primer edad: "))
edad2=int(input("Ingrese la segunda edad: "))

if edad1>edad2:
    print("La Primer Persona es Mayor".format(edad1,edad2))
if edad1<edad2:
    print("La Segunda Persona es Mayor". format(edad1,edad2))
if edad1==edad2:
    print("Las Dos Personas Tienen La Misma Edad". format(edad1,edad2))