# Ejercicio que calcula el valorNeto de un precio aplicando distintos descuentos según el valorBruto.

#------Subrutinas a usar---------

# Subrutina: calcularValorNeto
# Descripción: Dado un valorBruto calcula el valorNeto
# Entrada: 1 numero
# Salidas: 1 numero 
#   -1: El primer numero es negativo y por lo tanto no se puede producir la suma.
#   -2: El segundo numero es negativo y por lo tanto no se puede producir la suma.
#   -3: Ambos numeros son negativos y por lo tanto no se puede producir la suma.
#   default: Suma de los numeros.

def calcularValorNeto(valorBruto):
    if valorBruto <= 20:
        valorNeto = valorBruto
        return valorNeto
    elif valorBruto > 20 and valorBruto <= 100:
        descuento = valorBruto * 5 / 100 ## Calculamos el 5% del valorBruto para descontarlo
        valorNeto = valorBruto - descuento
        return valorNeto
    elif valorBruto > 100:
        descuento = valorBruto * 10 / 100 ## Calculamos el 10% del valorBruto para descontarlo
        valorNeto = valorBruto - descuento
        return valorNeto
    else:
        return 
    
#------Fin de las subrutinas------

#-------Programa principal--------

calcular 

#---------Fin del programa--------

#--------------Tests--------------

if __name__  == '__main__':

    if valorBruto <= 20 and valorNeto = valorBruto:
        print("OK")
    else:
        print("FAIL")
##    if valorBruto > 20 and valorBruto <=100 and valorNeto = valorBruto:
##        print("OK")
##    else:
##        print("FAIL")
##    if valorBruto > 100 and valorBruto = valorNeto:
##        print("OK")
##    else:
##        print("FAIL")

#----------Fin de Tests-----------
