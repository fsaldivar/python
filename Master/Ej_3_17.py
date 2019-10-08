'''
Ejercicio 17
Un ciclista parte de una ciudad A a las HH horas,
MM minutos y SS segundos. El tiempo de viaje hasta
llegar a otra ciudad B es de T segundos. Escribir un
algoritmo que determine la hora de llegada a la ciudad B.
'''

horas=int(input("Introduce la hora de la salida HH: "))
minutos=int(input("Introduce el minuto de la salida MM: "))
segundos=int(input("Introduce el segundo de la salida SS: "))

t1=int(input("Introduce el tiempo en segundos del viaje: "))





t2=horas*60*60+minutos*60+segundos
t3=t2+t1
HH=t3//3600
MM=t3//60-HH*60
SS=t3-MM*60-HH*3600


r=0

print("El ciclista llegará a su destino a las: {}:{}:{}".format(HH,MM,SS))
