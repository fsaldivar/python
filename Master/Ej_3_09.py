'''
Ejercicio 9
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuanto deberá pagar finalmente por su compra.
'''
totalCompra=int(input("Introduce el total de tu compra:"))
descuento = totalCompra*0.15
dTotalCompra=totalCompra-descuento
print(" Tu compra es de: ${} ".format(totalCompra))
print(" Tu descuento es de: ${} ".format(descuento))
print(" Tu pago debe ser de: ${} ".format(dTotalCompra))
