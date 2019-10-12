'''
Ejercicio 3
Escribe un programa que lea un número e indique si es par o impar.
'''

n1=int(input("Intruduce un numero: "))
n2=n1%2

if n2>0:
        print("El numero {} es IMPAR".format(n1))

if n2==0:
        print("El numero {} es PAR".format(n1))
