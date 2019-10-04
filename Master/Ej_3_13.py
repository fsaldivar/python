'''
Ejercicio 13
Realizar un algoritmos que lea un número y que muestre su raíz cuadrada
y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita
calcular la raíz cúbica, ¿Cómo se puede calcular?
'''

import math as m
num = int(input("Dime el número:"))
print("Raíz cuadrada:",m.sqrt(num))
print("Raíz cuadrada:",num ** (1 / 2))
print("Raíz cúbica:",num ** (1 / 3))
