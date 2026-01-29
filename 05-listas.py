import os
os.system("cls")

'''
Una lista es una estructura de datos que permite almacenar varios
valores en una sola variable.

Las listas pueden contener datos del mismo o de distinto tipo 
y son notables (se pueden modificar)


'''
numeros=[1,2,3,4,5]
print(numeros)
nombres= ["Ana", "Luis", "Carlos"]
print(nombres)
mezcla=[10,"Hola", 3.5, True]
print(mezcla)

print(nombres[1])
print("|---------------------------------------------------|")
print(type(mezcla))

#agregar elementos a la lista
print(nombres)
nombres[1]="Pedro"
print(nombres)
#funcion append para agregar cualquier cosa a la lista
nombres.append("Juan")
print(nombres)
print(lista2)
lista2.append(1)
lista2.append(5)
lista2.append(7)
print(lista2)