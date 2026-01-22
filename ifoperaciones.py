import math,os

os.system("cls")
print("Seleccione una opcion(1/2/3/4): ")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
menu=int(input("Ingrese la Operacion a Realizar: "))
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

if menu==1:
    suma=num1+num2
    print("La Suma de {} y {} es: {}".format(num1,num2,suma))

if menu==2:
    resta= num1-num2
    print("La Resta de {} y {} es: {}".format(num1,num2,resta))

if menu==3:
    multiplicacion=num1*num2
    print("La Multiplicacion de {} y {} es: {}".format(num1,num2,multiplicacion))

if menu==4:
    division=num1/num2
    print("La Division de {} y {} es: {}".format(num1,num2,division))

if(menu!=1 or menu!=2 or menu!=3 or menu!=4):
    print("Opcion no valida")