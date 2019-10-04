'''
Ejercicio 12
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
'''


import math as m

x1=int(input("Introduce el valor x1: "))
y1=int(input("Introduce el valor y1: "))
x2=int(input("Introduce el valor x2: "))
y2=int(input("Introduce el valor y2: "))
d= m.sqrt((x2-x1)**2+ (y2-y1)**2)
print("La distancia entre estos dos puntos es: {}".format(d))
