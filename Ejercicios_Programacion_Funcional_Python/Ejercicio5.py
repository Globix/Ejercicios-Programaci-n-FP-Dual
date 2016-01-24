# Escribe un programa que calcule lo que tiene que cobrar un empleado
# sabiendo que se le tieneque aplicar al sueldo una retención del 20%.

RETENCION = 20#%
sueldo = float(input("Introduzca el sueldo del empleado: "))


print ("El sueldo con la retención del 20% es de: " + str(sueldo-(sueldo*RETENCION/100)) + "€")
