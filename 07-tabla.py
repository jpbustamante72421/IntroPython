'''
crear un programa que pida un numero al usuario, una vez
que el usuario ingrese el numero, la salida debe de ser
la tabla de multiplicar de ese numero.

'''
import os
os.system("cls")
print("|°TABLA°|")
numero=int(input("Ingrese un número: "))
v=range(1,11)
for z in range(1,11):
    tabla=numero*z
    print("{} + {} = {}".format (numero,z,tabla))