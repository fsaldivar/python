'''

Ejercicio 11
Pide al usuario dos números y muestra la “distancia” entre ellos
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).


'''

cP01=int(input("introduce un numero: "))
cP02=int(input("introduce otro numero: "))

if cP01>cP02:
    print("La distancia entre ellos es: {}" .format(cP01-cP02))
else:
    print("La distancia entre ellos es: {}" .format(cP02-cP01))
