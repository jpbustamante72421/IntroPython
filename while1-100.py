'''realizar un programa que le pida al usuario un numero comprendido entre el 1 y 100
si el usuario escribe -7 mandar u  mensaje que diga "numero no valido" y
que vuelva a pedir un numero, si el numero es permitido que lo de en binario'''


'''
// division entera
/ division con decimal
% 

''' 
import math,os

os.system("cls")

num=int(input("Ingrese un numero :"))

while num < 1 or num > 100:
    print("Número no válido")
    num=int(input("Vuelva a intentar con otro número de entre 1-100: "))
print("Número valido: ",num)  

decimal=1
bin=0
while num >0:
        res=num%2
        bin= bin + res*decimal
        decimal=decimal *10
        num=num//2
print("El número en binario  es: ",bin)
