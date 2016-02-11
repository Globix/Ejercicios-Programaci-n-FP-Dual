# Escribe un programa que pida por teclado dos valores de tipo numérico
# que se han de guardar en sendas variables. ¿Qué instrucciones habría que
# utilizar para intercambiar su contenido? (es necesario utilizar una variable
# auxiliar). Para comprobar que el algoritmo ideado es correcto, muestra en
# pantalla el contenido de las variables una vez leídas, y vuelve a mostrar
# su contenido una vez hayas intercambiado sus valores.

primerNum = input("Introduzca un número: ")
segundoNum = input("Introduzca otro número: ")

print("\nEl valor del primer número es: " + str(primerNum))
print("El valor del segundo número es: " + str(segundoNum))

print("\nAhora intercambiaremos el contenido de las variables entre si\n")

numAux = primerNum
primerNum = segundoNum
segundoNum = numAux

print("El valor del primer número es: " + str(primerNum))
print("El valor del segundo número es: " + str(segundoNum))
