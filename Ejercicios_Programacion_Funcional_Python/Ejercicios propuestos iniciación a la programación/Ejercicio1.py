# Escribe un programa que pida por teclado un número entero mostrando un mensaje oportuno.
# A continuación escribe en pantalla el número leído, el doble del número leído y el triple del mismo.

#------Subrutinas a usar---------

# Subrutina: printNumero
# Descripción: Imprime un número introducido por atributo.
# Entrada: 1 número
# Salida: 1 print por pantalla

def printNumero(numero):
    if not isinstance(numero, float):
        return None
    else:
        print ("El número introducido es: " + str(numero))
        return 1

# Subrutina: printDobleDeNumero
# Descripción: Imprime el doble de un número introducido por atributo.
# Entrada: 1 número
# Salida: 1 print por pantalla

def printDobleDeNumero(numero):
    if not isinstance(numero, float):
        return None
    else:
        print ("El doble del número introducido es: " + str(numero*2))
        return 1
    

# Subrutina: printTripleDeNumero
# Descripción: Imprime el doble de un número introducido por atributo.
# Entrada: 1 número
# Salida: 1 print por pantalla

def printTripleDeNumero(numero):
    if not isinstance(numero, float):
        return None
    else:
        print ("El triple del número introducido es: " + str(numero*3))
        return 1
    

#------Fin de las subrutinas------

    
#-------Programa principal--------

numero = float(input("Introduzca un número: "))

if None == printNumero(numero):
    print ("Error, el valor introducido no es un número")
else:
    printDobleDeNumero(numero)
    printTripleDeNumero(numero)

#---------Fin del programa--------


