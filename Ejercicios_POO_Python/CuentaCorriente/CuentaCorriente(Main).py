from dni import *

##---Clase Cuenta Corriente---
class CuentaCorriente():

    ## Constructor del ADT Cuenta Corriente
    def __init__(self, nombre = "NoAsignado", apellidos = "NoAsignado", direccion = "NoAsignado", telefono = "NoAsignado", dni = "NoAsignado", saldo = 0.0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.NIF = Dni(dni)
        self.saldo = saldo

    ## Setters del ADT Cuenta Corriente
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setDni(self, dni):
        self.NIF.setDni(dni)

    def setSaldo(self, saldo):
        self.saldo = saldo

    ## Getters del ADT Cuenta Corriente
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getDireccion(self):
        return self.direccion

    def getTelefono(self):
        return self.telefono

    def getDni(self):
        return self.NIF.getDni()

    def getSaldo(self):
        return self.saldo

    ## Otros métodos y funciones

    # Subrutina: retirarDinero
    # Descripción: Resta el saldo dado por argumento al saldo de la instancia de CuentaCorriente
    # Entrada: 1 instancia Cuenta corriente y 1 saldo a restar
    # Salidas: Ninguna
    def retirarDinero(self, saldo):
        try:
            self.saldo = self.saldo - saldo
        except TypeError:
            print("El valor no es númerico")
            print()

    # Subrutina: ingresarDinero
    # Descripción: Suma el saldo dado por argumento al saldo de la instancia de CuentaCorriente
    # Entrada: 1 instancia Cuenta corriente y 1 saldo a sumar
    # Salidas: Ninguna
    def ingresarDinero(self, saldo):
        try:
            self.saldo = self.saldo + saldo
        except TypeError:
            print("El valor no es númerico")
            print()

    # Subrutina: consultarCuenta
    # Descripción: Muestra por pantalla los datos de una instancia Cuenta Corriente
    # Entrada: 1 Instancia Cuenta Corriente
    # Salidas: Ninguna
    def consultarCuenta(self):
        print ("Nombre: %s" % self.nombre)
        print ("Apellidos: %s" % self.apellidos)
        print ("Direccion: %s" % self.direccion)
        print ("Telefono: %s" % self.telefono)
        print ("NIF: %s" % self.getDni())
        print ("Saldo: %d" % self.saldo)
        print ()

    # Subrutina: saldoNegativo
    # Descripción: Comprueba si el saldo de una instancia Cuenta Corriente esta en numeros rojos (Negativo)
    # Entrada: 1 Instancia Cuenta Corriente
    # Salidas: 1 Booleano donde
    #   True: El saldo es negativo
    #   False: El saldo es positivo
    def saldoNegativo(self):
        if (self.saldo-self.saldo == 0):
            return True
        else:
            return False

##--Fin de la clase Cuenta corriente--

##---------------Tests----------------

if __name__ == '__main__':

    objeto = CuentaCorriente()
    objeto.setDni("12345678T")
    objeto.setNombre("Alfredo")
    objeto.setApellidos("lopes jimeno")
    objeto.setDireccion("NingunaParteLejana")
    objeto.setTelefono("124151262")
    objeto.setSaldo(40.0)

    objeto.consultarCuenta()
    objeto.ingresarDinero("a")
    objeto.consultarCuenta()
    objeto.retirarDinero(90.0)
    objeto.consultarCuenta()
    if objeto.saldoNegativo() == True:
        print("Estas pobre")
    else:
        print("Vas tirando")

#-----------Fin de los tests----------


        
