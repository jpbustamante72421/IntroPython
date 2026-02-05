import math,os

os.system("cls")


print("|Figuras Geometricas|")


print("1.- Triangulo")
print("2.- Cuadrado")
print("3.- Circulo")
print("4.- Pentagono")
print("5.- Salir")
menu = int(input("Seleccione una opcion(1/2/3/4/5): "))
print("Usted seleccionó:",menu)

if menu == 1: 
    base=int(input("Ingrese la medida de la base: "))
    altura=int(input("Ingrese la medida de la altura: "))
    area=(base*altura)/2
    print("El area del triangulo es: ",area)

if menu == 2: 
    lado=int(input("Ingrese la medida del lado: "))
    area=(lado*lado)
    print("El area del cuadrado es: ",area)

if menu == 3: 
    diametro=int(input("Ingrese la medida del diametro del circulo: "))
    radio = diametro/2
    area=3.1416 * radio ** 2
    print("El area del circulo es: ",area)

if menu == 4:
    lado=int(input("Ingrese la medida del lado: "))
    perimetro=lado*5    
    apotema=int(input("Ingrese la medida del apotema: "))
    area=perimetro*apotema/2
    print("El area del pentagono es: ",area)

if menu == 5:
    print("Finalizando el programa")

else:
    print("Opcion Invalida")