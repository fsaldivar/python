'''
Ejercicio 14
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
Ejemplo, si se introduce 23 que muestre 32.
'''

num = str(input("Dime el número:"))
x=list(num)
y=x[::-1]
y="".join(y)

print("{} <--> {}".format(num,y))
