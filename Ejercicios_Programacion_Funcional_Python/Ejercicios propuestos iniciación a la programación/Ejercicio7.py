#Ejercicio que comprueba si un numero es positivo o negativo.

#Subrutinas a usar
def esPositivo (numeroPrueba):
    if numeroPrueba >= 0:
        return True
    else:
        return False
    
#Aquí empieza el programa principal
numAux = int(input("Introduzca un número para descubrir su signo: "))    
    
if esPositivo(numAux):
    print ("El número leído es positivo")
else:
    print ("El número leído es negativo")
