##---Imports necesarios para utilizar la clase TarjetaPrepago---
from dni import *
from Hora import *

##---Clases para manejo de excepciones---
class Error(Exception):
    pass

class ValorNegativo(Error):
    def __init__(self, mensaje, valor):
        self.mensaje = mensaje
        self.valor = valor

##---Clase TarjetaPrepago---

class TarjetaPrepago:

    ## Constructor del ADT TarjetaPrepago

    def __init__(self, numeroTelefono = "NoAsignado", dni = "NoAsignado", saldo = 0):
        self.numeroTelefono = numeroTelefono
        self.NIF = Dni(dni)
        self.saldo = saldo
        self.consumo = Hora()

    ## Setters y Getters de ADT TarjetaPrepago

    def setNumeroTelefono(self, numeroTelefono):
        self.numeroTelefono = numeroTelefono

    def setNIF(self, dni):
        self.NIF.setDni(dni)

    def setSaldo(self, Saldo):
        self.Saldo = Saldo

    def setConsumo(self, consumo, horas, minutos, segundos):
        self.consumo.setHoras(horas)
        self.consumo.setMinutos(minutos)
        self.consumo.setSegundos(segundos)

    def getNumeroTelefono(self):
        return self.numeroTelefono

    def getNIF(self):
        return self.NIF.getDni()

    def getSaldo(self):
        return self.saldo

    def getConsumo(self):
        return self.consumo.getHora()

    # Subrutina: ingresarSaldo
    # Descripción: Ingresa un saldo en la instancia de TarjetaPrepago
    # Entrada: 1 int con el saldo a ingresar
    # Salidas: Ninguna

    def ingresarSaldo(self, saldoAIngresar):
        try:
            if saldoAIngresar < 0:
                raise ValorNegativo("El saldo a añadir es negativo: ", saldoAIngresar)
            else:
                self.saldo = self.saldo + saldoAIngresar
        except ValorNegativo as error:
            print(error.mensaje + str(error.valor))
        except TypeError:
            print("El valor no es númerico")

    # Subrutina: enviarMensaje
    # Descripción: Resta un saldo segun los mensajesEnviados en la instancia de TarjetaPrepago
    # Entrada: 1 int con el numero de mensajes para calcular el saldo a restar
    # Salidas: Ninguna

    def enviarMensaje(self, numeroMensajes):
        try:
            if numeroMensajes < 0:
                 raise ValorNegativo("El numero de Mensajes a enviar es negativo: ", numeroMensajes)
            else:
                saldoARestar = numeroMensajes * 9
                self.saldo = self.saldo - saldoARestar
        except ValorNegativo as error:
            print(error.mensaje + str(error.valor))
        except TypeError:
            print("El valor no es númerico")

    # Subrutina: realizarLlamada
    # Descripción: Resta un saldo segun los mensajesEnviados y actualiza el consumo
    #              en la instancia de TarjetaPrepago
    # Entrada: 1 int con el numero de mensajes para calcular el saldo a restar
    # Salidas: Ninguna

    def realizarLlamada(self, numeroSegundos):
        try:
            if numeroSegundos < 0:
                raise ValorNegativo("El numero de segundos consumidos es negativo: ", numeroSegundos)
            else:
                saldoARestar = numeroSegundos + 15
                self.saldo = self.saldo - saldoARestar
                horas, minutos, segundos = self.__calcularConsumo(numeroSegundos)
                self.setConsumo(self.consumo, horas, minutos, segundos)
        except ValorNegativo as error:
            print(error.mensaje + str(error.valor))
        except TypeError:
            print("El valor no es númerico")

    # Subrutina: consultarTarjeta
    # Descripción: Imprime los atributos de la instancia TarjetaPrepago por pantalla
    # Entrada: Ninguna
    # Salidas: Ninguna

    def consultarTarjeta(self):
        print ("NumeroTeléfono: %s" % self.numeroTelefono)
        print ("Saldo: %d" % self.saldo)
        print ("NIF: %s" % self.getNIF())
        print ("Consumo: %s" % self.consumo.getHora())

    # Subrutina: __calcularConsumo
    # Descripción: Calcula el consumo en horas, minutos y segundos.
    # Entrada: 1 int con los segundos consumidos.
    # Salidas: 3 int con las horas, minutos y segundos consumidos.

    def __calcularConsumo(self, numeroSegundos):
        if numeroSegundos > 59:
            numeroMinutos = numeroSegundos//60
            numeroSegundos = numeroSegundos%60
            if numeroMinutos > 59:
                numeroHoras = numeroMinutos//60
                numeroMinutos = numeroMinutos%60
                return numeroHoras, numeroMinutos, numeroSegundos
            else:
                return 0, numeroMinutos, numeroSegundos
        else:
            return 0, 0, numeroSegundos
        

##---------------Tests----------------

#Caso Test para constructor
objeto = TarjetaPrepago()
print(objeto.getNumeroTelefono(), objeto.getNIF(), objeto.getSaldo(), objeto.getConsumo())
print("")

objeto.consultarTarjeta()
print("")

objeto = TarjetaPrepago(663230195, "56124603H", 50)

#Caso Test para ingresarSaldo
objeto.ingresarSaldo(-60)
objeto.ingresarSaldo("a")
objeto.ingresarSaldo(5000)
print("")

objeto.consultarTarjeta()
print("")

#Caso Test para enviarMensaje
objeto.enviarMensaje(-5)
objeto.enviarMensaje("Hola")
objeto.enviarMensaje(2)
print("")

objeto.consultarTarjeta()
print("")

#Caso Test para realizarLlamada
objeto.realizarLlamada(-2)
objeto.realizarLlamada("paosda")
objeto.realizarLlamada(3665)
print("")

objeto.consultarTarjeta()
print("")

###Caso Test para calcularConsumo
##objeto2 = TarjetaPrepago()
##horas, minutos, segundos = objeto2.__calcularConsumo(59)
##if horas == 0 and minutos == 0 and segundos == 59:
##    print("OK")
##else:
##    print("ERROR")

#-----------Fin de los tests----------

    
