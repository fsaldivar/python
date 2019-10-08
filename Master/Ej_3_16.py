'''
Dos vehículos viajan a diferentes velocidades (v1 y v2) y
están distanciados por una distancia d. El que está detrás
viaja a una velocidad mayor. Se pide hacer un algoritmo para
ingresar la distancia entre los dos vehículos (km) y sus
respectivas velocidades (km/h) y con esto determinar y
mostrar en que tiempo (minutos) alcanzará el vehículo más
rápido al otro.
'''
d=int(input("Introduce la distancia entre ambos vehiculos en km: "))
v1=int(input("Introduce la velocidad del vehiculo 1 (km/h): "))
v2=int(input("Introduce la velocidad del vehiculo 2 (km/h): "))

v1=v1*(1/60)
v2=v2*(1/60)

r=d/(v2-v1)


print("El vehiculo 2 alcanzará al vehiculo 1 en {} minutos".format(r))
