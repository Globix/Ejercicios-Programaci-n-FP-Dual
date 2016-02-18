def desglosarDinero(importeRestante, valoresDinero):
    importeDesglosado = []
    if importeRestante < 0:
        return 0
    for valorActual in range(0, len(valoresDinero)-1):
        importeDesglosado.append(importeRestante//valoresDinero[valorActual])
        importeRestante = importeRestante%valoresDinero[valorActual]
    return importeDesglosado

def imprimirImporteDesglosado(importeDesglosado, valoresDinero):
    stringAImprimir = ""
    if not importeDesglosado:
        return 0
    for i in range(0, len(importeDesglosado)-1):
        if (importeDesglosado[i] != 0):
            stringAImprimir = (stringAImprimir + str(importeDesglosado[i])[0] + " de " +  str(valoresDinero[i]) + "€, ")
            #He cogido solo la posicion 0 del str importeDesglosado para pillar la parte entera de cada numero float y que al imprimirlo quede mejor.
    print("El importe es de: " + stringAImprimir[0:-2] + ".")
    #El stringAImprimir esta hasta -2 para que no me introduzca una ultima ,
    return 1

valoresDinero = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]                     
importeTotal = float(input("Introduzca el importe a desglosar: "))
importeDesglosado = desglosarDinero(importeTotal, valoresDinero)
if importeDesglosado:
    print("Paso la rutina desglosarDinero OK")
else:
    print("No paso la rutina desglosarDinero ERROR")
resultado = imprimirImporteDesglosado(importeDesglosado, valoresDinero)
if resultado == 1:
    print("Paso la rutina imprimirImporteDesglosado OK")
else:
    print("No paso la rutina imprimirImporteDesglosado ERROR")

