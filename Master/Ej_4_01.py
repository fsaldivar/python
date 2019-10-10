'''
Ejercicio 1

Algoritmo que pida dos números e
indique si el primero es mayor que el segundo o no.
'''
n1=int(input("Intruduce el primer numero: "))
n2=int(input("Intruduce el segundo numero: "))

if n1>n2:
    print("El numero 1 es mayor al numero 2: {} > {}".format(n1,n2))

if n2>n1:
    print("El numero 1 es menor al numero 2: {} < {}".format(n1,n2))

if n1==n2:
    print("El numero 1 es igual al numero 2: {} = {}".format(n2,n1))
