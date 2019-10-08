'''
Ejercicio 20
Diseñar un algoritmo que nos diga el dinero que tenemos
(en pesos y centavos) después de pedirnos cuantas monedas
tenemos (10,5,2,1 o 50 centavos o 10 centavos).
'''
diez=int(input("Cuantas monedas de 10 pesos tienes: "))
cinco=int(input("Cuantas monedas de 5 pesos tienes: "))
dos=int(input("Cuantas monedas de 2 pesos tienes: "))
uno=int(input("Cuantas monedas de 1 peso tienes: "))
cincuenta=int(input("Cuantas monedas de 50 centavos tienes: "))
decimo=int(input("Cuantas monedas de 10 centavos tienes: "))

pesos=(cincuenta*50+decimo*10)//100
centavos=(cincuenta*50+decimo*10)%100

total=diez*10+cinco*5+dos*2+uno*1+pesos

print("Tienes {} pesos con {} centavos".format(total,centavos))
