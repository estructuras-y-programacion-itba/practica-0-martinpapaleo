class Cliente():
    tel_clientes = []
    def __init__(self,nombre,correo,telefono):
        #Validaciones
        if telefono in Cliente.tel_clientes:
            raise ValueError(f'Error, el tel {telefono} ya existe!')
        Cliente.validar_tel(telefono)

        # creacion de instancia
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono


        # modifico atributo de clase
        Cliente.tel_clientes.append(telefono)

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
            for num in telefono_:
                int(num)
        except ValueError:
            print(f'Error: todos los caracteres deben ser numericos')
# buscar libreria _str_ 

try:
    pedro = Cliente('Pedro', 'pedro@gmail.com', '1234567890')
    print(pedro.telefono)
    
    mati = Cliente('Matias', 'mati@gmail.com', 'a12345678ab')
    print(mati.telefono)
    
    joaco = Cliente('Joaco', 'joaco@gmail.com', '1234567')
    print(joaco.telefono)

    luca = Cliente('Luca', 'luca@gmail.com', '1234567890')
    print(luca.telefono)

except ValueError as e:
    print(f'Error: {e}')

