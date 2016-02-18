##---Clase Hora---
class Hora():

    ## Constructor del ADT Hora

    def __init__ (self, horas = 0, minutos = 0, segundos = 0):
        self.setHora(horas, minutos, segundos)

    ## Setters y Getters de ADT Hora

    def setHoras(self, horas):
        self.horas = horas
        
    def setMinutos(self, minutos):
        self.minutos = minutos
        
    def setSegundos(self, segundos):
        self.segundos = segundos

    def getHoras(self):
        return self.horas
        
    def getMinutos(self):
        return self.minutos
        
    def getSegundos(self):
        return self.segundos

    # Subrutina: setHora
    # Descripción: Establece las horas, minutos y segundos
    #              de la instancia de la clase Hora a la vez.
    # Entrada: 3 int los cuales pertenecen a: Horas:Minutos:Segundos
    # Salidas: Ninguna

    def setHora(self, horas, minutos, segundos):
        try:
            if horas > 0 and horas <= 24:
                self.horas = horas
            else:
                self.horas = 0
                
            if minutos > 0 and minutos <= 59:
                self.minutos = minutos
            else:
                self.minutos = 0
                
            if segundos > 0 and segundos <= 59:
                self.segundos = segundos
            else:
                self.segundos = 0
        except TypeError:
            print("Su hora contiene algun carácter numérico y la operación 'setHora' no se ha podido llevar a cabo")

    # Subrutina: getHora
    # Descripción: Devuelve la hora de una instancia Hora
    # Entrada: Ninguna
    # Salidas: Array con 3 posiciones:
    #   [0]: Horas
    #   [1]: Minutos
    #   [2]: Segundos
    
    def getHora(self):
        horaAux = (str(self.horas) + ":" + str(self.minutos) + ":" + str(self.segundos))
        return horaAux

    # Subrutina: imprimirHora
    # Descripción: Imprime la hora de la instancia Hora por pantalla
    # Entrada: Ninguna
    # Salidas: Ninguna

    def imprimirHora(self):
        print("Su hora es: " + self.getHora())
        

##---------------Tests----------------

if __name__ == '__main__':
    
    ##Caso test para constructor
    objeto = Hora()
    print(objeto.horas, objeto.minutos, objeto.segundos)
    objeto = Hora(46, 67, 24)
    print(objeto.horas, objeto.minutos, objeto.segundos)

    ##Caso test para setHora
    objeto.setHora('a', 24, 45)
    print(objeto.horas, objeto.minutos, objeto.segundos)
    objeto.setHora(22, 56, 12)
    print(objeto.horas, objeto.minutos, objeto.segundos)

    ##Caso test para getHora
    horaAux = objeto.getHora()
    print(horaAux)

    ##Caso test para imprimirHora
    objeto.imprimirHora()
        
#-----------Fin de los tests----------
