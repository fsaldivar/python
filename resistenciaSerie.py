numero_resistencias=input("Introduce el numero de resistencias: ")
rTotal=[]
suma=0
val=0
val1=0

try:
   val = int(numero_resistencias)
except ValueError:
   print("Introduce un valor entero")


for i in range(1,val+1) :
    r = input("Introduce el valor de la resistencia %s : " %(i))

    try:
       val1 = int(r)
    except ValueError:
       print("Introduce un valor entero")

    print("El valor de la resistencia",i, "es igual a", r,"Ohms")
    rTotal.append(val1)


for j in rTotal:
    suma = suma + j

print("\nEl valor de la Resistencia Total es: ",suma, "Ohms")
