import os
os.system ("cls")
#el while nos sirve para tareas repetitivas
'''programa en el que le voy a pedir al ususario 5 calificaciones
despues de pedirlas voy a imprimir el promedio de esas cinco cslificaciones 
hacer el diagrama de flujo y hacer el codigo en python'''

suma = 0
a = 1
while a <= 5:
    calif=int(input("Calificación {}: ".format(a)))
    suma=suma+calif
    a=a+1

promedio=suma/5
print("El promedio es el siguiente: {} ".format(promedio))