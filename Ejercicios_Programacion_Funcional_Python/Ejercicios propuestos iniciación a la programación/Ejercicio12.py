# Ejercicio que pide dos números y comprueba unas condiciones prestablecidas.
# Si dichos números las pasan se realiza la suma de ambos y se muestra por pantalla.

#------Subrutinas a usar---------

# - Subrutina: sumaCondicinal
# - Descripción: Suma 2 numeros solo si se cumplen las siguientes 3 condiciones:
#   a) Los dos son pares 
#   b) El primero es menor que cincuenta 
#   c) El segundo está dentro del intervalo cerrado 100-500. 
# - Entrada: 2 numeros
# - Salidas:
#    -> -1: Si no se cumple la primera condición
#    -> -2: Si no se cumple la segunda condición
#    -> -3: Si no se cumple la tercera condición
#    -> Default: Resultado con la suma de los 2 numeros

def sumaPositivos (primerNumero, segundoNumero):
    if primerNumero%2==1 or segundoNumero%2==1:
        return -1
    elif primerNumero > 50:
        return -2
    elif segundoNumero < 100 or segundoNumero > 500:
        return -3
    else:
        return primerNumero + segundoNumero
    
#------Fin de las subrutinas------

    
#-------Programa principal--------
    
print ("Vamos a realizar la suma de 2 numeros positivos solo si se cumple que: \n - Los 2 son pares. \n - El primero es menor que cincuenta. \n - El segundo está dentro del intervalo cerrado 100-500.\n")
    
primerNumero = int(input("Introduzca un número: "))
segundoNumero = int(input("Introduzca un segundo número: "))
print("\n")

valor = sumaPositivos(primerNumero, segundoNumero)
    
if valor == -1:
    print ("No se calcula la suma porque un número és impar o ambos són impares.")
elif valor == -2:
    print ("No se calcula la suma porque el primer número es menor que 50.")
elif valor == -3:
    print ("No se calcula la suma porque el segundo número no esta entre el intervalo 100-500.")
else:
    print ("La suma de los dos números es: " + str(valor))
    
#---------Fin del programa--------
