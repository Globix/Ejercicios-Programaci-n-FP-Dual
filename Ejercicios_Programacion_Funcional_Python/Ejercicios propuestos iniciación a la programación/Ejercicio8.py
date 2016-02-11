# Ejercicio que comprueba si un numero es superior a otro o son iguales.

#------Subrutinas a usar---------

# Subrutina: esPositivo
# Descripción: Compara 2 numeros y muestra cual es el valor relacionado entre ellos
# Entrada: 2 numeros
# Salida: 1 numero con los posibles valores
#   1: El primer numero es superior al segundo
#   2: El segundo numero es superior al primero
#   3: Ambos numeros son iguales

def esPositivo (primerNumero, segundoNumero):
    if primerNumero > segundoNumero:
        return 1
    if segundoNumero > primerNumero:
        return 2
    else:
        return 3
    
#------Fin de las subrutinas------

    
#-------Programa principal--------

print ("Dados 2 números introducidos por teclado comprobemos cual es mayor.")

primerNumero = int(input("Introduzca un número: "))
segundoNumero = int(input("Introduzca un segundo número: "))

valor = esPositivo(primerNumero, segundoNumero)
    
if valor == 1:
    print ("El primer número '" + str(primerNumero) + "' es mayor que el segundo '" + str(segundoNumero) + "'")
elif valor == 2:
    print ("El segundo número '" + str(segundoNumero) + "' es mayor que el primero '" + str(primerNumero) + "'")
elif valor == 3:
    print ("Los dos números són iguales")
    
#---------Fin del programa--------
