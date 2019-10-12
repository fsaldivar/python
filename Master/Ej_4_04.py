'''
Ejercicio 4
Crea un programa que pida al usuario dos números y muestre su
división si el segundo no es cero, o un mensaje de aviso en caso
contrario.
'''

n1=int(input("Introduce un numero: "))
n2=int(input("Introduce otro numero: "))

if n2==0:
    print("No se puede dividir entre 0")
else:
    print("La division {}/{} = {}".format(n1,n2,n1/n2))
