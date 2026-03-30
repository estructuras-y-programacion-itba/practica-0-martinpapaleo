class Cliente():
    # construir cliente
    # cualquier funcion dentro de una clase se le llama metodo de esa clase.

    def __init__(self, nombre, correo, telefono):
        #atributos de instancia
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.lista_pedidos = []

    # getters
    def getnombre(self):
        return self.nombre
    
    # setters permiten modificar la info de los atributos
    def setter_correo(self,correo_nuevo):
        self.correo = correo_nuevo

    def agregar_pedido(self, pedido):
        self.lista_pedidos.append(pedido)

    def mostrar_pedidos(self):
        return self.lista_pedidos

    def __str__(self): #  devuelve una cadena
        return f'Cliente: {self.nombre}, Correo: {self.correo}, Telefono: {self.telefono}'


agustin = Cliente('Agustin', 'agustin1@gmail.com', '1159472822')
print(agustin.getnombre())