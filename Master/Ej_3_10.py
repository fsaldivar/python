'''

Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:

    55% del promedio de sus tres calificaciones parciales.
    30% de la calificación del examen final.
    15% de la calificación de un trabajo final.

'''
cP01=int(input("introduce la calificacion de tu primer parcial: "))
cP02=int(input("introduce la calificacion de tu segundo parcial: "))
cP03=int(input("introduce la calificacion de tu tercer parcial: "))
cE01=int(input("introduce la calificacion de tu examen final: "))
cT01=int(input("introduce la calificacion de tu trabajo final: "))

cP=(cP01+cP02+cP03)/3

cF=0.55*cP+0.3*cE01+0.15*cT01

print("Tu calificacion final es de: {:.2f}".format(cF))

if cF>=70:
    print("Pasaste")
else:
    print("Reprobado")
