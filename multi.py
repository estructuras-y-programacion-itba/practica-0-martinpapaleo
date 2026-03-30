class Humano():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def saludar(self):
        print('Hola , soy',self.nombre,'mucho gusto de conocerte')

class Robot():
    def __init__(self,modelo):
        self.modelo=modelo
    
    def procesarData(self):
        print('Estoy procesando informacion.....')
    
    def saludar(self):
        print('Hola , soy un robot',self.nombre)

class Humanoide(Robot,Humano):
    def __init__(self, nombre, edad, modelo):
        Humano.__init__(self, nombre,edad)
        Robot.__init__(self, modelo)
    
    def quesoy(self):
        return "Soy un humanoide"

r2r2=Humanoide('R2-D2',12,'124-HE')
print(r2r2.quesoy())
r2r2.saludar()

print(Humano.__bases__)
print(Humano.__subclasses__())


