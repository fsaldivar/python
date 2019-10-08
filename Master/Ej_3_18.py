'''
Ejercicio 18
Pedir el nombre y los dos apellidos de una
persona y mostrar las iniciales.
'''

nombre = str(input("Cual es tu nombre: "))
apellido = str(input("Cual es tu primer apellido: "))
apellido2 = str(input("Cual es tu segundo apellido: "))

y=nombre[0]+apellido[0]+apellido2[0]
print("Tus iniciales son:",y.upper())
