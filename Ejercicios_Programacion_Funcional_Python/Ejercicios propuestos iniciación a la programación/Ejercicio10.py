# Ejercicio que comprueba si un numero es superior a otro o son iguales.

#------Subrutinas a usar---------

# Subrutina: sumaPositivos
# Descripción: Suma 2 numeros solo si ambos son positivos
# Entrada: 2 numeros
# Salidas: 1 numero con los posibles valores
#   -1: El primer numero es negativo y por lo tanto no se puede producir la suma.
#   -2: El segundo numero es negativo y por lo tanto no se puede producir la suma.
#   -3: Ambos numeros son negativos y por lo tanto no se puede producir la suma.
#   default: Suma de los numeros.

def sumaPositivos (primerNumero, segundoNumero):
    if primerNumero < 0 and segundoNumero <0:
        return -3
    elif primerNumero < 0:
        return -1
    elif segundoNumero < 0:
        return -2
    else:
        return primerNumero + segundoNumero
    
#------Fin de las subrutinas------

    
#-------Programa principal--------
print ("Vamos a realizar la suma de 2 numeros positivos")
    
primerNumero = int(input("Introduzca un número: "))
segundoNumero = int(input("Introduzca un segundo número: "))

valor = sumaPositivos(primerNumero, segundoNumero)
    
if valor == -1:
    print ("No se calcula la suma porque el primer número es negativo.")
elif valor == -2:
    print ("No se calcula la suma porque el segundo número es negativo.")
elif valor == -3:
    print ("No se calcula la suma porque los dos números son negativos.")
else:
    print ("La suma de los dos números es: " + str(valor))
    
#---------Fin del programa--------
