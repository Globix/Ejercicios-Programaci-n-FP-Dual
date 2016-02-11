# Escribe un programa que calcule el área de una finca rectangular en metros
# cuadrados, así como su perímetro exterior, también en metros.

base = float(input("Introduzca la base del rectangulo en metros: "))
altura = float(input("Introduzca la altura del rectangulo en metros: "))

print ("El área de su finca es de: " + str(base*altura) + " m²")
print ("El perimetro de su finca es de: " + str((base*2)+(altura*2)) + " m")
