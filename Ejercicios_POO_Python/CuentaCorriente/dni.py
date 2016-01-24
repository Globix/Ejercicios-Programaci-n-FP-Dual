class Dni():

        def __init__(self, cadena = ''):
            self.dni  = cadena

        def setDni(self, cadena):
            self.dni = cadena

        def getDni(self):
            return self.dni

if __name__ == 	'__main__':

	objeto = Dni()

	print(objeto.dni)

	otro = Dni()
	otro.setDni('A2345678X')
	print(otro.dni)
