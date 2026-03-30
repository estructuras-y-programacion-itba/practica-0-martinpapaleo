class Cliente():
    def __init__(self,nombre,correo,telefono):
        #Validaciones
        Cliente.validar_tel(telefono)

        # creacion de instancia
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.lista_pedidos = []
    def getternombre(self):
        return self.nombre
    def gettercorreo(self):
        return self.correo
    def gettertelefono(self):
        return self.telefono
    def settercorreo(self,correo):
        self.correo = correo    
    def settertelefono(self,telefono):
        self.telefono = telefono    
    def agregar_pedido(self,pedido):
        self.lista_pedidos.append(pedido)
    def mostrar_pedidos(self):
        for pedido in self.lista_pedidos:
            print(pedido)
        
    @staticmethod
    def validar_tel(telefono_: str):
        if not telefono_:
            raise ValueError(f'el atributo no puede estar vacio!')
        if not isinstance(telefono_, str):
            raise ValueError(f'el atributo "{telefono_}" debe ser string!')
        if not (10 <= len(telefono_)<= 12):           
            raise ValueError(f'el atributo {telefono_} debe tener entre 10 y 12 caracteres!')


try:
    pedro = Cliente('Pedro', 'pedro@gmail.com', 12)
    print(pedro.telefono)
    
    joaco = Cliente('Joaco', 'joaco@gmail.com', '1234567')
    print(joaco.telefono)
except ValueError as e:
    print(f'Error: {e}')

