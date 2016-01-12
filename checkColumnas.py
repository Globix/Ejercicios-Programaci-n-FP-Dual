def checkColumnas(sudoku):
    sano = True
    for filaActual in sudoku:
        for indexFila in range(0, len(filaActual)):
            for indexColumna in range (sudoku.index(filaActual) + 1, len(sudoku)):
                if filaActual[indexFila] != sudoku[indexColumna][indexFila]:
                    pass
                else:
                    sano = False
                    return sano
    return sano

test = [[1,2,3],
        [2,3,1],
        [3,1,2]]
resultado = checkColumnas(test)
if resultado == True:
    print("CORRECTO")
else:
    print("INCORRECTO")
