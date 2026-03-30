class Cliente():
    PUNTOS_LEALTAD_INICIALES=100
    cantidadClientes=0
    dnis_clientes=[]
    
    # Construir 
    def __init__(self,id, nombre, correo, telefono):
        # atributos de instancia
        Cliente.validar_dni(id)
        Cliente.validar_existencia_dni(id)
        self.dni=id
        self.nombre=nombre
        self.correo=correo
        self.telefono=telefono
        self.lista_pedidos=[]
        self.puntos_lealtad=Cliente.PUNTOS_LEALTAD_INICIALES
        Cliente.cantidadClientes+=1
        Cliente.dnis_clientes.append(id)
        
    # metodos
    # Getters 

    def getternombre(self):
        return self.nombre
    
    def getterpuntos(self):
        return self.puntos_lealtad
    
    # Setters
    def setter_correo(self,correo_nuevo):
        self.correo=correo_nuevo
    
    #instancia
    def agregar_pedido(self,pedido):
        self.lista_pedidos.append(pedido)
        self.puntos_lealtad += 10  # Supongamos que cada pedido suma 10 puntos de lealtad
            
    def mostrar_pedidos(self):
        return self.lista_pedidos
    
    def __str__(self):
        return f"Cliente: {self.nombre}, DNI:{self.dni} Correo: {self.correo}, Teléfono: {self.telefono}"
    
    #método estático
    @staticmethod
    def validar_dni(dni):
        if type(dni)!=int or not(999999<dni<99999999):
            raise ValueError("DNI es invalido, porque debe ser un entero de entre 7 y 8 cifras")

    
    @staticmethod
    def validar_existencia_dni(dni):
        if dni in Cliente.dnis_clientes:
            raise ValueError("DNI ya registrado")
        
    #metodo de clase
    @classmethod
    def ver_total_clientes(cls):
        return cls.cantidadClientes
    
try:
    agustin=Cliente(1234567,"Agustin", "abrowne@itba.edu.ar", "1234567890")
    print(agustin)
    alberto=Cliente(1234567,"Agustin", "abrowne@itba.edu.ar", "1234567890")
    print(alberto)
    print(agustin.getterpuntos())
    # print(alberto.getternombre())
    # print(agustin.getternombre())
    # print(Cliente.ver_total_clientes())
    # print(agustin.ver_total_clientes())
except ValueError as e:
    print(f"Error: {e}")