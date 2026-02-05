import os
os.system ("cls")
'''
crea un programa que pida al ususario ingresar numeros
el programa debe sumar todos los numeros ingresados
el programa debe terminar cuando el usuario ingrese el numero cero
al finalizar el programa, imprimir la suma total de los numeros ingresados
 ejemplo de salida:
 ingresa un numero (0 para terminar): 5
 ingresa un numero (0 para terminar): 10
 ingresa un numero (0 para terminar): 3
 ingresa un numero (0 para terminar):0
 la suma total de los numeros ingresados es: 18.
'''
suma=0
num=1
while  num != 0:
  num=int(input("Ingrese el numero: "))
  if num != 0:
   suma=suma+num
print("Suma total de los numeros: {}".format(suma))