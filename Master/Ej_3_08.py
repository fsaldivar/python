#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
#el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por
#las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
#en cuenta su sueldo base y comisiones.

sB=int(input("Introduce tu sueldo base: "))
v01=int(input("Introduce tu venta 01: "))
v02=int(input("Introduce tu venta 02: "))
v03=int(input("Introduce tu venta 03: "))
comisiones=(v01+v02+v03)*0.1
total=sB+comisiones

print("Tus comisiones por las 3 ventas son: {}".format(comisiones))
print("Tu sueldo base + comisiones es: {}".format(total))
