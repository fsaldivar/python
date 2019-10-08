'''
Ejercicio 19
Escribir un algoritmo para calcular la nota final
de un estudiante, considerando que: por cada respuesta correcta
5 puntos, por una incorrecta -1 y por respuestas en blanco 0.
Imprime el resultado obtenido por el estudiante.

'''
respuestaCorrecta=int(input("Introduce el numero de respuestas correctas: "))
respuestaIncorrecta=int(input("Introduce el numero de respuestas incorrectas: "))
respuestaBlanco=int(input("Introduce el numero de respuestas en blanco: "))

r=respuestaCorrecta*5+respuestaIncorrecta*(-1)

print("El resultado final es de: {} puntos".format(r))
