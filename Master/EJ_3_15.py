'''
Ejercicio 15
Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
los valores de ambas variables y muestre cuanto valen al final las dos variables.

'''

A = str(input("Introduce un valor numero para la variable A: "))
B = str(input("Introduce un valor numero para la variable B: "))

print("El valor original de A es: ",A)
print("El valor original de B es: ",B)

a=B
B=A
A=a

print("El valor nuevo de A es : ",A)
print("El valor nuevo de B es : ",B)
