import math,os

os.system ("cls")

print ("Calificaciones")

calif=int(input("Ingrese la calificación: "))

if calif>=7:
    if calif>=9:
        print("Excelente")
    else:
        print("aprobado")
else:
    print("reprobado")  
