print("Calculo del perimetro y area de un rectangulo")
print("")
base=input("Introduce la base del rectangulo en cm: ")
base=float(base)
altura=input("Introduce la altura del rectangulo en cm: ")
altura=float(altura)
perimetro = 2*base+2*altura
area=(base*altura)/2
print("El perimetro del rectangulo es: {} cm" .format(perimetro))
print("El area del rectangulo es: {} cm2" .format(area) )
