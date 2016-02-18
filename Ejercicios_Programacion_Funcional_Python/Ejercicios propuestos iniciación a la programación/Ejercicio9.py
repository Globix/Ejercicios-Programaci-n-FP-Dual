# Ejercicio que comprueba si un numero es superior a otro o son iguales.

#------Subrutinas a usar---------

# Subrutina: sumaPositivos
# Descripción: Suma 2 numeros solo si ambos son positivos
# Entrada: 2 numeros
# Salidas:
#   - "None" Si alguno de los 2 numeros es negativo
#   o
#   - Resultado con la suma de los 2 numeros

def sumaPositivos (primerNumero, segundoNumero):
    if primerNumero < 0 or segundoNumero < 0:
        return None
    else:
        return primerNumero + segundoNumero
    
#------Fin de las subrutinas------

    
#-------Programa principal--------
    
print ("Vamos a realizar la suma de 2 numeros positivos")
    
primerNumero = int(input("Introduzca un número: "))
segundoNumero = int(input("Introduzca un segundo número: "))

resultado = sumaPositivos(primerNumero, segundoNumero)
    
if resultado == None:
    print("No se calcula la suma porque alguno de los números o los dos no son positivos")
else:
    print("La suma de los dos números es: " + str(resultado))
    
#---------Fin del programa--------
