class Cliente():
    def __init__(self,nombre,correo,telefono):
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

