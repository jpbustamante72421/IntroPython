import math,os

os.system("cls")

print("|Calculadora de Impuestos|")
sueldo=int(input("Ingrese el sueldo de la persona: "))

if sueldo<1000:
   impuesto=0
   print("No paga ningun impuesto")

if sueldo >= 1000 and sueldo <= 2000:
   impuesto = sueldo * .10
   print("Se amuenta el 10% de impuesto")

else:
   impuesto= sueldo * .20   
   print("Se aumenta el 20% de impuesto")

suelneto=sueldo-impuesto
print("El impuesto es: ",impuesto)
print("El sueldo neto es: ",suelneto)