# Ejercicio que comprueba si un numero es superior a otro o son iguales.

#------Subrutinas a usar---------

# Subrutina: sumaCombinada
# Descripción: Dado 3 números comprueba si alguno de ellos es la suma de los otros 2.
# Entrada: 3 numeros
# Salidas: 1 numero con los siguientes posibles valores
#   1: El primer número es la suma del segundo y el tercero.
#   2: El segundo número es la suma del primero y el tercero.
#   3: El tercer número es la suma del primer y el segundo.
#   default: Los numeros no cumplen la condición del programa.

def sumaPositivos (primerNumero, segundoNumero, tercerNumero):
    if primerNumero == segundoNumero + tercerNumero:
        return 1
    elif segundoNumero == primerNumero + tercerNumero:
        return 2
    elif tercerNumero == primerNumero + segundoNumero:
        return 3
    else:
        return None
    
#------Fin de las subrutinas------

    
#-------Programa principal--------

print("Vamos a comprobar dado 3 números si alguno de ellos es la suma de los otros 2")
    
primerNumero = int(input("Introduzca un primer número: "))
segundoNumero = int(input("Introduzca un segundo número: "))
tercerNumero = int(input("Introduzca un tercer número: "))

valor = sumaPositivos(primerNumero, segundoNumero, tercerNumero)

print("Números introducidos: " + str(primerNumero) + "   " + str(segundoNumero) + " " + str(tercerNumero))
      
if valor == 1:
    print ("Se cumple que " + str(primerNumero) + " = " + str(segundoNumero) + " + " + str(tercerNumero))
elif valor == 2:
    print ("Se cumple que " + str(segundoNumero) + " = " + str(primerNumero) + " + " + str(tercerNumero))
elif valor == 3:
    print ("Se cumple que " + str(tercerNumero) + " = " + str(primerNumero) + " + " + str(segundoNumero))
else:
    print ("Los números no cumplen la condición.")
    
#---------Fin del programa--------
