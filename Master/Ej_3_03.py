import math as mt
print("Calculo de hipotenusa apartir de sus catetos")
print("")
cat01=input("Introduce el valor del cateto01 en cm: ")
cat01=float(cat01)

cat02=input("Introduce el valor del cateto02 en cm: ")
cat02=float(cat02)

hipo01= mt.sqrt(cat01**2+cat02**2)
print("La hipotenusa es: {} cm" .format(hipo01))
