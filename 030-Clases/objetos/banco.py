#
from objetos.cliente import Cliente

class Banco:
    # aca defino los atributos de clase
    nombreBanco ="X"           # publico Banco.nombreBanco ="X" ok
    __ClientesSuspendidos = [] # privado solo se modifica con metodos de la clase  def suspenderCliente(cls,nombre):
    _datoProtegido="protegido" # protegido solo se modifica de la clase y subclases 
    def __init__(self):
        # aca defino los atributos de instancia
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")
        self.__datoprivado = "privado"
    #metodos de clase
    @classmethod
    def suspenderCliente(cls,nombre):
        cls.__ClientesSuspendidos.append(nombre)
    @classmethod
    def clientesSuspendidos(cls):
        return cls.__ClientesSuspendidos
    
    # genero un propiedad
    @property
    def datoprivado(self):
        return self.__datoprivado
    @datoprivado.setter
    def datoprivado(self, datoprivado):
        self.__datoprivado = datoprivado
    #metodos de instancia
    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)
    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero en el banco es: {}".format(total))
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
    
